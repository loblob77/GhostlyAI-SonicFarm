# Ghostly AI - Sonic Chain Stablecoin Farming

Ghostly AI optimizes USDT/USDC farming on Sonic Chain, targeting 10%+ APY with 99.9% uptime and 90% gas savings.

## Overview
- **Chain**: Sonic (Ethereum L2)
- **Protocols**: SwapX (LPs), Silo Finance (Lending), Rings (scUSD)
- **Assets**: USDT, USDC.e

## Structure
- `contracts/`: Solidity contracts for deposit/farming
- `src/`: Python AI logic for yield optimization
- `tests/`: Unit tests

## Setup
1. Deploy `GhostlyAIFarm.sol` on Sonic (use Hardhat/Foundry).
2. Install Python deps: `pip install -r src/requirements.txt`
3. Update `ghostly_ai.py` with Sonic RPC and contract details.
4. Run: `python src/ghostly_ai.py`

