from enum import Enum


class Status(str, Enum):
    """
    Status of the resource.
    """

    CREATED = "created"
    PROCESSING = "processing"
    FINISHED = "finished"
    FAILED = "failed"

    def __str__(self) -> str:  # type: ignore
        return str(self.value)
