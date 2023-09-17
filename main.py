from src.config import Config
from src.extractScript import script_extract

config = Config.load()
script_extract(config)
