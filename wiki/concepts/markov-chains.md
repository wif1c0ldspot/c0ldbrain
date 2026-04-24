---
title: Markov Chains in Trading
type: concept
tags: [markov-chains, quant-trading, prediction-markets, polymarket, kelly-criterion, state-machine]
sources:
- 0xricker-markov-chain-quant-trading-2026-04
created: '2026-04-19'
updated: '2026-04-19'
confidence: high
status: current
priority: important
summary: "Markov chain models for quantitative trading — state machines, transition matrices, Kelly criterion bet sizing for prediction markets"
---

# Markov Chains in Trading

## Summary

Markov chain models applied to quantitative trading, particularly prediction markets like Polymarket. Models discrete state transitions (bullish/bearish/neutral) with probabilistic patterns, enabling state-dependent strategy selection and Kelly criterion optimal bet sizing.

## Key Concepts

### State Machine Construction
1. Define discrete states (bullish, bearish, neutral, or yes/no/uncertain)
2. Build transition matrix from historical data
3. Estimate transition probabilities via maximum likelihood
4. Apply state-dependent strategies

### Kelly Criterion for Bet Sizing
- Optimal fraction to wager given edge and odds
- `f* = (bp - q) / b` where b = odds, p = win prob, q = loss prob
- Critical for prediction markets where odds shift with state transitions

### Application to Polymarket
- Binary outcome markets map naturally to Markov states
- News/sentiment drives state transitions
- Enables systematic edge extraction vs. emotional trading

## Source
[[0xricker-markov-chain-quant-trading-2026-04]]

## Related
- [[quantitative-trading]] — broader quant trading concepts
- [[polymarket]] — prediction market platform
