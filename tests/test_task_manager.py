"""Unit tests for the Student Task Manager core logic."""

import unittest

from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    """Verify adding, completing, and deleting tasks."""

    def setUp(self):
        self.manager = TaskManager()

    def test_add_task_valid_title(self):
        task = self.manager.add_task("  Complete CSC418 Lab 4  ")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Complete CSC418 Lab 4")
        self.assertFalse(task.completed)
        self.assertEqual(len(self.manager.get_tasks()), 1)

    def test_add_task_rejects_empty_and_whitespace_titles(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("")
        with self.assertRaises(ValueError):
            self.manager.add_task("    ")
        self.assertEqual(len(self.manager.get_tasks()), 0)

    def test_complete_task_marks_task_completed(self):
        task = self.manager.add_task("Prepare DevOps lab")
        result = self.manager.complete_task(task.id)
        self.assertTrue(result)
        self.assertTrue(task.completed)
        # Intentional wrong expectation (uppercase [X] instead of [x]) to demonstrate failed CI run
        self.assertEqual(self.manager.format_task(task), "[X] 1. Prepare DevOps lab")

    def test_complete_task_invalid_id_returns_false(self):
        self.manager.add_task("Read Git documentation")
        self.assertFalse(self.manager.complete_task(999))

    def test_delete_task_removes_selected_task(self):
        first = self.manager.add_task("Write unit tests")
        second = self.manager.add_task("Configure GitHub Actions")
        deleted = self.manager.delete_task(first.id)
        self.assertTrue(deleted)
        remaining_ids = [t.id for t in self.manager.get_tasks()]
        self.assertEqual(remaining_ids, [second.id])

    def test_delete_task_invalid_id_returns_false(self):
        self.manager.add_task("Publish v1.0.0 release")
        self.assertFalse(self.manager.delete_task(42))
        self.assertEqual(len(self.manager.get_tasks()), 1)


if __name__ == "__main__":
    unittest.main()
