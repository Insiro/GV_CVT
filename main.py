from src.config import Config
from src.extractScript import script_extract
from src.cvt_file import cvtScriptFile2Key, convertName
from os import path

config = Config.load()
splited = script_extract(config)
to = cvtScriptFile2Key(splited[config.to["language"]])
convertName(splited[config._from["language"]], to, path.join(config.input_pck))
