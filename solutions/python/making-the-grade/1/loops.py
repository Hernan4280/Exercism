"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    "Round all provided student scores."

    new_list = []
    for score in student_scores:
        new_list.append(round(score))
    return new_list


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided."""

    count = 0
    for score in student_scores:
        if score <= 40:
            count += 1
    return count


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold."""

    new_list = []
    for score in student_scores:
        if score >= threshold:
            new_list.append(score)
    return new_list


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade."""

    x = highest - 40
    result = round(x / 4)
    a = 41
    new_list = [a]
    for i in range(3):
        a += result
        new_list.append(a)
    return new_list


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order."""

    new_list = []
    for i in range(len(student_scores)):
        new_list.append(f"{i + 1}. {student_names[i]}: {student_scores[i]}")
    return new_list


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam."""

    for i in student_info:
        if 100 in i:
            return i
    return []
