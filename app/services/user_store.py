
# Temporary in-memory storage for the assessment prototype.
# All registered users are stored here while the application runs.
# Data will be lost when the application restarts.

users: dict[str, dict] = {}
