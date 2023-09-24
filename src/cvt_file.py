from .type import *
from os import path, listdir, rename, makedirs
from shutil import rmtree, copyfile
from .config import Config


def rmLangPath(fileName: str) -> str:
    return "\\".join(fileName.split("\\")[1:])


def cvtScriptFile2Key(script: ScriptSection) -> FileKeyScriptSection:
    output: FileKeyScriptSection = {}
    for obj in script.values():
        k = rmLangPath(obj["fileName"])
        output[k] = obj
    return output


def convert_hash(
    config: Config, from_scritp: ScriptSection, to_script: FileKeyScriptSection
):
    actions: HashedActions = {}
    assert config.mod is not None
    mod_dir = config.mod
    print(mod_dir)
    assert path.isdir(mod_dir)
    for ext in listdir(mod_dir):
        dir = path.join(mod_dir, ext)
        if not path.isdir(dir):
            continue
        for item in listdir(dir):
            fsplit = item.split(".")
            if len(fsplit) != 2 or fsplit[1] != "wem":
                continue

            from_hash = fsplit[0]
            if from_hash not in from_scritp:
                continue

            f_key = rmLangPath(from_scritp[from_hash]["fileName"])
            new_hash = to_script[f_key]["hash"]

            actions[new_hash] = Action(
                src_ext=ext, dst_ext=ext, src_hash=from_hash, dst_hash=new_hash
            )
    return actions


def cvt_external(config: Config, actions: HashedActions):
    from_path = path.join(config.input, config._from["language"])
    to_path = path.join(config.input, config.to["language"])
    assert path.isdir(from_path)
    assert path.isdir(to_path)
    for ext in listdir(to_path):
        if not ext.startswith("External"):
            continue
        dir = path.join(to_path, ext)
        for item in listdir(dir):
            hash, fext = item.split(".")
            if fext != "wem" or hash not in actions:
                continue

            actions[hash].dst_ext = ext
    return actions


def apply(src: str, config: Config, actions: HashedActions):
    if path.isdir(config.wem):
        rmtree(config.wem)
    for hash, item in actions.items():
        ext_dir = path.abspath(path.join(config.wem, item.dst_ext))
        if not path.isdir(ext_dir):
            makedirs(ext_dir)
        copyfile(
            path.join(src, item.src_ext, item.src_hash + ".wem"),
            path.join(config.wem, item.dst_ext, item.dst_hash + ".wem"),
        )
