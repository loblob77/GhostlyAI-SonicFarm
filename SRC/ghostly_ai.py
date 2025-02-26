import requests
from web3 import Web3
import json

# Sonic Chain RPC (placeholder - replace with real Sonic RPC)
SONIC_RPC = "https://sonic-testnet-rpc.example.com"
w3 = Web3(Web3.HTTPProvider(SONIC_RPC))

# Contract details (deployed address TBD)
CONTRACT_ADDRESS = "0xYourContractAddress"
with open("GhostlyAIFarm.abi.json") as f:
    CONTRACT_ABI = json.load(f)
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

# Protocol addresses (placeholders)
SWAPX = "0xSwapXAddress"
SILO = "0xSiloAddress"

def get_yield_data():
    # Fetch APY from SwapX and Silo (mock API calls)
    swapx_apy = float(requests.get("https://swapx-api.example.com/apy").text)  # e.g., 15.0
    silo_apy = float(requests.get("https://silo-api.example.com/apy").text)   # e.g., 10.0
    return {"SwapX": swapx_apy, "Silo": silo_apy}

def optimize_farming(amount=1000 * 10**6):  # 1000 USDC (6 decimals)
    yields = get_yield_data()
    best_protocol = max(yields, key=yields.get)
    protocol_address = SWAPX if best_protocol == "SwapX" else SILO
    
    # Call farm function (requires private key setup)
    tx = contract.functions.farm(protocol_address, amount).build_transaction({
        "from": "0xYourAIWallet",
        "nonce": w3.eth.get_transaction_count("0xYourAIWallet"),
        "gas": 200000,
        "gasPrice": w3.to_wei("0.01", "gwei")
    })
    print(f"Farming {amount/10**6} USDC to {best_protocol}")

if __name__ == "__main__":
    optimize_farming()
