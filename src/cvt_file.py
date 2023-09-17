from .type import *
from os import path, listdir, rename


def rmLangPath(fileName: str) -> str:
    return "\\".join(fileName.split("\\")[1:])


def cvtScriptFile2Key(script: ScriptSection) -> FileKeyScriptSection:
    output: FileKeyScriptSection = {}
    for obj in script.values():
        k = rmLangPath(obj["fileName"])
        output[k] = obj
    return output


def convertName(
    from_scritp: ScriptSection, to_script: FileKeyScriptSection, input_dir: str
):
    assert path.isdir(input_dir)
    for dname in listdir(input_dir):
        dir = path.join(input_dir, dname)
        if not path.isdir(dir):
            continue
        for item in listdir(dir):
            fsplit = item.split(".")
            if len(fsplit) != 2:
                continue
            from_hash = fsplit[0]
            if from_hash not in from_scritp:
                continue

            key = rmLangPath(from_scritp[from_hash]["fileName"])
            new_hash = to_script[key]["hash"]
            original = path.join(dir, from_hash + ".wem")
            target = path.join(dir, new_hash + ".wem")

            rename(original, target)
