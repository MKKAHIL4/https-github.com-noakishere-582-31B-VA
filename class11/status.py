from enum import Enum

class CourseStatus(Enum):
    OPEN = "open"
    CLOSED = "closed"
    CANCELED = "canceled"

class DeliveryMode(Enum):
    ONLINE = "online"
    IN_PERSON = "in_person"
    HYBRID = "hybrid"

class StudentLevel(Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
