import os
from dotenv import load_dotenv

load_dotenv() # Loads the env first
DISCORD_TOKEN = os.environ.get('BOT_TOKEN')