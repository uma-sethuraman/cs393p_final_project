from enum import IntEnum
class DifficultyTraceLevel(IntEnum):
    EASY = 2
    MEDIUM = 3
    HARD = 4

class ProblemType(IntEnum):
    ADDITION = 0
    SUBTRACTION = 1
    MULTIPLICATION = 2
    DIVISION = 3
    EXPONENTS = 4
    ROOTS = 5
    FRACTIONS = 6
    INEQUALITIES = 7
    PERCENTAGES = 8
    MULTIPLE_OPERATIONS = 9

def convert_difficulty(difficulty_level):
    if difficulty_level == "EASY":
        return DifficultyTraceLevel.EASY
    elif difficulty_level == "MEDIUM":
        return DifficultyTraceLevel.MEDIUM
    else:
        return DifficultyTraceLevel.HARD