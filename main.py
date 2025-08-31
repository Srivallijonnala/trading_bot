# main.py

from src.config import API_KEY, API_SECRET
from src.bot import BasicBot

def main():
    print("🚀 Starting Binance Trading Bot (Simulation Mode)...")

    # Initialize bot with API keys
    bot = BasicBot(API_KEY, API_SECRET)

    print("✅ Bot initialized successfully!\n")

    # Example: Place a BUY Market Order
    order = bot.place_order(symbol="BTCUSDT", side="BUY", order_type="MARKET", quantity=0.01)

    print("\n🎯 Final Order Response:", order)

if __name__ == "__main__":
    main()

