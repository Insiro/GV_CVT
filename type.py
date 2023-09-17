from typing import TypedDict


class ParseOption(TypedDict):
    input: str
    targets: dict[str, list[str]]
    output: str


class TextInstance(TypedDict):
    fileName: str
    language: str
    npcName: str
    text: str
    type: str


ScriptSection = dict[str, TextInstance]
