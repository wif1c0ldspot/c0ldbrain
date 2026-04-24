---
title: Polymarket Weather Trading with Hermes Agent — @0xmovez
author: '@0xmovez'
date: 2026-04-19
source: https://x.com/0xmovez/status/2045080054917476451
type: source
tags:
- polymarket
- prediction-markets
- weather-trading
- agent-trading
- hermes-agent
- quantitative-trading
priority: reference
updated: '2026-04-24'
created: '2026-04-24'
confidence: high
status: current
summary: Auto-generated placeholder for Polymarket Weather Trading with Hermes Agent
  — @0xmovez
compiled: true
---

## Summary

Guide for building a self-learning weather trading bot on Polymarket using Hermes Agent. Author claims $100 → $5,000. Based on open-source weatherbot by AlterEgo (github.com/alteregoeth-ai/weatherbot). Covers deployment, wallet setup, API configuration, and continuous trading.

## Reported Success Stories

| Bot | Domain | PnL | Timeframe |
|-----|--------|-----|-----------|
| ColdMath | Weather | $300 → $219K | 3 months |
| Sharky6999 | Crypto | $819K (99.3% win rate) | — |
| RN1 | Sports | $1.2K → $7.3M | — |

## Core Strategy

Polymarket weather markets bet on temperature ranges per city per day. Bot compares professional weather forecasts (ECMWF, HRRR, METAR) to market prices. When forecast probability significantly exceeds market price → buy.

**Example**: Forecast says 78% chance of 46-47°F in Chicago. Market trading at $0.08. Buy.

## Technical Stack

- **Forecasts**: Open-Meteo (ECMWF + HRRR, free), Aviation Weather METAR (free)
- **Market data**: Polymarket Gamma API (free)
- **Resolution**: Visual Crossing API (free key)
- **Agent**: Hermes Agent (memory, skills, 24/7 execution)
- **Wallet**: Polygon network, USDC.e, EIP-1559 transactions

## Key Design Decisions

1. **Airport coordinates, not city center** — 3-8°F difference matters for 1-2°F buckets
2. **Expected Value filter** — only trade with >10% expected edge
3. **Kelly Criterion sizing** — position scaled to edge strength
4. **Stop-loss + trailing stop** — 20% stop, moves to breakeven at +20%
5. **Slippage filter** — skip if spread > $0.03
6. **Self-calibration** — learns forecast accuracy per city over time

## Strategy Validity Assessment

See [[polymarket-weather-trading-strategy]] for full analysis.

**Verdict: Fundamentally sound but overstated returns.**

- Real alpha exists in forecast-vs-market pricing inefficiency
- Mathematical approach (EV, Kelly) is correct
- But astronomical returns ($300 → $219K) likely survivorship bias
- Edge is thin and shrinking as more bots enter
- Requires $50-500 capital, not $100
