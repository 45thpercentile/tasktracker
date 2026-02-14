"""TaskTracker - a simple task management application."""

from models import User, Task
from utils import validate_email, generate_id, format_date
from config import APP_NAME, VERSION, DEFAULT_PAGE_SIZE


class TaskTracker:
    def __init__(self):
        self.users = {}
        self.tasks = {}
        self._user_counter = 0
        self._task_counter = 0

    def create_user(self, username, email):
        if not validate_email(email):
            raise ValueError(f"Invalid email: {email}")
        if username in self.users:
            raise ValueError(f"Username already exists: {username}")

        self._user_counter += 1
        user_id = generate_id("USR", self._user_counter)
        user = User(user_id, username, email)
        self.users[username] = user
        return user

    def create_task(self, title, description, assigned_to=None):
        self._task_counter += 1
        task_id = generate_id("TSK", self._task_counter)

        assignee = None
        if assigned_to:
            assignee = self.users.get(assigned_to)
            if not assignee:
                raise ValueError(f"User not found: {assigned_to}")

        task = Task(task_id, title, description, assignee)
        self.tasks[task_id] = task
        return task

    def update_task_status(self, task_id, new_status):
        task = self.tasks.get(task_id)
        if not task:
            raise ValueError(f"Task not found: {task_id}")
        task.update_status(new_status)
        return task

    def get_tasks_by_status(self, status):
        return [t for t in self.tasks.values() if t.status == status]

    def get_tasks_for_user(self, username):
        return [
            t for t in self.tasks.values()
            if t.assigned_to and t.assigned_to.username == username
        ]

    def list_tasks(self, page=1, page_size=None):
        if page_size is None:
            page_size = DEFAULT_PAGE_SIZE
        all_tasks = list(self.tasks.values())
        start = (page - 1) * page_size
        end = start + page_size
        return all_tasks[start:end]

    def summary(self):
        total = len(self.tasks)
        by_status = {}
        for status in Task.STATUSES:
            count = len(self.get_tasks_by_status(status))
            by_status[status] = count
        return {
            "total_tasks": total,
            "total_users": len(self.users),
            "by_status": by_status,
        }


def main():
    print(f"{APP_NAME} v{VERSION}")
    print("-" * 30)

    tracker = TaskTracker()

    alice = tracker.create_user("alice", "alice@example.com")
    bob = tracker.create_user("bob", "bob@example.com")

    t1 = tracker.create_task("Set up database", "Initialize the DB schema", "alice")
    t2 = tracker.create_task("Write tests", "Add unit tests for models", "bob")
    t3 = tracker.create_task("Deploy to staging", "Push to staging environment")

    tracker.update_task_status(t1.task_id, "in_progress")
    tracker.update_task_status(t2.task_id, "done")

    print("\nAll tasks:")
    for task in tracker.list_tasks():
        print(f"  {task.task_id}: {task.title} [{task.status}]")

    print("\nSummary:")
    summary = tracker.summary()
    for key, value in summary.items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
