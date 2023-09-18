import json
from collections import defaultdict
from os import makedirs, path

from .type import *
from .config import Config


def script_extract(config: Config, save=False) -> LangSplitedScript:
    with open(path.join(config.input, "result.json"), encoding="UTF-8") as ji:
        script: ScriptSection = json.load(ji)

    src_lang = config._from["language"]
    src_npc = config._from["npcName"]
    dst_lang = config.to["language"]
    dst_npc = config.to["npcName"]

    splited: LangSplitedScript = {
        src_lang: defaultdict(None),
        dst_lang: defaultdict(None),
    }
    for key, obj in script.items():
        if "npcName" not in obj:
            continue
        lang = obj["language"]
        if lang not in [src_lang, dst_lang]:
            continue
        if obj["npcName"] not in [src_npc, dst_npc]:
            continue
        obj["hash"] = key
        splited[lang][key] = obj
    if save:
        __save_script(config, splited)
    return splited


def __save_script(config: Config, splited: LangSplitedScript):
    out_folder = path.join(config.output, "scripts")
    if not path.isdir(out_folder):
        makedirs(out_folder)
    for key, obj in splited.items():
        fname = path.join(out_folder, key + ".json")
        with open(fname, "w", encoding="UTF-8") as f:
            json.dump(obj, f, indent=2, ensure_ascii=False)
