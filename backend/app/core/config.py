from dotenv import dotenv_values, load_dotenv
from os import getenv

load_dotenv()
conf = dotenv_values()
# postgres = "postgresql://localmachine:0503@localhost:5432/new_test"
postgres = getenv("DATABASE_URL")

print(conf, postgres)
