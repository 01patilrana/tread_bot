import argparse
import logging
import sys
from binance import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException


class BasicBot:
    def __init__(self, api_key: str, api_secret: str, testnet: bool = True):
        self.client = Client(api_key, api_secret)

        if testnet:
            self.client.FUTURES_URL = "https://testnet.binancefuture.com"

        self.logger = self._setup_logging()

    def _setup_logging(self):
        logger = logging.getLogger("TradingBot")
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        file_handler = logging.FileHandler("trading_bot.log")
        console_handler = logging.StreamHandler()

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        if not logger.handlers:
            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        return logger

    def place_market_order(self, symbol, side, quantity):
        try:
            self.logger.info(
                f"Market Order Request | {symbol} | {side} | Qty: {quantity}"
            )

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity,
            )

            self.logger.info(f"Market Order Response: {order}")
            return order

        except (BinanceAPIException, BinanceRequestException) as e:
            self.logger.error(f"Market Order Error: {e}")
            raise

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            self.logger.info(
                f"Limit Order Request | {symbol} | {side} | Qty: {quantity} | Price: {price}"
            )

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC",
            )

            self.logger.info(f"Limit Order Response: {order}")
            return order

        except (BinanceAPIException, BinanceRequestException) as e:
            self.logger.error(f"Limit Order Error: {e}")
            raise

    def place_stop_limit_order(self, symbol, side, quantity, price, stop_price):
        try:
            self.logger.info(
                f"Stop-Limit Order Request | {symbol} | {side} | Qty: {quantity} | "
                f"Price: {price} | Stop: {stop_price}"
            )

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP",
                quantity=quantity,
                price=price,
                stopPrice=stop_price,
                timeInForce="GTC",
            )

            self.logger.info(f"Stop-Limit Order Response: {order}")
            return order

        except (BinanceAPIException, BinanceRequestException) as e:
            self.logger.error(f"Stop-Limit Order Error: {e}")
            raise


def run_cli():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--api-key", required=True)
    parser.add_argument("--api-secret", required=True)
    parser.add_argument("--symbol", required=True, help="Example: BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument(
        "--order-type",
        required=True,
        choices=["market", "limit", "stop-limit"],
    )
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)
    parser.add_argument("--stop-price", type=float)

    args = parser.parse_args()

    if args.order_type in ["limit", "stop-limit"] and args.price is None:
        print("Error: --price is required for limit and stop-limit orders")
        sys.exit(1)

    if args.order_type == "stop-limit" and args.stop_price is None:
        print("Error: --stop-price is required for stop-limit orders")
        sys.exit(1)

    bot = BasicBot(args.api_key, args.api_secret, testnet=True)

    try:
        if args.order_type == "market":
            order = bot.place_market_order(
                args.symbol, args.side, args.quantity
            )
        elif args.order_type == "limit":
            order = bot.place_limit_order(
                args.symbol, args.side, args.quantity, args.price
            )
        else:
            order = bot.place_stop_limit_order(
                args.symbol,
                args.side,
                args.quantity,
                args.price,
                args.stop_price,
            )

        print("\nOrder Placed Successfully")
        print("-------------------------")
        print(f"Order ID : {order['orderId']}")
        print(f"Symbol   : {order['symbol']}")
        print(f"Side     : {order['side']}")
        print(f"Type     : {order['type']}")
        print(f"Quantity : {order['origQty']}")
        print(f"Price    : {order.get('price', 'MARKET')}")
        print(f"Status   : {order['status']}")

    except Exception as e:
        print(f"Order Failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    run_cli()

