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

SEASON_ADVICE = {
    "Spring": "Spring: Focus on planting, soil prep, and protecting new growth from late frosts.",
    "Summer": "Summer: Water consistently, mulch to retain moisture, and watch for pests.",
    "Fall": "Fall: Harvest remaining crops, clean up beds, and plant for next spring.",
    "Winter": "Winter: Plan next year's garden, maintain tools, and protect perennials from frost.",
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


def get_season(month=None):
    """
    Determine the season for a given month.

    Args:
        month (int, optional): Month number (1-12). Defaults to the
            current month if not provided.

    Returns:
        str: One of "Spring", "Summer", "Fall", "Winter", or
            "Unknown" if the month is invalid.
    """
    if month is None:
        month = datetime.datetime.now().month

    if month in (3, 4, 5):
        return "Spring"
    elif month in (6, 7, 8):
        return "Summer"
    elif month in (9, 10, 11):
        return "Fall"
    elif month in (12, 1, 2):
        return "Winter"
    return "Unknown"


def get_season_advice(season=None):
    """
    Return general gardening advice for a given season.

    Args:
        season (str, optional): One of "Spring", "Summer", "Fall",
            "Winter". Defaults to the current season if not provided.

    Returns:
        str: Seasonal gardening advice, or an error message if the
            season is not recognized.
    """
    if season is None:
        season = get_season()
    return SEASON_ADVICE.get(season, "Invalid season.")


def main():
    """Entry point: print advice for the current month and season."""
    print(get_advice())
    print(get_season_advice())


if __name__ == "__main__":
    main()
