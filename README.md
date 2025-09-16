# Dynamic Pricing and Auctions

This project implements dynamic pricing algorithms and an auction bidding agent as part of the **E-commerce in Networks** course (096211) at Technion.  
It consists of two main parts:

## Part 1 — Dynamic Pricing
- **Task:** Set optimal prices for a sequence of arriving customers with unknown valuations.
- **Models:**
  - **PriceSetter1:** Binary search–based strategy for a fixed unknown value.
  - **PriceSetter2:** Optimal price selection given known Beta(α, β) distribution.
  - **PriceSetter3:** Thompson Sampling–style Bayesian updating for unknown Beta parameters.
- **Evaluation:** Algorithms tested against thresholds on simulated rounds, aiming to maximize cumulative revenue.
- **Deliverables:**  
  - `PriceSetter1_214034621_213932338.py`  
  - `PriceSetter2_214034621_213932338.py`  
  - `PriceSetter3_214034621_213932338.py`  
  - `Part1_214034621_213932338.pdf` — explanation of approach

## Part 2 — Auction Bidding Agent
- **Task:** Participate in sequential second-price auctions for insurance contracts, maximizing client utility.
- **Implementation:**  
  - `AuctionClient` class that decides bids based on value, insurance duration, and feedback.
  - Strategy: start below true valuation, adjust bids dynamically depending on outcomes.
  - Ensures positive expected utility and adapts across rounds.
- **Evaluation:** Competes against baseline naive agents in simulation environments.
- **Deliverables:**  
  - `AuctionClient_214034621_213932338.py`  
  - `Part2_214034621_213932338.pdf` — explanation of approach

## Tools
- Python 3.10  
- Libraries: `numpy`, `scipy`, `time`

## How to Run
Run each PriceSetter independently to test dynamic pricing:
```bash
python PriceSetter1_214034621_213932338.py
python PriceSetter2_214034621_213932338.py
python PriceSetter3_214034621_213932338.py
