Binance Futures Testnet Trading Bot (Python)

A simplified command-line trading bot built using Python and the official python-binance library.
This bot allows users to place Market, Limit, and Stop-Limit orders on the Binance Futures Testnet (USDT-M) with proper input validation, logging, and error handling.

📌 Features

Place Market Orders

Place Limit Orders

Place Stop-Limit Orders (Bonus)

Supports BUY and SELL order sides

Uses Binance Futures Testnet

Command-Line Interface (CLI) for user input

Structured logging of API requests, responses, and errors

Clean, reusable, and modular code design

🛠️ Tech Stack

Language: Python 3.9+

Library: python-binance

Exchange: Binance Futures Testnet (USDT-M)

Interface: Command Line (CLI)

🔐 Prerequisites

Python 3.9 or higher

Binance Futures Testnet account

API Key & Secret from Binance Testnet

👉 Register here: https://testnet.binancefuture.com

📂 Project Structure
binance-trading-bot/
│
├── bot.py                # Main trading bot script
├── trading_bot.log       # Auto-generated log file
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies

📦 Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/binance-trading-bot.git
cd binance-trading-bot

2️⃣ Create Virtual Environment (Recommended)

Windows

python -m venv venv
venv\Scripts\activate


macOS / Linux

python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install python-binance

🚀 How to Run the Bot
📌 Market Order
python bot.py \
--api-key YOUR_API_KEY \
--api-secret YOUR_API_SECRET \
--symbol BTCUSDT \
--side BUY \
--order-type market \
--quantity 0.001

📌 Limit Order
python bot.py \
--api-key YOUR_API_KEY \
--api-secret YOUR_API_SECRET \
--symbol BTCUSDT \
--side BUY \
--order-type limit \
--quantity 0.001 \
--price 30000

📌 Stop-Limit Order (Bonus)
python bot.py \
--api-key YOUR_API_KEY \
--api-secret YOUR_API_SECRET \
--symbol BTCUSDT \
--side SELL \
--order-type stop-limit \
--quantity 0.001 \
--price 29500 \
--stop-price 29600

📤 Sample Output
Order Placed Successfully
-------------------------
Order ID : 123456789
Symbol   : BTCUSDT
Side     : BUY
Type     : LIMIT
Quantity : 0.001
Price    : 30000
Status   : NEW

🧾 Logging

All API requests, responses, and errors are logged automatically to:

trading_bot.log# tread_bot
