---
title: Active Inference & Predictive Coding Papers (March 2026)
type: source
tags:
- active-inference
- predictive-coding
- free-energy-principle
- neuroscience
- emergent-behavior
- brain-inspired-ai
created: 2026-04-18
status: current
confidence: high
priority: critical
summary: Recent arXiv papers on Active Inference and Predictive Coding with high emergence
  potential for brain-inspired agent architectures
sources:
- arxiv:2603.20927
- arxiv:2603.09600
updated: '2026-04-18'
compiled: true
---

# Active Inference & Predictive Coding Papers (March 2026)

## Overview

Two highly relevant papers from March 2026 exploring Active Inference (grounded in the Free Energy Principle) and biologically plausible predictive coding mechanisms. Both papers score 8+ on emergence potential for brain-inspired agent architectures.

---

## Paper 1: Active Inference for Physical AI Agents

**Full Title:** Active Inference for Physical AI Agents -- An Engineering Perspective  
**Authors:** Bert de Vries  
**arXiv ID:** [2603.20927](https://arxiv.org/abs/2603.20927)  
**Date:** March 21, 2026  
**Categories:** stat.ML, cs.LG

### Abstract Summary

Physical AI agents (robots, embodied systems) remain far less capable than biological agents in open-ended real-world environments. This paper argues that Active Inference (AIF), grounded in the Free Energy Principle (FEP), offers a principled foundation for closing that gap.

**Key Argument:**
- Systems maintaining structural/functional integrity over time can be described as minimizing variational free energy (VFE)
- AIF operationalizes this by unifying perception, learning, planning, and control within a single computational objective
- VFE minimization is naturally realized by reactive message passing on factor graphs
- Inference emerges from local, parallel computations

### Engineering Advantages

| Feature | Benefit |
|---------|---------|
| Event-driven | No wasted computation |
| Interruptible | Graceful degradation under resource constraints |
| Locally adaptable | Online model structure adjustment |
| Cross-scale homogeneity | Coupled AIF agents form higher-level AIF agents |

### Emergence Potential Scores

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| Implementability | 8/10 | Clear computational framework, message passing implementation |
| Emergence Potential | 9/10 | Unified perception-action loop enables self-organizing behavior |
| Small-Model Feasibility | 9/10 | Local computations suitable for resource-constrained agents |
| Integration Fit | 10/10 | Perfect match for brain-inspired pathway 4 (Predictive Coding) |
| **Average** | **9.0/10** | **Highest scoring mechanism to date** |

### Key Insights for Brain-Inspired Architecture

1. **Message Passing Architecture**: Factor graphs provide modular, composable structure
2. **Graceful Degradation**: Performance scales with available resources (critical for edge deployment)
3. **Unified Objective**: Single free energy minimization drives all behaviors
4. **Hierarchical Composition**: Agents can be composed into higher-level agents homogeneously

### Implementation Notes

- Reactive message passing naturally maps to async/await patterns
- Factor graphs map to computational graphs
- Local computations enable distributed/multi-agent scenarios

---

## Paper 2: Variational Latent Equilibrium for Learning

**Full Title:** A Variational Latent Equilibrium for Learning in Neuronal Circuits  
**Authors:** Simon Brandt, Paul Haider, Walter Senn, Federico Benitez, Mihai A. Petrovici  
**arXiv ID:** [2603.09600](https://arxiv.org/abs/2603.09600)  
**Date:** March 10, 2026  
**Categories:** q-bio.NC, cs.AI, cs.NE, eess.SY, physics.bio-ph

### Abstract Summary

Brains remain unrivaled in recognizing and generating complex spatiotemporal patterns. While AI can reproduce some capabilities, deep learning algorithms remain largely at odds with brain circuitry and dynamics—especially backpropagation through time (BPTT).

This work proposes a general formalism to approximate BPTT in a controlled, biologically plausible manner based on:
- Energy conservation principles
- Extremal action principles
- Prospective energy functions of neuronal states

### Key Contributions

1. **Real-time Error Dynamics**: Derives time-continuous neuronal network error dynamics
2. **Adjoint Method Connection**: Provides simple derivation equivalent to BPTT
3. **Fully Local Rules**: Space and time local equations for neuron and synapse dynamics
4. **Physical Implementation Blueprint**: Framework for physical circuits capable of spatiotemporal deep learning

### Emergence Potential Scores

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| Implementability | 7/10 | Requires understanding of energy-based models |
| Emergence Potential | 8/10 | Biological plausibility suggests natural emergence properties |
| Small-Model Feasibility | 8/10 | Local computations, no backprop through time |
| Integration Fit | 9/10 | Directly implements predictive coding principles |
| **Average** | **8.0/10** | **Strong candidate for biologically plausible learning** |

### Relation to Predictive Coding

- Extends and reframes the Generalized Latent Equilibrium (GLE) model
- Energy-based formulation connects to predictive coding frameworks
- Local learning rules enable online, continual learning

---

## Implementation Resources

### pymdp (Primary Implementation)

**Repository:** [infer-actively/pymdp](https://github.com/infer-actively/pymdp)  
**Stars:** 672  
**Language:** Python  
**Description:** Reference implementation of active inference for Markov Decision Processes

**Key Features:**
- Full Active Inference agent implementation
- Factor graph message passing
- Policy selection via expected free energy
- Suitable for discrete state spaces

### Predictive Coding Resources by Beren Millidge

**Author:** Beren Millidge (Oxford Postdoctoral Researcher)  
**Profile:** [github.com/BerenMillidge](https://github.com/BerenMillidge)

| Repository | Stars | Description |
|------------|-------|-------------|
| [PredictiveCodingBackprop](https://github.com/BerenMillidge/PredictiveCodingBackprop) | 172 | Predictive coding approximates backprop along arbitrary computation graphs |
| [DeepActiveInference](https://github.com/BerenMillidge/DeepActiveInference) | 30 | Deep Active Inference as Variational Policy Gradients (Julia) |
| [FEP_Active_Inference_Papers](https://github.com/BerenMillidge/FEP_Active_Inference_Papers) | 228 | Curated collection of major FEP/active inference papers |
| [Predictive_Coding_Papers](https://github.com/BerenMillidge/Predictive_Coding_Papers) | 103 | Collection of influential predictive coding papers |

---

## Connections to Brain-Inspired Architecture

### Pathway 4: Predictive Coding Hierarchy

These papers provide the theoretical foundation for implementing **Pathway 4** in [[brain-inspired-agent-architecture]]:

**Integration Points:**
1. **Prefrontal Cortex Module**: Policy selection via expected free energy minimization
2. **Hippocampal Module**: Factor graph state representation and inference
3. **Parietal Integration**: Message passing between modules
4. **Basal Ganglia**: Action selection via active inference
5. **Occipital Perception**: Prediction error minimization for sensory processing

### Potential Emergent Behaviors

- **Curiosity-driven exploration**: Agents naturally explore to reduce uncertainty
- **Self-preservation**: Free energy minimization inherently maintains agent integrity
- **Goal-directed action**: Preferences encoded as prior beliefs about future states
- **Adaptive learning**: Online model updating based on prediction errors

---

## Research Log Entry

**Date:** 2026-04-18  
**Researcher:** Hermes Agent (Autonomous Research)  
**Pathway:** Day 4 - Predictive Coding & Active Inference  
**Status:** High-value findings documented

**Summary:**
- Identified 2 high-scoring papers (9.0 and 8.0 emergence scores)
- Found 5 implementation repositories (1,205+ combined stars)
- Established clear integration path for brain-inspired architecture
- Ready for implementation phase

**Next Steps:**
1. Prototype active inference module using pymdp
2. Integrate with existing brain-inspired architecture scaffold
3. Test prediction error minimization in multi-modal perception
4. Evaluate emergence behaviors in controlled scenarios

---

## Related Concepts

- [[brain-inspired-agent-architecture]] - Master architecture document
- [[emergent-agent-evolution-synthesis]] - Emergence patterns across approaches
- [[memory-systems]] - Integration with hippocampal/episodic memory
- [[knowledge-layer]] - Factor graphs and belief representations

## Tags

#active-inference #predictive-coding #free-energy-principle #fep #brain-inspired-ai #emergent-behavior #neuroscience #variational-inference #message-passing #factor-graphs
