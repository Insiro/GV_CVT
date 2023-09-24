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


class Action:
    src_hash: str
    src_ext: str
    dst_hash: str
    dst_ext: str

    def __init__(
        self,
        src_hash: str,
        dst_hash: str,
        src_ext: str,
        dst_ext: str,
    ) -> None:
        self.src_ext = src_ext
        self.src_hash = src_hash
        self.dst_ext = dst_ext
        self.dst_hash = dst_hash


def convert_hash(
    from_scritp: ScriptSection, to_script: FileKeyScriptSection, mod_dir: str
):
    actions: dict[str, Action] = {}
    assert path.isdir(mod_dir)
    for ext in listdir(mod_dir):
        dir = path.join(mod_dir, ext)
        if not path.isdir(dir):
            continue
        for item in listdir(dir):
            fsplit = item.split(".")
            if len(fsplit) != 2:
                continue

            from_hash = fsplit[0]
            if from_hash not in from_scritp:
                continue

            f_key = rmLangPath(from_scritp[from_hash]["fileName"])
            new_hash = to_script[f_key]["hash"]

            actions[from_hash] = Action(
                src_ext=ext, dst_ext=ext, src_hash=from_hash, dst_hash=new_hash
            )
    return actions


def apply(config: Config, actions: dict[str, Action]):
    config.input
    config.wem

    rmtree(config.wem)
    for hash, item in actions.items():
        makedirs(path.dirname(path.join(config.wem, item.dst_ext)), exist_ok=True)
        from_path = path.join(config.input, config._from["language"])
        copyfile(
            path.join(from_path, item.src_ext, item.src_hash + ".wem"),
            path.join(config.wem, item.dst_ext, item.dst_hash + ".wem"),
        )
