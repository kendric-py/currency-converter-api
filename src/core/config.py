import dotenv

import os


dotenv.load_dotenv()


DATABASE_URL = os.getenv('DATABASE_URL')
CENTRAL_BANK_LINK = os.getenv('CENTRAL_BANK_LINK')
CACHE_RATES_BANK_PATH = os.getenv('CACHE_RATES_BANK_PATH')