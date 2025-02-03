from typing_extensions import TypeAlias

class BasePriorityQueue:
    def __init__(self, **kw) -> None: ...
    def add(self, task, priority: int | None = None) -> None: ...
    def remove(self, task) -> None: ...
    def peek(self, default=...): ...
    def pop(self, default=...): ...
    def __len__(self) -> int: ...

class HeapPriorityQueue(BasePriorityQueue): ...
class SortedPriorityQueue(BasePriorityQueue): ...

PriorityQueue: TypeAlias = SortedPriorityQueue
