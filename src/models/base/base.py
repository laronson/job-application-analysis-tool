from abc import ABC
from typing import TypedDict
from langchain_core.language_models import BaseChatModel
from langchain_core.output_parsers import StrOutputParser


class ModelConfig(TypedDict):
    model: BaseChatModel
    # TODO: see if there are other parsers that would be better for specific models.  If so, I may want to use the base
    # parser class.
    parser: StrOutputParser


class BaseModel(ABC):
    def __init__(self, config: ModelConfig):
        self.model = config.get("model")
        self.parser = config.get("parser")
