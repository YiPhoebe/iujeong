from collections.abc import Callable
from email.message import Message
from email.policy import Policy
from typing import Generic, TypeVar, overload

__all__ = ["FeedParser", "BytesFeedParser"]

_MessageT = TypeVar("_MessageT", bound=Message, default=Message)

class FeedParser(Generic[_MessageT]):
    @overload
    def __init__(self: FeedParser[Message], _factory: None = None, *, policy: Policy[Message] = ...) -> None: ...
    @overload
    def __init__(self, _factory: Callable[[], _MessageT], *, policy: Policy[_MessageT] = ...) -> None: ...
    def feed(self, data: str) -> None: ...
    def close(self) -> _MessageT: ...

class BytesFeedParser(FeedParser[_MessageT]):
    @overload
    def __init__(self: BytesFeedParser[Message], _factory: None = None, *, policy: Policy[Message] = ...) -> None: ...
    @overload
    def __init__(self, _factory: Callable[[], _MessageT], *, policy: Policy[_MessageT] = ...) -> None: ...
    def feed(self, data: bytes | bytearray) -> None: ...  # type: ignore[override]
