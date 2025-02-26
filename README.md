GhostlyAI-SonicFarm
AI-driven stablecoin farming on Sonic Chain

Ghostly AI - Sonic Chain Stablecoin Farming
Ghostly AI optimizes USDT/USDC farming on Sonic Chain, targeting 10%+ APY with 99.9% uptime and 90% gas savings.

Overview
Chain: Sonic (Ethereum L2)
Protocols: SwapX (LPs), Silo Finance (Lending), Rings (scUSD)
Assets: USDT, USDC.e
Structure
contracts/: Solidity contracts for deposit/farming
src/: Python AI logic for yield optimization
tests/: Unit tests
Setup
Deploy GhostlyAIFarm.sol on Sonic (use Hardhat/Foundry).
Install Python deps: pip install -r src/requirements.txt
Update ghostly_ai.py with Sonic RPC and contract details.
Run: python src/ghostly_ai.py
Contracts
GhostlyAIFarm.sol: Main contract for depositing USDT/USDC and farming to SwapX/Silo.
Deploy on Sonic Chain using Hardhat or Foundry.
Dependencies: OpenZeppelin ERC20 and Ownable.
