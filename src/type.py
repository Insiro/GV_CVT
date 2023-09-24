from typing import TypedDict


class TextInstance(TypedDict):
    fileName: str
    language: str
    npcName: str
    text: str
    type: str
    hash: str


class NpcSelect(TypedDict):
    language: str
    npcName: str


ScriptSection = dict[str, TextInstance]
"""key: hash"""
LangSplitedScript = dict[str, ScriptSection]
"""key: Language"""
FileKeyScriptSection = dict[str, TextInstance]
"""key: filepath without Language"""


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


HashedActions = dict[str, Action]
