import datetime
from typing import Any, Iterator, List, Optional, Tuple, Type, TypeVar

from .asset import Asset
from .guild import Guild
from .role import Role
from .user import User

_PE = TypeVar("_PE", bound=PartialEmoji)

class PartialEmoji:
    animated: bool
    name: Optional[str]
    id: Optional[int]
    @classmethod
    def with_state(
        cls: Type[_PE],
        state: Any,
        *,
        animated: bool,
        name: Optional[str],
        id: Optional[int] = ...,
    ) -> _PE: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    def is_custom_emoji(self) -> bool: ...
    def is_unicode_emoji(self) -> bool: ...
    @property
    def url(self) -> Asset: ...

class Emoji:
    name: str
    id: int
    require_colons: bool
    animated: bool
    managed: bool
    guild_id: int
    available: bool
    user: Optional[User]
    def __iter__(self) -> Iterator[Tuple[str, Any]]: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    @property
    def created_at(self) -> datetime.datetime: ...
    @property
    def url(self) -> Asset: ...
    @property
    def roles(self) -> List[Role]: ...
    @property
    def guild(self) -> Guild: ...
    def is_usable(self) -> bool: ...
    async def delete(self, *, reason: Optional[str] = ...) -> None: ...
    async def edit(
        self,
        *,
        name: Optional[str] = ...,
        roles: Optional[List[Role]] = ...,
        reason: Optional[str] = ...,
    ) -> None: ...
