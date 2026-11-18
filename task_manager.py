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

    @staticmethod
    def format_task(task):
        """Render one task as a single line, e.g. ``[x] 2. Buy books``."""
        checkbox = "[x]" if task.completed else "[ ]"
        return f"{checkbox} {task.id}. {task.title}"

    def display_tasks(self):
        """Return a printable listing of all tasks (or an empty note)."""
        if not self.tasks:
            return "No tasks yet. Add one to get started!"
        lines = ["Your tasks:"]
        lines.extend(self.format_task(task) for task in self.tasks)
        return "\n".join(lines)

    # --- add-task section ------------------------------------------------
    # Implemented on the feature/add-task branch.

    # --- complete-task section -------------------------------------------
    # Implemented on the feature/complete-task branch.

    # --- delete-task section ---------------------------------------------
    # Implemented on the feature/delete-task branch.
