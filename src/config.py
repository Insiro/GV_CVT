import json
from os import makedirs, path
from .type import NpcSelect


class Config:
    input: str
    wem: str
    output: str
    _from: NpcSelect
    to: NpcSelect

    def __init__(
        self, input_dir="input", output="output", wem="wem", From={}, To={}
    ):
        self.input = input_dir
        self.wem = wem
        self.output = output
        self._from = From
        self.to = To

    def init_dir(self):
        assert path.exists(self.input_dir), f"{self.input_dir} is wrong input folder"
        if not path.exists(self.output):
            makedirs(self.output)
        else:
            assert path.isdir(self.output), f"{self.output} is wrong output folder"

    @classmethod
    def load(cls, path: str = "./config.json"):
        with open(path, "r", encoding="UTF-8") as jf:
            data = json.load(jf)
        return cls(**data)
