import os

def get_env_variable(name, default=None):
    try:
        return os.environ[name]
    except KeyError:
        return default

# Example usage
LOG_LEVEL = get_env_variable("LOG_LEVEL", "WARNING")
HISTORY_FILE = get_env_variable("HISTORY_FILE", "history.csv")
