import os

from dynaconf import Dynaconf

# We set our environment variable in Python.
# It's for demo purposes only.
# We should set it in our shell.
os.environ["THE_SECRET"] = "ABC-123"

settings = Dynaconf(envvar_prefix=False, load_dotenv=True)

# Secret
# DB_SECRET=${THE_SECRET}

print(settings.DB_SECRET)
