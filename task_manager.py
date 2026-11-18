"""Core logic for the Student Task Manager.

This module holds the data model and the in-memory task store.
It deliberately knows nothing about the console UI (that lives in
``main.py``) so the logic can be unit-tested on its own.
"""

from dataclasses import dataclass, field


@dataclass
class Task:
    """A single student task."""

    id: int
    title: str
    completed: bool = False


@dataclass
class TaskManager:
    """Stores tasks and provides operations on them."""

    tasks: list = field(default_factory=list)
    _next_id: int = 1

    # --- display section -------------------------------------------------
    def get_tasks(self):
        """Return all tasks, in the order they were added."""
        return list(self.tasks)

    # --- add-task section ------------------------------------------------
    # Implemented on the feature/add-task branch.

    # --- complete-task section -------------------------------------------
    # Implemented on the feature/complete-task branch.

    # --- delete-task section ---------------------------------------------
    # Implemented on the feature/delete-task branch.
