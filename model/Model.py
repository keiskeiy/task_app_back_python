from pydantic import ConfigDict
from pydantic.alias_generators import to_camel
from pydantic import BaseModel


class Model(BaseModel):
    # このモデルを継承すると、フィールド名がキャメルケースに変換されます
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
