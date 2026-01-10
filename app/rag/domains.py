from enum import Enum

class Domain(str, Enum):
    NALSA = "nalsa"
    JUDICIAL = "judicial"
    CASE = "case"
    RESEARCH = "research"
