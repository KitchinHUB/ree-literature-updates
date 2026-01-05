#!/usr/bin/env python3
"""
Rare Earth Literature Monitor

Searches OpenAlex and web sources for recent publications and news
related to rare earth element separation technologies.

Usage:
    python literature_monitor.py                    # Last 7 days
    python literature_monitor.py --days 30          # Last 30 days
    python literature_monitor.py --output report.md # Custom output file
    python literature_monitor.py --slack            # Send notification to Slack

Environment Variables:
    SLACK_WEBHOOK_URL  - Incoming webhook URL for simple notifications
    SLACK_BOT_TOKEN    - Bot token for file uploads (optional)
    SLACK_CHANNEL      - Channel ID for file uploads (optional)
"""

import argparse
import json
import os
import re
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional
import urllib.parse
import urllib.request

# Search topics for rare earth separation research
SEARCH_TOPICS = [
    # Core separation technologies
    "rare earth separation",
    "rare earth extraction",
    "lanthanide separation",
    "REE solvent extraction",
    "rare earth ion exchange",

    # Specific techniques
    "rare earth membrane separation",
    "rare earth electrochemical separation",
    "rare earth precipitation",
    "rare earth chromatography",

    # Extractants and materials
    "rare earth extractant",
    "ionic liquid rare earth",
    "deep eutectic solvent rare earth",

    # Applications and sources
    "rare earth recycling",
    "rare earth urban mining",
    "rare earth permanent magnet recycling",
    "rare earth e-waste",

    # Environmental and sustainability
    "green rare earth separation",
    "sustainable rare earth extraction",
    "rare earth environmental impact",

    # Supply chain and policy
    "rare earth supply chain",
    "critical minerals separation",
]

# GitHub repository for report hosting
GITHUB_REPO_URL = "https://github.com/KitchinHUB/ree-literature-updates"

# OpenAlex concepts for filtering
OPENALEX_CONCEPTS = [
    "C185592680",  # Rare earth element
    "C41008148",   # Solvent extraction
    "C108827166",  # Ion exchange
    "C187320778",  # Hydrometallurgy
    "C142362112",  # Lanthanide
]

# Terms that indicate a paper is relevant to rare earth research
# Papers must contain at least one of these terms in title, abstract, or concepts
RELEVANCE_TERMS = [
    # General terms
    "rare earth", "rare-earth", "ree ", "rees ", "rees.", "rees,",
    "lanthanide", "lanthanoid", "actinide",
    "critical mineral", "critical metal",

    # Individual elements (lanthanides)
    "lanthanum", "cerium", "praseodymium", "neodymium", "promethium",
    "samarium", "europium", "gadolinium", "terbium", "dysprosium",
    "holmium", "erbium", "thulium", "ytterbium", "lutetium",
    "scandium", "yttrium",

    # Element symbols with context (to avoid false positives)
    " la ", " ce ", " pr ", " nd ", " pm ", " sm ", " eu ", " gd ",
    " tb ", " dy ", " ho ", " er ", " tm ", " yb ", " lu ", " sc ", " y ",
    "la3+", "ce3+", "ce4+", "nd3+", "eu3+", "gd3+", "tb3+", "dy3+",
    "la(iii)", "ce(iii)", "nd(iii)", "eu(iii)", "gd(iii)", "dy(iii)",

    # Common REE materials and applications
    "ndfeb", "nd-fe-b", "nd2fe14b", "neodymium magnet",
    "bastnäsite", "bastnasite", "monazite", "xenotime", "ion-adsorption",
    "f-element", "f-block", "4f electron",

    # REE-specific separation terms
    "lanthanide separation", "ree separation", "ree extraction",
    "rare earth recycl", "magnet recycl",
]


def query_openalex(
    query: str,
    from_date: str,
    per_page: int = 25,
    cursor: str = "*"
) -> dict:
    """
    Query OpenAlex API for works matching the search query.

    Args:
        query: Search query string
        from_date: ISO date string (YYYY-MM-DD) for filtering
        per_page: Results per page
        cursor: Pagination cursor

    Returns:
        API response as dict
    """
    base_url = "https://api.openalex.org/works"

    params = {
        "search": query,
        "filter": f"from_publication_date:{from_date}",
        "sort": "publication_date:desc",
        "per-page": str(per_page),
        "cursor": cursor,
        "mailto": "literature-monitor@example.com",  # Polite pool
    }

    url = f"{base_url}?{urllib.parse.urlencode(params)}"

    try:
        req = urllib.request.Request(url, headers={"User-Agent": "LiteratureMonitor/1.0"})
        with urllib.request.urlopen(req, timeout=30) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"  Warning: OpenAlex query failed: {e}")
        return {"results": [], "meta": {"count": 0}}


