from dotenv import dotenv_values, load_dotenv
from os import getenv

load_dotenv()
conf = dotenv_values()
postgres = getenv("DATABASE_URL")

print(conf, postgres)
