# src/bot.py

from src.utils import log_message

class BasicBot:
    def __init__(self, api_key: str, api_secret: str, testnet: bool = True):
        self.api_key = api_key
        self.api_secret = api_secret
        self.testnet = testnet
        log_message("Bot initialized with API credentials (dummy).")

    def place_order(self, symbol: str, side: str, order_type: str, quantity: float, price: float = None):
        """
        Simulate placing an order.
        In real case, this would use Binance API.
        """
        log_message(f"Placing {order_type} order: {side} {quantity} {symbol} @ {price if price else 'MARKET'}")

        # Fake order response
        order_response = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
            "price": price if price else "MARKET",
            "status": "FILLED"
        }

        log_message(f"Order executed: {order_response}")
        return order_response