def search_openalex_all_topics(from_date: str, max_per_topic: int = 10) -> list[dict]:
    """
    Search OpenAlex for all configured topics.

    Returns deduplicated list of works.
    """
    all_works = {}

    for topic in SEARCH_TOPICS:
        print(f"  Searching OpenAlex: {topic}")
        result = query_openalex(topic, from_date, per_page=max_per_topic)

        for work in result.get("results", []):
            work_id = work.get("id", "")
            if work_id and work_id not in all_works:
                all_works[work_id] = work

    return list(all_works.values())


def extract_work_info(work: dict) -> dict:
    """Extract relevant information from an OpenAlex work."""
    # Get authors
    authors = []
    for authorship in work.get("authorships", [])[:5]:  # Limit to first 5
        author = authorship.get("author", {})
        name = author.get("display_name", "Unknown")
        authors.append(name)

    if len(work.get("authorships", [])) > 5:
        authors.append("et al.")

    # Get primary source/journal
    source = work.get("primary_location", {}).get("source") or {}
    journal = source.get("display_name", "Unknown Source")

    # Get DOI
    doi = work.get("doi", "")
    if doi and not doi.startswith("http"):
        doi = f"https://doi.org/{doi}"

    # Get abstract
    abstract = ""
    if work.get("abstract_inverted_index"):
        # Reconstruct abstract from inverted index
        inv_index = work["abstract_inverted_index"]
        words = [""] * (max(max(positions) for positions in inv_index.values()) + 1)
        for word, positions in inv_index.items():
            for pos in positions:
                words[pos] = word
        abstract = " ".join(words)

    # Get concepts/topics
    concepts = [c.get("display_name", "") for c in work.get("concepts", [])[:5]]

    return {
        "id": work.get("id", ""),
        "title": work.get("title", "Untitled"),
        "authors": authors,
        "publication_date": work.get("publication_date", ""),
        "journal": journal,
        "doi": doi,
        "url": work.get("id", "").replace("https://openalex.org/", "https://openalex.org/works/"),
        "abstract": abstract[:500] + "..." if len(abstract) > 500 else abstract,
        "concepts": concepts,
        "cited_by_count": work.get("cited_by_count", 0),
        "type": work.get("type", "unknown"),
        "open_access": work.get("open_access", {}).get("is_oa", False),
    }


def is_relevant_to_ree(work: dict) -> bool:
    """
    Check if a work is actually relevant to rare earth element research.

    Filters out false positives from broad OpenAlex searches by requiring
    at least one REE-related term in the title, abstract, or concepts.

    Args:
        work: Processed work dictionary

    Returns:
        True if the work appears relevant to REE research
    """
    # Combine searchable text fields
    title = work.get("title", "").lower()
    abstract = work.get("abstract", "").lower()
    concepts = " ".join(work.get("concepts", [])).lower()

    # Add spaces around text to help with word boundary matching
    searchable_text = f" {title} {abstract} {concepts} "

    # Check for any relevance term
    for term in RELEVANCE_TERMS:
        if term.lower() in searchable_text:
            return True

    return False


def filter_relevant_works(works: list[dict]) -> tuple[list[dict], list[dict]]:
    """
    Filter works to only include those relevant to REE research.

    Args:
        works: List of processed work dictionaries

    Returns:
        Tuple of (relevant_works, filtered_out_works)
    """
    relevant = []
    filtered_out = []

    for work in works:
        if is_relevant_to_ree(work):
            relevant.append(work)
        else:
            filtered_out.append(work)

    return relevant, filtered_out


def categorize_works(works: list[dict]) -> dict[str, list[dict]]:
    """
    Categorize works into topic groups based on title and concepts.
    """
    categories = {
        "Separation Technologies": [],
        "Extractants & Materials": [],
        "Recycling & Urban Mining": [],
        "Environmental & Sustainability": [],
        "Supply Chain & Policy": [],
        "Other": [],
    }

    for work in works:
        title_lower = work["title"].lower()
        concepts_lower = " ".join(work["concepts"]).lower()
        combined = title_lower + " " + concepts_lower

        if any(kw in combined for kw in ["recycl", "urban mining", "e-waste", "waste", "secondary"]):
            categories["Recycling & Urban Mining"].append(work)
        elif any(kw in combined for kw in ["extractant", "ionic liquid", "eutectic", "ligand", "complexa"]):
            categories["Extractants & Materials"].append(work)
        elif any(kw in combined for kw in ["green", "sustainab", "environment", "pollution", "toxic"]):
            categories["Environmental & Sustainability"].append(work)
        elif any(kw in combined for kw in ["supply chain", "policy", "critical mineral", "strategic", "china"]):
            categories["Supply Chain & Policy"].append(work)
        elif any(kw in combined for kw in ["separat", "extract", "ion exchange", "membrane", "electro"]):
            categories["Separation Technologies"].append(work)
        else:
            categories["Other"].append(work)

    # Remove empty categories
    return {k: v for k, v in categories.items() if v}


