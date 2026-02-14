# Application configuration

APP_NAME = "TaskTracker"
VERSION = "1.0.0"
DEBUG = False

# Database settings
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "tasktracker"

# Retry settings
MAX_RETRIES = 3
RETRY_DELAY = 1.0

# Pagination
DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100

# Feature flags
ENABLE_NOTIFICATIONS = True
ENABLE_SEARCH = False
ENABLE_EXPORT = False
