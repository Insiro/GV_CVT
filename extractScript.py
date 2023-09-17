import json
from collections import defaultdict
from os import makedirs, path
from typing import Tuple
from type import *


def load() -> Tuple[ParseOption, ScriptSection]:
    with open("parseOption.json", encoding="UTF-8") as po:
        option: ParseOption = json.load(po)
    with open(option["input"], encoding="UTF-8") as ji:
        parsedScript: ScriptSection = json.load(ji)

    out_folder = option["output"]
    if not path.exists(out_folder):
        makedirs(out_folder)
    else:
        assert path.isdir(out_folder), f"{out_folder} is wrong output folder"
    return option, parsedScript


def script_extract(option: ParseOption, script: ScriptSection):
    targets = option["targets"]

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

    out_folder = option["output"]
    for key, obj in splited.items():
        fname = path.join(out_folder, key + ".json")
        with open(fname, "w", encoding="UTF-8") as f:
            json.dump(obj, f, indent=2, ensure_ascii=False)


option, parsedScript = load()
script_extract(option, parsedScript)
