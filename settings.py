import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

CK = os.environ.get("consumer_key")
CS = os.environ.get("consumer_secret")
AT = os.environ.get("access_token")
ATS = os.environ.get("access_token_secret")
