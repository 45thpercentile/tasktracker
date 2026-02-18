# TaskTracker API module

from models import Task, User


class TaskAPI:
    """Simple API for managing tasks."""

    def __init__(self):
        self.tasks = []
        self.users = []
        self.next_task_id = 1

    def create_task(self, title, description):
        """Create a new task."""
        task = Task(self.next_task_id, title, description)
        self.tasks.append(task)
        self.next_task_id += 1
        return task

    def get_task(self, task_id):
        """Get a task by ID."""
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    # TODO: add update_task method
    # TODO: add delete_task method
    # TODO: add list_tasks with filtering
    # TODO: add error handling
    # TODO: add authentication