# =============================================================================
# Slack Integration
# =============================================================================

def send_slack_webhook(
    webhook_url: str,
    message: str,
    blocks: list = None,
    attachments: list = None
) -> bool:
    """
    Send a message to Slack via incoming webhook.

    Args:
        webhook_url: Slack incoming webhook URL
        message: Fallback text message
        blocks: Optional Block Kit blocks for rich formatting
        attachments: Optional attachments

    Returns:
        True if successful, False otherwise
    """
    payload = {"text": message}

    if blocks:
        payload["blocks"] = blocks
    if attachments:
        payload["attachments"] = attachments

    data = json.dumps(payload).encode("utf-8")

    try:
        req = urllib.request.Request(
            webhook_url,
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=30) as response:
            return response.status == 200
    except Exception as e:
        print(f"Warning: Slack webhook failed: {e}")
        return False


def upload_slack_file(
    token: str,
    channel: str,
    file_path: Path,
    title: str = None,
    initial_comment: str = None
) -> bool:
    """
    Upload a file to Slack using the Bot API.

    Args:
        token: Slack Bot OAuth token
        channel: Channel ID to upload to
        file_path: Path to file to upload
        title: Optional title for the file
        initial_comment: Optional message to accompany the file

    Returns:
        True if successful, False otherwise
    """
    url = "https://slack.com/api/files.upload"

    # Read file content
    with open(file_path, "rb") as f:
        file_content = f.read()

    # Build multipart form data manually (avoiding external dependencies)
    boundary = "----WebKitFormBoundary7MA4YWxkTrZu0gW"

    body_parts = []

    # Add channel
    body_parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="channels"\r\n\r\n{channel}')

    # Add title if provided
    if title:
        body_parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="title"\r\n\r\n{title}')

    # Add initial comment if provided
    if initial_comment:
        body_parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="initial_comment"\r\n\r\n{initial_comment}')

    # Add filename
    filename = file_path.name
    body_parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="filename"\r\n\r\n{filename}')

    body = "\r\n".join(body_parts).encode("utf-8")
    body += f'\r\n--{boundary}\r\nContent-Disposition: form-data; name="file"; filename="{filename}"\r\nContent-Type: text/markdown\r\n\r\n'.encode("utf-8")
    body += file_content
    body += f"\r\n--{boundary}--\r\n".encode("utf-8")

    try:
        req = urllib.request.Request(
            url,
            data=body,
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": f"multipart/form-data; boundary={boundary}",
            },
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=60) as response:
            result = json.loads(response.read().decode())
            return result.get("ok", False)
    except Exception as e:
        print(f"Warning: Slack file upload failed: {e}")
        return False


def create_slack_summary(
    works: list[dict],
    categorized: dict[str, list[dict]],
    from_date: str,
    to_date: str,
    report_path: Path = None
) -> tuple[str, list]:
    """
    Create a Slack message summarizing the literature update.

    Returns:
        tuple: (fallback_text, blocks)
    """
    total = len(works)

    # Fallback text
    fallback = f"📚 Rare Earth Literature Update: {total} new publications ({from_date} to {to_date})"

    # Block Kit formatting for rich message
    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "📚 Rare Earth Literature Update",
                "emoji": True
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*{total} new publications* found from {from_date} to {to_date}"
            }
        },
        {"type": "divider"}
    ]

    # Category breakdown
    if categorized:
        category_lines = []
        for category, cat_works in categorized.items():
            emoji = {
                "Separation Technologies": "🔬",
                "Extractants & Materials": "🧪",
                "Recycling & Urban Mining": "♻️",
                "Environmental & Sustainability": "🌱",
                "Supply Chain & Policy": "📊",
                "Other": "📄"
            }.get(category, "📄")
            category_lines.append(f"{emoji} *{category}*: {len(cat_works)}")

        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "\n".join(category_lines)
            }
        })

    # Highlight top papers (by citation count or recency)
    if works:
        blocks.append({"type": "divider"})
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*📌 Recent Highlights:*"
            }
        })

        # Get top 3 most recent with abstracts
        highlights = sorted(works, key=lambda x: x["publication_date"], reverse=True)[:3]

        for work in highlights:
            title = work["title"][:100] + "..." if len(work["title"]) > 100 else work["title"]
            authors = ", ".join(work["authors"][:2])
            if len(work["authors"]) > 2:
                authors += " et al."

            text = f"• *{title}*\n  _{authors}_ ({work['journal']})"
            if work["doi"]:
                text += f"\n  <{work['doi']}|View paper>"

            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": text
                }
            })

    # Add report link/note if available
    if report_path:
        github_link = f"{GITHUB_REPO_URL}/blob/main/{report_path}"
        blocks.append({"type": "divider"})
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"📎 <{github_link}|View full report on GitHub>"
            }
        })

    return fallback, blocks


