import os
from dotenv import load_dotenv

# Loading environment variables from .env file
load_dotenv()

# Read API keys (using dummy keys for now because i didn't set up)
API_KEY = os.getenv("BINANCE_API_KEY", "valli")
API_SECRET = os.getenv("BINANCE_API_SECRET", "valli")

# Base URL for Binance Futures Testnet
BASE_URL = "https://testnet.binancefuture.com"
