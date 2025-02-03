import sys
from _typeshed import ReadableBuffer
from collections.abc import Mapping
from io import BytesIO
from logging import Logger
from socket import _RetAddress, socket
from typing_extensions import TypeAlias

_Socket: TypeAlias = socket
_SocketMap: TypeAlias = Mapping[int, socket]

socket_map: _SocketMap

class ExitNow(Exception): ...

def read(obj: dispatcher) -> None: ...
def write(obj: dispatcher) -> None: ...
def readwrite(obj: dispatcher, flags: int) -> None: ...
def poll(timeout: float = 0.0, map: _SocketMap | None = None) -> None: ...
def poll2(timeout: float = 0.0, map: _SocketMap | None = None) -> None: ...

poll3 = poll2

def loop(timeout: float = 30.0, use_poll: bool = False, map: _SocketMap | None = None, count: int | None = None) -> None: ...
def compact_traceback() -> tuple[tuple[str, str, str], BaseException, BaseException, str]: ...

class dispatcher:
    debug: bool
    connected: bool
    accepting: bool
    connecting: bool
    closing: bool
    addr: _RetAddress | None
    ignore_log_types: frozenset[str]
    logger: Logger
    @staticmethod
    def compact_traceback() -> tuple[tuple[str, str, str], BaseException, BaseException, str]: ...
    socket: socket | None
    def __init__(self, sock: _Socket | None = None, map: _SocketMap | None = None) -> None: ...
    def add_channel(self, map: _SocketMap | None = None) -> None: ...
    def del_channel(self, map: _SocketMap | None = None) -> None: ...
    family_and_type: tuple[int, int]
    def create_socket(self, family: int = ..., type: int = ...) -> None: ...
    def set_socket(self, sock: _Socket, map: _SocketMap | None = None) -> None: ...
    def set_reuse_addr(self) -> None: ...
    def readable(self) -> bool: ...
    def writable(self) -> bool: ...
    def listen(self, num: int) -> None: ...
    def bind(self, addr: _RetAddress) -> None: ...
    def accept(self) -> tuple[_Socket, _RetAddress] | None: ...
    def send(self, data: bytes, do_close: bool = True) -> int: ...
    def recv(self, buffer_size: int) -> bytes: ...
    def close(self) -> None: ...
    def log(self, message: str) -> None: ...
    def log_info(self, message: str, type: str = "info") -> None: ...
    def handle_read_event(self) -> None: ...
    def handle_connect_event(self) -> None: ...
    def handle_write_event(self) -> None: ...
    def handle_expt_event(self) -> None: ...
    def handle_error(self) -> None: ...
    def handle_expt(self) -> None: ...
    def handle_read(self) -> None: ...
    def handle_write(self) -> None: ...
    def handle_connect(self) -> None: ...
    def handle_accept(self) -> None: ...
    def handle_accepted(self, sock: _Socket, addr: _RetAddress) -> None: ...
    def handle_close(self) -> None: ...

def close_all(map: _SocketMap | None = None, ignore_all: bool = False) -> None: ...

if sys.platform != "win32":
    class file_wrapper:
        fd: BytesIO
        def __init__(self, fd: BytesIO) -> None: ...
        def __del__(self) -> None: ...
        def recv(self, length: int, /) -> bytes: ...
        def send(self, data: ReadableBuffer, /) -> bytes: ...
        def getsockopt(self, level: int, optname: int, buflen: bool | None = None) -> int: ...
        read = recv
        write = send
        def close(self) -> None: ...
        def fileno(self) -> BytesIO: ...

    class file_dispatcher(dispatcher):
        connected: bool
        def __init__(self, fd: BytesIO, map: _SocketMap | None = None) -> None: ...
        socket: socket
        def set_file(self, fd: BytesIO) -> None: ...
