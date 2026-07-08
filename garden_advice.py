"""
Garden Advice App
------------------
Gives gardening tips and advice based on the current month and season.
"""

import datetime

MONTH_ADVICE = {
    1: "January: Plan your garden layout and order seeds.",
    2: "February: Start seeds indoors for early spring planting.",
    3: "March: Prepare soil and beds for planting.",
    4: "April: Plant cool-season vegetables like lettuce and peas.",
    5: "May: Transplant seedlings outdoors after the last frost.",
    6: "June: Water regularly and watch for pests.",
    7: "July: Harvest summer vegetables and keep up with watering.",
    8: "August: Continue harvesting and plant fall crops.",
    9: "September: Start cleaning up summer plants and prepare for fall.",
    10: "October: Plant bulbs for spring flowers.",
    11: "November: Mulch beds to protect plants from frost.",
    12: "December: Plan next year's garden and review notes.",
}


def get_advice(month=None):
    """
    Return gardening advice for a given month.

    Args:
        month (int, optional): Month number (1-12). Defaults to the
            current month if not provided.

    Returns:
        str: Gardening advice for the given month, or an error message
            if the month is invalid.
    """
    if month is None:
        month = datetime.datetime.now().month
    return MONTH_ADVICE.get(month, "Invalid month.")


def main():
    """Entry point: print advice for the current month."""
    print(get_advice())


if __name__ == "__main__":
    main()
