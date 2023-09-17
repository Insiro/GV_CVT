from src.config import Config
from src.extractScript import script_extract
from src.cvt_file import cvtScriptFile2Key, convertName
from os import path

config = Config.load()
splited = script_extract(config)
to = cvtScriptFile2Key(splited["KR"])
convertName(splited["JP"], to, path.join(config.input, "fem_kazuha"))
