# TaskTracker API module

from models import Task, User


class TaskNotFoundError(Exception):
    """Raised when a task is not found."""
    pass


class TaskAPI:
    """Simple API for managing tasks."""

    def __init__(self):
        self.tasks = []
        self.users = []
        self.next_task_id = 1

    def create_task(self, title, description):
        """Create a new task."""
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")
        task = Task(self.next_task_id, title, description)
        self.tasks.append(task)
        self.next_task_id += 1
        return task

    def get_task(self, task_id):
        """Get a task by ID."""
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        raise TaskNotFoundError(f"Task with ID {task_id} not found")

    def update_task(self, task_id, status):
        """Update a task's status."""
        task = self.get_task(task_id)
        task.update_status(status)
        return task

    def delete_task(self, task_id):
        """Delete a task by ID."""
        task = self.get_task(task_id)
        self.tasks.remove(task)
        return task

    def list_tasks(self, status=None, page=1, page_size=20):
        """List tasks with optional filtering and pagination."""
        filtered = self.tasks
        if status:
            filtered = [t for t in filtered if t.status == status]
        start = (page - 1) * page_size
        end = start + page_size
        return filtered[start:end]

    # TODO: add authentication
