// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract GhostlyAIFarm is Ownable {
    IERC20 public usdt;  // Bridged USDT on Sonic
    IERC20 public usdc;  // USDC.e on Sonic
    mapping(address => uint256) public balances;

    address public swapX;  // SwapX pool address
    address public silo;   // Silo Finance lending address

    event Deposited(address user, uint256 amount, string token);
    event Farmed(address protocol, uint256 amount);

    constructor(address _usdt, address _usdc, address _swapX, address _silo) Ownable(msg.sender) {
        usdt = IERC20(_usdt);
        usdc = IERC20(_usdc);
        swapX = _swapX;
        silo = _silo;
    }

    function deposit(address token, uint256 amount) external {
        require(token == address(usdt) || token == address(usdc), "Invalid token");
        IERC20(token).transferFrom(msg.sender, address(this), amount);
        balances[msg.sender] += amount;
        emit Deposited(msg.sender, amount, token == address(usdt) ? "USDT" : "USDC");
    }

    function farm(address protocol, uint256 amount) external onlyOwner {
        require(protocol == swapX || protocol == silo, "Invalid protocol");
        usdc.transfer(protocol, amount);
        emit Farmed(protocol, amount);
    }

    function withdraw(address token, uint256 amount) external {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        IERC20(token).transfer(msg.sender, amount);
        balances[msg.sender] -= amount;
    }
}
