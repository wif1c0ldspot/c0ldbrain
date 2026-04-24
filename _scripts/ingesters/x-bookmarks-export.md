# X Bookmarks Exporter

Export all X bookmarks into the wiki's raw/social/ folder for ingestion.

## Overview

X doesn't have a public API for bookmarks. This script authenticates via your browser's local storage cookies and extracts all bookmark data. Runs locally on your machine.

## Prerequisites

- Node.js installed locally
- Your X browser session (Chrome or similar)
- The `twitter-bookmarks` npm package

## Setup

```bash
npm install -g twitter-cli
# OR use the Python approach below
pip install twikit
```

## Method 1: Python (twikit)

```python
import asyncio
import json
from twikit import Client
import os

# Get cookies from browser: install EditThisCookie extension, export as JSON
# Or use: python -c "import twikit; client = Client('en-US'); asyncio.run(client.login(...))"

async def export_bookmarks():
    client = Client('en-US')
    await client.login(
        auth_info_1='your_username',
        auth_info_2='your_email', 
        password='your_password'
    )
    
    bookmarks = []
    async for tweet in client.get_bookmarks():
        bookmarks.append({
            'text': tweet.text,
            'author': tweet.user.name,
            'author_screen_name': tweet.user.screen_name,
            'created_at': str(tweet.created_at),
            'url': f'https://x.com/{tweet.user.screen_name}/status/{tweet.id}',
            'bookmark_date': str(tweet.bookmarked_at) if hasattr(tweet, 'bookmarked_at') else None
        })
    
    return bookmarks

# Run and save
asyncio.run(export_bookmarks())
```

## Method 2: Manual Browser Extraction (No API)

1. Open https://x.com/i/bookmarks in your browser
2. Open DevTools Console (F12)
3. Run this script to extract visible bookmarks:

```javascript
// Scroll through all bookmarks first, then run:
const tweets = document.querySelectorAll('article[data-testid="tweet"]');
const data = [];
tweets.forEach(t => {
  const link = t.querySelector('a[href*="/status/"]');
  const text = t.querySelector('[data-testid="tweetText"]')?.textContent;
  const author = t.querySelector('[data-testid="User-Name"]')?.textContent;
  if (link && text) {
    data.push({
      url: 'https://x.com' + link.getAttribute('href').split('?')[0],
      text: text.substring(0, 280),
      author: author?.split('·')[0]?.trim(),
      date: author?.split('·')[1]?.trim()
    });
  }
});
console.log(JSON.stringify(data, null, 2));
```

4. Copy the JSON output
5. Paste it here and say "ingest these bookmarks"

## Output Format

The script produces a JSON dump. Drop it into `raw/social/x-bookmarks-YYYY-MM-DD.json`.

```json
[
  {
    "url": "https://x.com/karpathy/status/2039805659525644595",
    "text": "LLM Knowledge Bases: Something I'm finding very useful...",
    "author": "Andrej Karpathy",
    "date": "Apr 2, 2026"
  }
]
```

## After Export

1. Copy the JSON to `/Volumes/obsidian/C0ldbrain/raw/social/x-bookmarks-YYYY-MM-DD.json`
2. Add frontmatter wrapper if the tool doesn't:
   ```yaml
   ---
   source: x-bookmarks-export
   ingested_at: YYYY-MM-DD
   type: social
   status: uncompiled
   ---
   ```
3. Say to the LLM: "compile the wiki"

## Alternative: Third-party Exporter

- **Twitter Bookmarks Exporter** (Chrome extension): Exports all bookmarks as CSV/JSON
- **x-bookmarks-cli** (npm): CLI tool for bookmark export
- **twurl** (Ruby): Twitter API CLI with bookmark support

## Rate Limits

- X API has rate limits for bookmark access
- Browser extraction may hit scroll limits
- Run export in batches if you have 1000+ bookmarks
