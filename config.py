import os
from dotenv import load_dotenv

load_dotenv()

MAX_RETRIES = int(os.getenv("MAX_RETRIES", 5))

EXP_BASE = 7
INITIAL_DELAY = 1

HTTP_STATUS_CODES = [
    429,
    500,
    503,
    504
]