---
title: Magika Google 2026 04
date: 2026-04-17
type: source
compiled: true
tags:
- source
- developer-tools
- google
- open-source
priority: reference
updated: '2026-04-24'
created: '2026-04-24'
confidence: high
status: current
summary: Auto-generated placeholder for Magika Google 2026 04
source_url: https://github.com/google/magika
---

     1|---
     2|title: Magika
     3|type: source
     4|tags:
     5|- file-type-detection
     6|- deep-learning
     7|- security
     8|- google
     9|- ai-powered
    10|- content-type-identification
    11|source_url: https://github.com/google/magika
    12|sources: []
    13|created: '2026-04-18'
    14|updated: '2026-04-18'
    15|confidence: high
    16|status: current
    17|agents:
    18|- hermes
    19|priority: high
    20|summary: "Google's AI-powered file type detection tool using deep learning. ~99% accuracy across 200+ content types, used in Gmail, Drive, Safe Browsing, VirusTotal. Rust CLI + Python/JS/Go bindings."
    21|---
    22|
    23|# Magika - AI-Powered File Type Detection
    24|
    25|**Author:** Google  
    26|**Version:** 1.0.3-dev (Rust CLI)  
    27|**License:** Apache 2.0  
    28|**Source:** https://github.com/google/magika  
    29|**Website:** https://securityresearch.google/magika  
    30|**Research Paper:** Published at IEEE/ACM ICSE 2025  
    31|**Web Demo:** https://securityresearch.google/magika/demo/magika-demo/
    32|
    33|## Summary
    34|
    35|Magika is a novel AI-powered file type detection tool using deep learning. Under the hood, it employs a custom, highly optimized model (~few MB) that enables precise file identification within milliseconds on a single CPU. Trained on ~100M samples across 200+ content types, achieving ~99% average precision and recall.
    36|
    37|**Production usage:** Used at Google scale to route Gmail, Drive, and Safe Browsing files to proper security and content policy scanners, processing hundreds of billions of samples weekly. Integrated with VirusTotal and abuse.ch.
    38|
    39|## Key Details
    40|
    41|### Highlights
    42|
    43|- **Multiple bindings:** Rust CLI, Python API, JavaScript/TypeScript (npm), GoLang (WIP)
    44|- **200+ content types** (binary and textual formats)
    45|- **~99% accuracy** on test set, outperforming existing approaches (especially textual types)
    46|- **~5ms inference** per file (after model load, single CPU)
    47|- **Scale:** Handle thousands of files simultaneously; `-r` for recursive directory scanning
    48|- **Near-constant inference time** regardless of file size (uses limited subset of content)
    49|- **Per-content-type thresholds:** Returns generic labels ("Generic text document") when prediction falls below confidence
    50|- **Prediction modes:** `high-confidence`, `medium-confidence`, `best-guess`
    51|
    52|### Installation
    53|
    54|**Rust CLI (recommended):**
    55|```bash
    56|pipx install magika
    57|# or
    58|brew install magika
    59|# or
    60|curl -LsSf https://securityresearch.google/magika/install.sh | sh
    61|# or
    62|cargo install --locked magika-cli
    63|```
    64|
    65|**Python:**
    66|```bash
    67|pip install magika
    68|```
    69|
    70|**JavaScript:**
    71|```bash
    72|npm install magika
    73|```
    74|
    75|### CLI Examples
    76|
    77|```bash
    78|# Recursive scan with type display
    79|magika -r tests_data/basic/*
    80|
    81|# JSON output
    82|magika ./tests_data/basic/python/code.py --json
    83|
    84|# Pipe input
    85|cat file.ini | magika -
    86|
    87|# MIME type output
    88|magika -i file.py
    89|
    90|# Custom format
    91|magika --format "%p: %d (score: %s)" file.py
    92|```
    93|
    94|### Python API
    95|
    96|```python
    97|from magika import Magika
    98|m = Magika()
    99|
   100|# From bytes
   101|res = m.identify_bytes(b'function log(msg) {console.log(msg);}')
   102|print(res.output.label)  # javascript
   103|
   104|# From file path
   105|res = m.identify_path('./file.ini')
   106|print(res.output.label)  # ini
   107|
   108|# From stream
   109|with open('./file.ini', 'rb') as f:
   110|    res = m.identify_stream(f)
   111|print(res.output.label)  # ini
   112|```
   113|
   114|### CLI Options
   115|
   116|| Flag | Description |
   117||------|-------------|
   118|| `-r, --recursive` | Scan directories recursively |
   119|| `--json` | JSON output format |
   120|| `--jsonl` | JSONL output format |
   121|| `-i, --mime-type` | Output MIME type instead of description |
   122|| `-l, --label` | Output simple label |
   123|| `-s, --output-score` | Include prediction score |
   124|| `--format <CUSTOM>` | Custom output format with placeholders (%p, %l, %d, %g, %m, %e, %s, %S) |
   125|
   126|### Architecture
   127|
   128|- Custom highly optimized deep learning model (~few MB)
   129|- Uses limited subset of file content for inference (constant time regardless of file size)
   130|- Per-content-type threshold system for confidence-based output
   131|- One-off model load overhead, then ~5ms per file inference
   132|
   133|### Integrations
   134|
   135|- **Google:** Gmail, Drive, Safe Browsing (hundreds billions weekly)
   136|- **VirusTotal:** File type detection integration
   137|- **abuse.ch:** Bazaar integration
   138|- **Web Demo:** Browser-based local inference (WASM)
   139|
   140|### Documentation
   141|
   142|| Doc | Coverage |
   143||-----|----------|
   144|| [Website](https://securityresearch.google/magika) | Core concepts, CLI/bindings docs |
   145|| [Quick Start](https://securityresearch.google/magika/core-concepts/) | How Magika works, models, prediction modes |
   146|| [Content Types](./assets/models/standard_v3_3/README.md) | Full list of 200+ supported types |
   147|| [Research Paper](https://securityresearch.google/magika/additional-resources/research-papers-and-citation/) | IEEE/ACM ICSE 2025 publication |
   148|
   149|## Notes
   150|
   151|- **Security relevant:** File type detection is critical for security scanning pipelines
   152|- **Complements Clearwing:** Clearwing analyzes file content, Magika identifies file types — could be used together for file inspection workflows
   153|- **WASM demo:** Runs entirely in browser, no server needed
   154|- **Production-proven:** Used at Google scale across multiple products
   155|- CONSIDER: Integration for security research or file inspection pipelines
   156|
   157|## Project Structure
   158|
   159|```
   160|magika/
   161|├── python/          # Python package (pip install magika)
   162|├── rust/            # Rust CLI + bindings
   163|├── js/              # JavaScript/TypeScript npm package
   164|├── go/              # GoLang bindings (WIP)
   165|├── assets/          # Models, screenshots, content type lists
   166|├── website/         # Magika website
   167|├── website-ng/      # Updated website
   168|├── tests_data/      # Test files for 200+ content types
   169|└── Dockerfile       # Container support
   170|```
   171|