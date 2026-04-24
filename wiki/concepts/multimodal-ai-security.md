---
confidence: medium
created: '2026-04-16'
priority: critical
status: current
summary: Key Facts
tags:
- ai-security
- concept
title: Multimodal Ai Security
type: concept
updated: '2026-04-18'
---



## Key Facts
- [[defense-in-depth-llm]] — Multi-modal systems expand the attack surface beyond text
- [[llm-vulnerability-scanners]] — Multi-modal scanners must handle images, audio, video
- Visual/auditory injection attacks can bypass text-only safety filters

## Multi-Modal Attack Vectors

| Modality | Attack | Example | Impact |
|----------|--------|---------|--------|
| Image | Visual prompt injection | Hidden text in images | Bypasses text filters |
| Audio | Adversarial audio | Inaudible voice commands | Unauthorized actions |
| Video | Frame-by-frame injection | Malicious frames in video stream | Temporal attack |
| Multi-modal | Cross-modal transfer | Image text reads as injection | Evades single-modality scanners |
| Spatial | OCR manipulation | QR codes, styled text | Bypasses vision models |

## Security Challenges
- **Cross-modal attacks**: Injection in one modality affects processing in another
- **Scanner gaps**: [[llm-vulnerability-scanners]] may not cover all modalities equally
- **Model alignment**: Safety training often lags behind text-only capabilities
- **Runtime complexity**: Each modality adds its own [[defense-in-depth-llm]] requirements

## Defense Strategies
- Multi-modal input sanitization (image preprocessing, audio filtering)
- Cross-modal consistency checking
- Modality-specific [[defense-in-depth-llm]] layers
- Extended [[continuous-red-teaming]] for non-text modalities
- Multi-modal [[llm-vulnerability-scanners]] deployment

## Related Concepts


[[prompt-injection-comprehensive-2026]], [[defense-in-depth-llm]], [[rag-security]], [[llm-vulnerability-scanners]], [[llm-supply-chain-attacks]]
