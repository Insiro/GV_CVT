import json
from collections import defaultdict
from os import makedirs, path

from type import *
from config import Config


config = Config.load()


def script_extract(config: Config):
    with open(path.join(config.input, "result.json"), encoding="UTF-8") as ji:
        script: ScriptSection = json.load(ji)

    targets = config.targets
    splited: dict[str, ScriptSection] = {
        key: defaultdict(None) for key in targets.keys()
    }
    for key, obj in script.items():
        lang = obj["language"]
        if lang not in splited:
            continue
        if "npcName" not in obj:
            continue
        if obj["npcName"] not in targets[lang]:
            continue
        splited[lang][key] = obj

    out_folder = path.join(config.output, "scripts")
    if not path.isdir(out_folder):
        makedirs(out_folder)
    for key, obj in splited.items():
        fname = path.join(out_folder, key + ".json")
        with open(fname, "w", encoding="UTF-8") as f:
            json.dump(obj, f, indent=2, ensure_ascii=False)


script_extract(config)
