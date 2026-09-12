/* Faceted search over the book's bibliography.
 *
 * Click elements on the periodic table, pick extractants / techniques /
 * feedstocks / topics, and the 758-entry bibliography filters down. Everything
 * runs in the reader's browser against one JSON file; there is no backend, in
 * keeping with the rest of this site.
 *
 * Two conventions borrowed from static/chat/chat.js, both learned the hard way
 * there: MyST v2 emits a Remix SPA, so (1) the mount point has to be found
 * again after every client-side navigation -- hence the MutationObserver -- and
 * (2) asset paths are stored base-relative and prefixed at runtime from
 * window.__REE_SEARCH_BASE__, so the page survives being served from a
 * repository subpath.
 *
 * Filter semantics: OR within a facet group, AND across groups. That is what
 * faceted search normally means and what a reader expects. The elements group
 * additionally offers "all of", because "papers about Nd *and* Dy" is the
 * separations question and "papers about Nd or Dy" is not.
 */
(function () {
  "use strict";

  var BASE = window.__REE_SEARCH_BASE__ || "";
  var PAGE_SIZE = 40;

  var data = null;
  var loading = false;
  var host = null;

  // Selected facet values, by group id. Element mode is separate because it is
  // the only group with an any/all switch.
  var sel = Object.create(null);
  var elMode = "any";
  var query = "";
  var shown = PAGE_SIZE;

  /* ---------------------------------------------------------------- utils */

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }

  function selectedOf(g) { return sel[g] || (sel[g] = []); }

  function toggle(g, v) {
    var a = selectedOf(g);
    var i = a.indexOf(v);
    if (i < 0) a.push(v); else a.splice(i, 1);
    shown = PAGE_SIZE;
    writeHash();
    render();
  }

  function anySelected() {
    if (query) return true;
    for (var g in sel) if (sel[g].length) return true;
    return false;
  }

  function clearAll() {
    sel = Object.create(null);
    query = "";
    shown = PAGE_SIZE;
    writeHash();
    render();
  }

  /* --------------------------------------------------------- the filtering */

  // A record matches a group when it carries at least one of the selected
  // values -- except elements under "all of", which requires every one.
  function matchesGroup(rec, g, want) {
    if (!want.length) return true;
    var have = (rec.f && rec.f[g]) || [];
    if (g === "element" && elMode === "all") {
      for (var i = 0; i < want.length; i++) if (have.indexOf(want[i]) < 0) return false;
      return true;
    }
    for (var j = 0; j < want.length; j++) if (have.indexOf(want[j]) >= 0) return true;
    return false;
  }

  function matchesText(rec, q) {
    if (!q) return true;
    return rec._s.indexOf(q) >= 0;
  }

  // `skip` excludes one group from the test, which is what makes the counts on
  // an unselected chip mean "how many you would get if you added this" rather
  // than "how many match everything including me" (always 0 for the unselected).
  function filtered(skip) {
    var q = query.toLowerCase();
    var out = [];
    for (var i = 0; i < data.records.length; i++) {
      var r = data.records[i];
      if (!matchesText(r, q)) continue;
      var ok = true;
      for (var g in sel) {
        if (g === skip) continue;
        if (!matchesGroup(r, g, sel[g])) { ok = false; break; }
      }
      if (ok) out.push(r);
    }
    return out;
  }

  function countsFor(g) {
    var pool = filtered(g);
    var c = Object.create(null);
    for (var i = 0; i < pool.length; i++) {
      var vs = (pool[i].f && pool[i].f[g]) || [];
      for (var j = 0; j < vs.length; j++) c[vs[j]] = (c[vs[j]] || 0) + 1;
    }
    return c;
  }

  /* ------------------------------------------------------- URL round-trip */

  // A filtered view is a thing a reader will want to send to someone, so it
  // lives in the hash. Compact on purpose: `#e=Nd,Dy&mode=all&technique=...`.
  function writeHash() {
    var parts = [];
    for (var g in sel) if (sel[g].length) parts.push(g + "=" + sel[g].map(encodeURIComponent).join(","));
    if (elMode !== "any") parts.push("mode=all");
    if (query) parts.push("q=" + encodeURIComponent(query));
    var h = parts.join("&");
    var url = location.pathname + location.search + (h ? "#" + h : "");
    history.replaceState(null, "", url);
  }

  function readHash() {
    sel = Object.create(null);
    elMode = "any";
    query = "";
    var h = location.hash.replace(/^#/, "");
    if (!h) return;
    h.split("&").forEach(function (kv) {
      var i = kv.indexOf("=");
      if (i < 0) return;
      var k = kv.slice(0, i), v = kv.slice(i + 1);
      if (k === "mode") { if (v === "all") elMode = "all"; return; }
      if (k === "q") { query = decodeURIComponent(v); return; }
      sel[k] = v.split(",").map(decodeURIComponent).filter(Boolean);
    });
  }

  /* ------------------------------------------------------------ rendering */

  function renderPTable(counts) {
    var wrap = el("div", "rs-ptable");
    var byGrp = { 0: [], 1: [], 2: [] };
    data.elements.forEach(function (e) { byGrp[e[3]].push(e); });

    function strip(list, label, narrow) {
      if (!list.length) return;
      var lab = el("div", "rs-ptable-label", label);
      wrap.appendChild(lab);
      var row = el("div", "rs-ptable-row" + (narrow ? " rs-narrow" : ""));
      list.forEach(function (e) {
        var sym = e[0], name = e[1], z = e[2], grp = e[3];
        var n = counts[sym] || 0;
        var b = el("button", "rs-el");
        b.type = "button";
        b.setAttribute("data-grp", grp);
        var on = selectedOf("element").indexOf(sym) >= 0;
        b.setAttribute("aria-pressed", on ? "true" : "false");
        b.disabled = !n && !on;
        b.title = name + " — " + n + (n === 1 ? " work" : " works");
        b.appendChild(el("span", "rs-el-z", z));
        b.appendChild(el("span", "rs-el-sym", sym));
        b.appendChild(el("span", "rs-el-n", name));
        b.appendChild(el("span", "rs-el-c", n || "·"));
        b.addEventListener("click", function () { toggle("element", sym); });
        row.appendChild(b);
      });
      wrap.appendChild(row);
    }

    // Sc and Y are group 3; the lanthanide strip hangs below them, which is
    // how the table is drawn and why these are three rows and not one.
    strip(byGrp[2].filter(function (e) { return e[0] === "Sc"; }).concat(
          byGrp[1].filter(function (e) { return e[0] === "Y"; })),
          "Group 3", true);
    strip(byGrp[0].concat(byGrp[1].filter(function (e) { return e[0] !== "Y"; }))
            .sort(function (a, b) { return a[2] - b[2]; }),
          "Lanthanides — light (blue) and heavy (green)");
    strip(byGrp[2].filter(function (e) { return e[0] !== "Sc"; }),
          "Travels with the ores, not a rare earth", true);
    return wrap;
  }

  function renderGroup(gid, label, values, counts, labels) {
    var d = el("details", "rs-group");
    // Open by default: a collapsed facet is a facet nobody discovers, and
    // the whole point of the page is to show what there is to filter by.
    d.open = true;
    var s = el("summary");
    s.appendChild(el("span", null, label));
    var n = selectedOf(gid).length;
    s.appendChild(el("span", "rs-group-n", n ? n + " selected" : values.length + ""));
    d.appendChild(s);

    var box = el("div", "rs-chips");
    // Most-populated first: a reader scanning for a way in is better served by
    // the facets that actually cut the corpus than by alphabetical order.
    values.slice().sort(function (a, b) {
      return (counts[b] || 0) - (counts[a] || 0) || String(a).localeCompare(String(b));
    }).forEach(function (v) {
      var c = counts[v] || 0;
      var on = selectedOf(gid).indexOf(v) >= 0;
      if (!c && !on) return;
      var b = el("button", "rs-chip");
      b.type = "button";
      b.setAttribute("aria-pressed", on ? "true" : "false");
      b.appendChild(el("span", null, (labels && labels[v]) || v));
      b.appendChild(el("span", "rs-chip-n", c));
      b.addEventListener("click", function () { toggle(gid, v); });
      box.appendChild(b);
    });
    if (!box.children.length) box.appendChild(el("span", "rs-tag", "nothing left to narrow by"));
    d.appendChild(box);
    return d;
  }

  function renderHit(rec) {
    var li = el("li", "rs-hit");
    var t = el("div", "rs-hit-t");
    if (rec.doi || rec.url) {
      var a = el("a", null, rec.title);
      a.href = rec.doi ? "https://doi.org/" + rec.doi : rec.url;
      a.rel = "noopener";
      t.appendChild(a);
    } else {
      t.textContent = rec.title;
    }
    li.appendChild(t);

    var meta = [rec.authors, rec.year, rec.venue].filter(Boolean).join(" · ");
    var m = el("div", "rs-hit-m", meta);
    if (rec.cited && rec.cited.length) {
      m.appendChild(el("span", null, " — cited in "));
      rec.cited.forEach(function (c, i) {
        if (i) m.appendChild(el("span", null, ", "));
        var a = el("a", null, c[1]);
        a.href = BASE + c[0];
        m.appendChild(a);
      });
    }
    li.appendChild(m);

    // The facets this record carries, with the ones you filtered on lit up --
    // so a hit shows *why* it is a hit.
    var f = el("div", "rs-hit-f");
    ["element", "extractant", "technique", "feedstock", "topic"].forEach(function (g) {
      ((rec.f && rec.f[g]) || []).forEach(function (v) {
        var on = selectedOf(g).indexOf(v) >= 0;
        f.appendChild(el("span", "rs-tag" + (on ? " on" : ""), labelFor(g, v)));
      });
    });
    if (f.children.length) li.appendChild(f);
    return li;
  }

  var TOPIC_LABEL = null;
  function labelFor(g, v) {
    if (g !== "topic") return v;
    if (!TOPIC_LABEL) {
      TOPIC_LABEL = Object.create(null);
      data.topics.forEach(function (t) { TOPIC_LABEL[t[0]] = t[1]; });
    }
    return TOPIC_LABEL[v] || v;
  }

  function render() {
    if (!host) return;
    host.textContent = "";

    host.appendChild(renderPTable(countsFor("element")));

    var groups = el("div", "rs-groups");
    data.groups.forEach(function (g) {
      var gid = g[0], label = g[1], values = g[2];
      if (gid === "element") return;
      var labels = gid === "topic" ? (function () {
        var m = Object.create(null);
        data.topics.forEach(function (t) { m[t[0]] = t[1]; });
        return m;
      })() : null;
      groups.appendChild(renderGroup(gid, label, values, countsFor(gid), labels));
    });
    host.appendChild(groups);

    var ctl = el("div", "rs-controls");
    var q = el("input", "rs-q");
    q.type = "search";
    q.placeholder = "Filter by author, title or journal…";
    q.value = query;
    q.setAttribute("aria-label", "Filter by author, title or journal");
    q.addEventListener("input", function () {
      query = q.value;
      shown = PAGE_SIZE;
      writeHash();
      var pos = q.selectionStart;
      render();
      var nq = host.querySelector(".rs-q");
      if (nq) { nq.focus(); nq.setSelectionRange(pos, pos); }
    });
    ctl.appendChild(q);

    if (selectedOf("element").length > 1) {
      var mode = el("label", "rs-mode");
      var cb = el("input");
      cb.type = "checkbox";
      cb.checked = elMode === "all";
      cb.addEventListener("change", function () {
        elMode = cb.checked ? "all" : "any";
        shown = PAGE_SIZE;
        writeHash();
        render();
      });
      mode.appendChild(cb);
      mode.appendChild(el("span", null, "must cover all selected elements"));
      ctl.appendChild(mode);
    }

    var clear = el("button", "rs-btn", "Clear filters");
    clear.type = "button";
    clear.disabled = !anySelected();
    clear.addEventListener("click", clearAll);
    ctl.appendChild(clear);
    host.appendChild(ctl);

    var hits = filtered(null);
    var c = el("div", "rs-count");
    c.appendChild(el("strong", null, hits.length));
    c.appendChild(el("span", null, (hits.length === 1 ? " work" : " works") +
      (anySelected() ? " match these filters" : " in the bibliography") +
      " · " + data.records.length + " total"));
    host.appendChild(c);

    if (!hits.length) {
      host.appendChild(el("div", "rs-empty-msg",
        "Nothing matches that combination. Clear a filter and try again — " +
        "an empty result is often real: much of this literature treats one " +
        "element pair with one extractant, and the cross terms have not been studied."));
      return;
    }

    var ul = el("ul", "rs-results");
    hits.slice(0, shown).forEach(function (r) { ul.appendChild(renderHit(r)); });
    host.appendChild(ul);

    if (hits.length > shown) {
      var more = el("div", "rs-more");
      var b = el("button", "rs-btn",
        "Show " + Math.min(PAGE_SIZE, hits.length - shown) + " more of " + hits.length);
      b.type = "button";
      b.addEventListener("click", function () { shown += PAGE_SIZE; render(); });
      more.appendChild(b);
      host.appendChild(more);
    }
  }

  /* ------------------------------------------------------------- mounting */

  function prepare(d) {
    // One lowercased haystack per record for the text box, built once.
    d.records.forEach(function (r) {
      r._s = (r.authors + " " + r.title + " " + r.venue + " " + r.year + " " + r.key).toLowerCase();
    });
    return d;
  }

  function load() {
    if (loading || data) { render(); return; }
    loading = true;
    host.appendChild(el("div", "rs-loading", "Loading the bibliography…"));
    fetch(BASE + "/search/facets.json")
      .then(function (r) {
        if (!r.ok) throw new Error("HTTP " + r.status);
        return r.json();
      })
      .then(function (d) {
        data = prepare(d);
        loading = false;
        readHash();
        render();
      })
      .catch(function (err) {
        loading = false;
        host.textContent = "";
        host.appendChild(el("div", "rs-empty-msg",
          "The search index did not load (" + err.message +
          "). The full bibliography is on the Bibliography page."));
      });
  }

  // `src/95-explore.md` carries a literal `<div id="ree-search">`, which MyST
  // turns into a real AST node -- so React renders the container itself and
  // hydration has nothing to disagree about. That matters: the first version
  // of this file replaced a placeholder paragraph on DOMContentLoaded, which
  // mutated the DOM *before* React hydrated and produced React error #418 and
  // a container that React then wiped. Never touch this subtree until
  // hydration has finished.
  function findHost() {
    return document.getElementById("ree-search");
  }

  // React re-creates the div on client-side navigation, and a re-render resets
  // its children. Either way what we rendered is gone, and `mounted` is how we
  // notice: the flag lives on the element, so a fresh element fails the test
  // by not having it and a reset element fails it by having lost our content.
  function needsMount(h) {
    return h.dataset.reeMounted !== "1" || !h.querySelector(".rs-ptable, .rs-loading, .rs-empty-msg");
  }

  function attach() {
    var h = findHost();
    if (!h || !needsMount(h)) return;
    h.dataset.reeMounted = "1";
    host = h;
    load();
  }

  // Hydration runs from a module script, which is done by the time `load`
  // fires; two animation frames past that is belt and braces. Everything after
  // this point is ordinary DOM work on a subtree React has finished with.
  // The stylesheet is added here rather than as a <link> in the page, because
  // Remix reconciles <body> on hydration and deletes anything injected before
  // </body> -- which is exactly what happened to the first version: the CSS
  // fetched with a 200, was dropped from the document, and the widget rendered
  // correctly and completely unstyled. The <script> survives that because it
  // has already executed by then. Adding the link from here, after hydration,
  // puts it somewhere React is not reconciling.
  function ensureStyles() {
    if (document.getElementById("ree-search-css")) return;
    var l = document.createElement("link");
    l.id = "ree-search-css";
    l.rel = "stylesheet";
    l.href = BASE + "/search/search.css";
    document.head.appendChild(l);
  }

  function whenHydrated(fn) {
    function go() {
      var done = false;
      function once() { if (!done) { done = true; fn(); } }
      requestAnimationFrame(function () { requestAnimationFrame(once); });
      setTimeout(once, 60);
    }
    if (document.readyState === "complete") go();
    else window.addEventListener("load", go);
  }

  function start() {
    whenHydrated(function () {
      ensureStyles();
      attach();
      new MutationObserver(function () { attach(); })
        .observe(document.body, { childList: true, subtree: true });
    });
    window.addEventListener("hashchange", function () {
      if (!host || !data) return;
      readHash();
      shown = PAGE_SIZE;
      render();
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start);
  } else {
    start();
  }
})();