def notify_slack(
    works: list[dict],
    categorized: dict[str, list[dict]],
    from_date: str,
    to_date: str,
    report_path: Path,
    upload_file: bool = False
) -> bool:
    """
    Send Slack notification about the literature update.

    Uses SLACK_WEBHOOK_URL for simple notifications.
    Uses SLACK_BOT_TOKEN + SLACK_CHANNEL for file uploads.

    Args:
        works: List of processed works
        categorized: Works organized by category
        from_date: Start date of search period
        to_date: End date of search period
        report_path: Path to the generated report
        upload_file: Whether to upload the full report file

    Returns:
        True if notification sent successfully
    """
    webhook_url = os.environ.get("SLACK_WEBHOOK_URL")
    bot_token = os.environ.get("SLACK_BOT_TOKEN")
    channel = os.environ.get("SLACK_CHANNEL")

    if not webhook_url and not bot_token:
        print("Warning: No Slack credentials configured")
        print("Set SLACK_WEBHOOK_URL or SLACK_BOT_TOKEN environment variable")
        return False

    # Create summary message
    fallback, blocks = create_slack_summary(
        works, categorized, from_date, to_date, report_path
    )

    success = False

    # Send webhook notification
    if webhook_url:
        print("Sending Slack notification...")
        success = send_slack_webhook(webhook_url, fallback, blocks)
        if success:
            print("✓ Slack notification sent")

    # Upload file if configured and requested
    if upload_file and bot_token and channel:
        print("Uploading report to Slack...")
        title = f"Literature Update {to_date}"
        comment = f"📚 Rare Earth Literature Update: {len(works)} publications"
        file_success = upload_slack_file(bot_token, channel, report_path, title, comment)
        if file_success:
            print("✓ Report uploaded to Slack")
        success = success or file_success

    return success


def format_citation(work: dict) -> str:
    """Format a work as a citation string."""
    authors_str = ", ".join(work["authors"][:3])
    if len(work["authors"]) > 3:
        authors_str += " et al."

    year = work["publication_date"][:4] if work["publication_date"] else "n.d."

    citation = f"{authors_str} ({year}). {work['title']}. *{work['journal']}*."

    if work["doi"]:
        citation += f" [{work['doi']}]({work['doi']})"

    return citation


def format_bibtex(work: dict, key: str) -> str:
    """Format a work as a BibTeX entry."""
    authors_bibtex = " and ".join(work["authors"])
    year = work["publication_date"][:4] if work["publication_date"] else ""

    # Clean title for BibTeX
    title = work["title"].replace("{", "").replace("}", "")

    entry = f"""@article{{{key},
  author = {{{authors_bibtex}}},
  title = {{{{{title}}}}},
  journal = {{{work['journal']}}},
  year = {{{year}}},
  doi = {{{work['doi'].replace('https://doi.org/', '') if work['doi'] else ''}}},
  url = {{{work['url']}}},
}}
"""
    return entry


