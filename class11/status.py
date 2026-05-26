from enum import Enum

class CoursesStatus(Enum):
    OPEN = "open"
    CLOSED = "closed"
    CANCELED = "canceled"

class DeliveredMode(Enum):
    ONLINE = "online"
    IN_PERSON = "in_person"
    HYBRID = "hybrid"

class StudentLevel(Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
