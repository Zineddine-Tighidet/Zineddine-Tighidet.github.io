#!/usr/bin/env python3
import json
import re
import sys
from urllib.request import Request, urlopen

PROFILE_URL = "https://r.jina.ai/http://scholar.google.com/citations?user=jgle1SAAAAAJ&hl=en&view_op=list_works&sortby=pubdate"
HEADERS = {"User-Agent": "Mozilla/5.0"}


def fetch_text(url: str) -> str:
    req = Request(url, headers=HEADERS)
    with urlopen(req, timeout=20) as resp:
        return resp.read().decode("utf-8", errors="ignore")


def parse_publications(text: str):
    # Detect bot-protection pages and bail out
    lower = text.lower()
    if "automated queries" in lower or "protect our users" in lower or "unusual traffic" in lower:
        return []

    lines = [l.strip() for l in text.splitlines() if l.strip()]
    pubs = []
    year_re = re.compile(r"\b(20\d{2}|19\d{2})\b")
    i = 0
    while i < len(lines):
        line = lines[i]
        if len(line) > 20 and not line.lower().startswith(("my profile", "articles", "cited by", "co-authors", "public access")):
            title = line
            authors = ""
            venue = ""
            year = None
            for j in range(1, 4):
                if i + j >= len(lines):
                    break
                meta = lines[i + j]
                if not year and year_re.search(meta):
                    year = year_re.search(meta).group(1)
                if ("," in meta and len(meta) < 200) or (" - " in meta and len(meta) < 200):
                    if not authors:
                        authors = meta
                    elif not venue and " - " in meta:
                        venue = meta
            pubs.append({
                "title": title,
                "authors": authors,
                "venue": venue,
                "year": year
            })
            i += 3
        else:
            i += 1
    seen = set()
    cleaned = []
    for p in pubs:
        t = p["title"].lower()
        if t in seen:
            continue
        seen.add(t)
        if len(p["title"]) < 25:
            continue
        if p["title"].startswith("URL Source:"):
            continue
        cleaned.append(p)
    return cleaned[:8]


def main():
    try:
        text = fetch_text(PROFILE_URL)
    except Exception as e:
        print(f"Error fetching profile: {e}", file=sys.stderr)
        sys.exit(1)
    pubs = parse_publications(text)
    out = {
        "source": "google_scholar",
        "profile": "https://scholar.google.com/citations?user=jgle1SAAAAAJ&hl=en",
        "count": len(pubs),
        "items": pubs
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main() 