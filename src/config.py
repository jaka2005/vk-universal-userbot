from dataclasses import dataclass
from typing import List
from dacite import from_dict
import json


CONFIG_PATH = "./config.json"


@dataclass    
class Init:
    token: str
    user_id: int
    
@dataclass
class Preferences:
    swear_words: List[str]
    censoring: bool

@dataclass
class Config:
    init: Init
    preferences: Preferences

    @classmethod
    def from_json(cls, file_name: str, encoding="utf-8"):
        with open(CONFIG_PATH, "r", encoding="utf-8") as file:
            return from_dict(data_class=cls, data=json.load(file))


config = Config.from_json(CONFIG_PATH)
