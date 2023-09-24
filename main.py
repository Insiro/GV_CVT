from src.config import Config
from src.extractScript import script_extract
from src.cvt_file import cvtScriptFile2Key, convert_hash, cvt_external, apply

config = Config.load()
splited = script_extract(config)
to = cvtScriptFile2Key(splited[config.to["language"]])
actions = convert_hash(config, splited[config._from["language"]], to)
actions = cvt_external(config, actions)
#  path.join(config.input, config._from["language"])
apply(config.mod, config, actions)
