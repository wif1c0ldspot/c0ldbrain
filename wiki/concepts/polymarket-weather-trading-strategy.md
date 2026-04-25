---
title: "Polymarket Weather Trading Strategy"
type: concept
tags: [prediction-markets, quantitative-trading, weather-trading, polymarket, ev-kelly, alpha-factors]
created: '2026-04-19'
updated: '2026-04-19'
confidence: medium
status: current
priority: important
summary: "Strategy to exploit forecast-vs-market pricing inefficiencies in Polymarket temperature markets. Uses EV filtering, Kelly sizing, airport coordinates, self-calibration. Real alpha but overstated returns and shrinking edge."
sources:
- polymarket-weather-trading-0xmovez-2026-04
---

# Polymarket Weather Trading Strategy

## Summary

Exploit pricing inefficiencies in Polymarket temperature-range markets by comparing professional weather forecasts to market prices. Use Expected Value filtering and Kelly Criterion for sizing. Real alpha exists but return claims are likely survivorship bias.

## Strategy Mechanics

### Market Structure

Polymarket runs binary markets: "Will the highest temperature in [City] be between X-Y°F on [Date]?"

Each market has a Yes/No price. Price = implied probability. Buy Yes if your forecast probability > market price.

### Signal Generation

1. Fetch forecasts from 3 sources: ECMWF (global model), HRRR/GFS (US hourly), METAR (real-time airport observations)
2. Map forecast to temperature bucket probability
3. Compare to Polymarket market price
4. Calculate Expected Value = (win_prob × win_payoff) - (lose_prob × lose_cost)
5. Only trade if EV > 10%

### Position Sizing

Kelly Criterion: `f = (p × b - q) / b`
- p = your probability estimate
- q = 1 - p
- b = net odds (1/price - 1)
- f = fraction of bankroll to bet

Use fractional Kelly (25%) for safety margin.

### Key Edge: Airport Coordinates

Polymarket resolves on specific airport stations, not city centers:
- NYC = LaGuardia (KLGA), not Manhattan
- Chicago = O'Hare (KORD), not downtown
- Dallas = Love Field (KDAL), not DFW

Difference: 3-8°F. On 1-2°F market buckets, this is the entire edge.

## VERDICT: Is It Valid?

### ✅ What's Real

1. **Forecast edge exists.** Professional weather models (ECMWF, HRRR) are genuinely superior to crowd wisdom for short-range temperature prediction. This is real alpha.

2. **Airport coordinate advantage.** Using correct resolution station vs city center creates a genuine informational edge. Most participants miss this.

3. **Mathematical framework is correct.** EV filtering, Kelly sizing, slippage control — these are textbook quant trading principles applied correctly.

4. **Risk management is sensible.** 20% stop-loss, trailing stops, max bet limits, min volume filters — all appropriate for prediction market trading.

5. **Self-calibration has merit.** Tracking forecast accuracy per city and adjusting confidence over time is a solid approach.

### ⚠️ What's Overstated

1. **Return claims are survivorship bias.**
   - ColdMath: $300 → $219K = 72,900% in 3 months
   - RN1: $1.2K → $7.3M = 608,233%
   - These are lottery-level returns. For every ColdMath, dozens of bots blew up.
   - The $100 → $5,000 claim is more modest but still unlikely to be sustainable.

2. **Edge is thin and shrinking.**
   - Weather markets are low-volume ($500-$2,000 typical)
   - Slippage eats into returns at scale
   - As more bots enter, mispricings get arbitraged faster
   - First-mover advantage from 6-12 months ago is mostly gone

3. **Minimum EV of 10% is aggressive.**
   - Real edge in efficient markets is typically 2-5%
   - 10%+ opportunities are rare and fleeting
   - May indicate overfitting to historical data

4. **Liquidity constraint is severe.**
   - Kelly suggests size X, but market can only absorb Y << X
   - You're capped by orderbook depth, not edge
   - Moving prices against yourself is a real risk

5. **Tail risk is unpriced.**
   - Weather models fail in transition seasons
   - Sudden cold snaps or heat waves cause resolution surprises
   - Stop-losses may not fill in thin markets

### 🔴 Real Risks

1. **Market delisting.** Polymarket may remove low-volume weather markets
2. **API dependency.** Open-Meteo, METAR, Visual Crossing all single points of failure
3. **Gas cost erosion.** Polygon transactions eat into small positions
4. **Wallet security.** Private keys on a VPS = attack surface
5. **Regulatory.** Prediction market legality varies by jurisdiction

## Realistic Expectations

| Metric | Optimistic | Realistic | Pessimistic |
|--------|-----------|-----------|-------------|
| Annual return | 200-500% | 50-150% | -50% to 0% |
| Win rate | 65-70% | 55-60% | 45-50% |
| Sharpe ratio | 3-5 | 1-2 | <1 |
| Max drawdown | 20% | 40% | 80%+ |

**Realistic: 50-150% annual with proper risk management.** Not 72,900%.

## Optimization Opportunities

1. **Multiple forecast ensembles** — combine ECMWF, GFS, UKMET, NAM for better calibration
2. **Bayesian updating** — as resolution day approaches, weight observations more
3. **Cross-city correlation** — weather patterns affect multiple cities simultaneously
4. **Time-of-day edge** — scan immediately after model updates (00z, 06z, 12z, 18z runs)
5. **Market microstructure** — track order flow, not just price, for informed trading

## Implementation

### Stack
- Open-Meteo API (ECMWF + HRRR forecasts, free)
- Aviation Weather METAR (real-time airport obs, free)
- Polymarket Gamma API (market data, free)
- Visual Crossing (historical temps for backtest, free tier)
- web3.py (Polygon transactions)
- py-clob-client (Polymarket CLOB trading)

### File Structure
```
weatherbot/
├── weatherbet.py      # Main bot
├── config.json        # Parameters
├── .env               # Wallet keys
└── data/markets/      # Historical data per market
```

## Related
- [[polymarket-weather-hermes-agent-0xmovez-2026-04]] Concepts
- [[polymarket-weather-trading-0xmovez-2026-04]]

- [[quantitative-trading]] — broader quant trading methodology
- [[neutral-market-pairs-trading]] — market-neutral strategies
- [[ev-kelly-position-sizing]] — mathematical position sizing
- [[polymarket]] — prediction market platform
