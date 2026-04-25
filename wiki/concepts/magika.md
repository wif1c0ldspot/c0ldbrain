---
title: Magika
type: concept
tags: [file-type-detection, deep-learning, security, google, ai-powered, content-type-identification]
sources:
- magika-google-2026-04
created: '2026-04-19'
updated: '2026-04-19'
confidence: high
status: current
priority: important
summary: "Google's AI-powered file type detection — ~99% accuracy across 200+ types, used in Gmail/Drive/Safe Browsing/VirusTotal"
---

# Magika

## Summary

Google's AI-powered file type detection tool using deep learning. A custom, highly optimized model (~few MB) enables precise file identification within milliseconds on a single CPU. Trained on ~100M samples across 200+ content types, achieving ~99% average precision and recall.

## Key Features

- **Multiple bindings:** Rust CLI, Python API, JavaScript/TypeScript (npm), GoLang (WIP)
- **200+ content types** (binary and textual formats)
- **~99% accuracy** outperforming existing approaches
- **Production scale:** Processes hundreds of billions of samples weekly at Google

## Use Cases
- **Gmail** — routes files to security scanners
- **Google Drive** — content policy enforcement
- **Safe Browsing** — malware detection pipeline
- **VirusTotal** — file analysis integration

## Source
[[magika-google-2026-04]]

## Related
- [[defense-in-depth-llm]] — security layering
- [[llm-supply-chain-attacks]] — supply chain security
- [[magika]]
