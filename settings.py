import os
from dotenv import load_dotenv
from os.path import join, dirname

env_file = os.environ.get('ENV_FILE', '.env')

dotenv_path = join(dirname((__file__)), env_file)
load_dotenv(dotenv_path)

PSQL_DB = os.getenv('PSQL_DB')
PSQL_DBF = os.getenv('PSQL_DBF')
PSQL_USER = os.getenv('PSQL_USER')
PSQL_HOST = os.getenv('PSQL_HOST')
PSQL_PASSWORD = os.getenv('PSQL_PASSWORD')
PSQL_PORT = os.getenv('PSQL_PORT')