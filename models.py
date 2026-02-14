from datetime import datetime


class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.created_at = datetime.now()

    def __repr__(self):
        return f"User({self.username})"

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at.isoformat(),
        }


class Task:
    STATUSES = ["todo", "in_progress", "done"]

    def __init__(self, task_id, title, description, assigned_to=None):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = "todo"
        self.assigned_to = assigned_to
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __repr__(self):
        return f"Task({self.task_id}: {self.title})"

    def update_status(self, new_status):
        if new_status not in self.STATUSES:
            raise ValueError(f"Invalid status: {new_status}")
        self.status = new_status
        self.updated_at = datetime.now()

    def assign(self, user):
        self.assigned_to = user
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "assigned_to": self.assigned_to.username if self.assigned_to else None,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
