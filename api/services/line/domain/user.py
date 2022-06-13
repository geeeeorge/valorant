import dataclasses


@dataclasses.dataclass(frozen=True)
class User:
    id: int
    name: str
    user_id: str
