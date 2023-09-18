import json
from os import makedirs, path


class Config:
    input: str
    input_pck: str
    output: str
    # key: Langauge, value : [npcName]
    targets: dict[str, list[str]]

    def __init__(
        self, input_dir="input", output="output", input_pck="input_pck", targets={}
    ):
        self.input = input_dir
        self.output = output
        self.targets = targets
        self.input_pck = input_pck

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
