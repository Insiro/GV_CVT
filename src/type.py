from typing import TypedDict


class TextInstance(TypedDict):
    fileName: str
    language: str
    npcName: str
    text: str
    type: str
    hash: str


ScriptSection = dict[str, TextInstance]
"""key: hash"""
LangSplitedScript = dict[str, ScriptSection]
"""key: Language"""
FileKeyScriptSection = dict[str, TextInstance]
"""key: filepath without Language"""
