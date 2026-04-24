---
compiled: 2026-04-15
confidence: high
created: '2026-04-16'
priority: 2
source_url: https://github.com/microsoft/markitdown
stars: 109k
status: current
summary: Microsoft's file-to-Markdown converter. 109k stars. MCP server available
  for agent integration. Converts any file format to Markdown for LLM consumption.
tags:
- mcp-protocol
- knowledge-management
- developer-tools
- open-source
title: MarkItDown — Microsoft File-to-Markdown Converter
type: source
updated: '2026-04-18'
---


# MarkItDown — Microsoft File-to-Markdown Converter

## Key Insights

- Microsoft's massively popular file-to-Markdown converter (109k stars)
- Converts any document format to clean Markdown optimized for LLM consumption
- MCP server available for direct integration with AI agents like Claude Code
- Critical infrastructure for the LLM knowledge management ecosystem

## Technical Details

### Supported Formats
- PDF, DOCX, PPTX, XLSX
- Images (with OCR), audio (with transcription)
- HTML, EPUB, and web pages
- ZIP archives (processes contained files)

### MCP Server Integration
- Official MCP server for agent tool connectivity
- Agents can convert files on-demand without leaving their workflow
- Compatible with Claude Code, Cursor, and other MCP-enabled agents
- Streaming support for large files

### Architecture
- Python library with CLI and API
- Pluggable converter backends per format
- Image description via vision models
- Audio transcription via Whisper integration

### Usage
- CLI: `markitdown document.pdf > output.md`
- Python API: `MarkItDown().convert("path/to/file")`
- MCP: connect agent to markitdown MCP server

## Related Concepts

- [[mcp-protocol]] — MCP server for agent integration
- [[llm-knowledge-bases]] — key tool for ingesting documents into knowledge bases
- [[knowledge-management]] — file conversion enables knowledge extraction
- [[open-source-ai-infra]] — major Microsoft open-source contribution
