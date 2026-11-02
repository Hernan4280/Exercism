"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate."""

    return record[1]


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components."""

    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match."""

    return tuple(azara_record[1]) in rui_record


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group."""

    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    else:
        return "not a match"


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records."""

    report = ""
    for value in combined_record_group:
        report += f"('{value[0]}', '{value[2]}', {value[3]}, '{value[4]}')\n"
    return report
