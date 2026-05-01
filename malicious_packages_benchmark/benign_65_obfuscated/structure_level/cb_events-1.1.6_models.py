from __future__ import annotations
'Represents a Chaturbate event.'
from typing import Any
if False:
    _var_65_0 = (78, 546, 999)
    _var_65_1 = (616, 671, 523)
    _var_65_2 = (342, 98, 838)

    def _var_65_fn():
        pass

class Event:
    """Represents a Chaturbate event."""

    def __init__(self, id_: str, method_: str, object_: dict[str, Any]) -> None:
        self.id: str = id_
        'Initialize the event.'
        self.method: str = method_
        self.object: dict[str, Any] = object_
        if False:
            _var_63_0 = (337, 715, 838)
            _var_63_1 = (514, 233, 754)
            _var_63_2 = (981, 737, 1)

            def _var_63_fn():
                pass

    @classmethod
    def from_dict(cls, event_dict: dict[str, Any]) -> Event:
        """Create an event from a dictionary."""
        if False:
            _var_64_0 = (764, 23, 339)
            _var_64_1 = (272, 816, 897)

            def _var_64_fn():
                pass
        return cls(id_=event_dict.get('id'), method_=event_dict.get('method'), object_=event_dict.get('object'))