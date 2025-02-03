from _typeshed import ReadableBuffer
from asyncio import transports
from typing import Any

__all__ = ("BaseProtocol", "Protocol", "DatagramProtocol", "SubprocessProtocol", "BufferedProtocol")

class BaseProtocol:
    def connection_made(self, transport: transports.BaseTransport) -> None: ...
    def connection_lost(self, exc: Exception | None) -> None: ...
    def pause_writing(self) -> None: ...
    def resume_writing(self) -> None: ...

class Protocol(BaseProtocol):
    def data_received(self, data: bytes) -> None: ...
    def eof_received(self) -> bool | None: ...

class BufferedProtocol(BaseProtocol):
    def get_buffer(self, sizehint: int) -> ReadableBuffer: ...
    def buffer_updated(self, nbytes: int) -> None: ...
    def eof_received(self) -> bool | None: ...

class DatagramProtocol(BaseProtocol):
    def connection_made(self, transport: transports.DatagramTransport) -> None: ...  # type: ignore[override]
    # addr can be a tuple[int, int] for some unusual protocols like socket.AF_NETLINK.
    # Use tuple[str | Any, int] to not cause typechecking issues on most usual cases.
    # This could be improved by using tuple[AnyOf[str, int], int] if the AnyOf feature is accepted.
    # See https://github.com/python/typing/issues/566
    def datagram_received(self, data: bytes, addr: tuple[str | Any, int]) -> None: ...
    def error_received(self, exc: Exception) -> None: ...

class SubprocessProtocol(BaseProtocol):
    def pipe_data_received(self, fd: int, data: bytes) -> None: ...
    def pipe_connection_lost(self, fd: int, exc: Exception | None) -> None: ...
    def process_exited(self) -> None: ...
