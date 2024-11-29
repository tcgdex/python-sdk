from dataclasses import dataclass, field
from typing import Any


@dataclass
class Model:
    sdk: Any = field(init=False, default=None)