def generate_report(
    works: list[dict],
    from_date: str,
    to_date: str,
    output_path: Path
) -> str:
    """
    Generate a markdown report of the literature search results.
    """
    categorized = categorize_works(works)

    report = f"""# Rare Earth Separation Literature Update

**Report Period:** {from_date} to {to_date}
**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}
**Total Publications Found:** {len(works)}

---

## Executive Summary

This report summarizes recent publications related to rare earth element separation
technologies discovered through OpenAlex database searches. Publications are
categorized by topic area for easier navigation.

### Publications by Category

| Category | Count |
|----------|-------|
"""

    for category, cat_works in categorized.items():
        report += f"| {category} | {len(cat_works)} |\n"

    report += "\n---\n\n"

    # Detailed sections for each category
    for category, cat_works in categorized.items():
        report += f"## {category}\n\n"

        # Sort by publication date (newest first)
        cat_works.sort(key=lambda x: x["publication_date"], reverse=True)

        for i, work in enumerate(cat_works, 1):
            oa_badge = "🔓" if work["open_access"] else "🔒"

            report += f"### {i}. {work['title']}\n\n"
            report += f"**Authors:** {', '.join(work['authors'])}\n\n"
            report += f"**Published:** {work['publication_date']} | "
            report += f"**Journal:** {work['journal']} | "
            report += f"**Citations:** {work['cited_by_count']} | "
            report += f"**Access:** {oa_badge}\n\n"

            if work["doi"]:
                report += f"**DOI:** [{work['doi']}]({work['doi']})\n\n"

            if work["abstract"]:
                report += f"**Abstract:** {work['abstract']}\n\n"

            if work["concepts"]:
                report += f"**Topics:** {', '.join(work['concepts'])}\n\n"

            report += "---\n\n"

    # Bibliography section
    report += "## Full Bibliography\n\n"

    for i, work in enumerate(works, 1):
        report += f"{i}. {format_citation(work)}\n\n"

    # BibTeX section
    report += "\n## BibTeX Entries\n\n```bibtex\n"

    for i, work in enumerate(works, 1):
        # Create a key from first author's last name and year
        first_author = work["authors"][0] if work["authors"] else "Unknown"
        last_name = first_author.split()[-1].lower()
        year = work["publication_date"][:4] if work["publication_date"] else "0000"
        key = f"{last_name}{year}_{i}"

        report += format_bibtex(work, key)

    report += "```\n"

    # Write report
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report)

    return report


def main():
    parser = argparse.ArgumentParser(
        description="Monitor rare earth separation literature"
    )
    parser.add_argument(
        "--days", type=int, default=7,
        help="Number of days to look back (default: 7)"
    )
    parser.add_argument(
        "--output", type=str, default=None,
        help="Output file path (default: reports/YYYY-MM-DD_literature_update.md)"
    )
    parser.add_argument(
        "--max-per-topic", type=int, default=15,
        help="Maximum results per search topic (default: 15)"
    )
    parser.add_argument(
        "--slack", action="store_true",
        help="Send notification to Slack (requires SLACK_WEBHOOK_URL env var)"
    )
    parser.add_argument(
        "--slack-upload", action="store_true",
        help="Upload full report to Slack (requires SLACK_BOT_TOKEN and SLACK_CHANNEL)"
    )

    args = parser.parse_args()

    # Calculate date range
    to_date = datetime.now()
    from_date = to_date - timedelta(days=args.days)

    from_date_str = from_date.strftime("%Y-%m-%d")
    to_date_str = to_date.strftime("%Y-%m-%d")

    print(f"Searching for publications from {from_date_str} to {to_date_str}")
    print(f"Searching {len(SEARCH_TOPICS)} topics...")

    # Search OpenAlex
    works = search_openalex_all_topics(from_date_str, max_per_topic=args.max_per_topic)

    print(f"\nFound {len(works)} unique publications")

    # Extract info from works
    processed_works = [extract_work_info(w) for w in works]

    # Filter out works without titles
    processed_works = [w for w in processed_works if w["title"] != "Untitled"]

    print(f"After title filtering: {len(processed_works)} publications")

    # Apply relevance filtering to remove false positives
    processed_works, filtered_out = filter_relevant_works(processed_works)

    print(f"After relevance filtering: {len(processed_works)} publications")
    if filtered_out:
        print(f"  (Removed {len(filtered_out)} irrelevant papers)")

    # Categorize for reporting and Slack
    categorized = categorize_works(processed_works)

    # Generate output path
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = Path("reports") / f"{to_date_str}_literature_update.md"

    # Generate report
    report = generate_report(processed_works, from_date_str, to_date_str, output_path)

    print(f"\nReport saved to: {output_path}")
    print(f"Total publications: {len(processed_works)}")

    # Send Slack notification if requested
    if args.slack or args.slack_upload:
        notify_slack(
            processed_works,
            categorized,
            from_date_str,
            to_date_str,
            output_path,
            upload_file=args.slack_upload
        )

    return processed_works


if __name__ == "__main__":
    main()
