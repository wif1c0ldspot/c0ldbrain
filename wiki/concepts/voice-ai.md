---
title: Voice AI & Speech Systems
type: concept
tags: [voice-ai, ml-models, multimodal, open-source]
sources: [vibevoice-microsoft-2026-04]
created: '2026-04-15'
updated: '2026-04-15'
confidence: high
status: current
priority: important
summary: Voice AI systems — ASR, TTS, and real-time conversational models. Microsoft VibeVoice (39.6k stars) leads with ASR-7B, TTS-1.5B, and Realtime-0.5B.
---

# Voice AI & Speech Systems

## Summary

The ecosystem of voice AI models and frameworks covering automatic speech recognition (ASR), text-to-speech (TTS), and real-time conversational voice. Major open-source releases in 2026 have made production voice AI accessible.

## Key Models

### VibeVoice (Microsoft, 39.6k stars)
- **ASR-7B**: 7B parameter speech recognition model
- **TTS-1.5B**: 1.5B parameter text-to-speech synthesis
- **Realtime-0.5B**: 0.5B parameter real-time voice model
- ICLR 2026 Oral paper — top academic validation
- Full pipeline: listen → understand → respond → speak

### PersonaPlex 7B (NVIDIA)
- Real-time conversational model
- Simultaneous listening and speaking
- Handles natural interruptions and overlaps
- 100% open-source

## Architecture Patterns

| Component | Purpose | Typical Size |
|-----------|---------|-------------|
| ASR | Speech → Text | 1-7B params |
| TTS | Text → Speech | 1-2B params |
| Realtime | Low-latency voice | 0.5-2B params |
| Voice Clone | Adapt to speaker | 0.1-1B params |

## Applications

- Voice agents and assistants
- Real-time translation
- Meeting transcription and summarization
- Accessibility tools
- Conversational AI for customer service

## Related Concepts

- [[open-source-ai-infra]] — major open-source voice releases
- [[multimodal-ai-security]] — voice AI security considerations

## Sources

- [[vibevoice-microsoft-2026-04]]
