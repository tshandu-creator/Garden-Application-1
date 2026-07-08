"""
Garden Advice App
------------------
Gives gardening tips and advice based on the current month and season.
"""

# TODO: Replace hardcoded month/season strings with constants or an Enum
# TODO: Move advice data into a separate config/data structure instead of
#       embedding it directly in the logic below.

def get_advice():
    import datetime
    month = datetime.datetime.now().month

    # TODO: Refactor this long if/elif chain into a function that maps
    #       month -> advice, e.g. using a dictionary lookup.
    if month == 1:
        print("January: Plan your garden layout and order seeds.")
    elif month == 2:
        print("February: Start seeds indoors for early spring planting.")
    elif month == 3:
        print("March: Prepare soil and beds for planting.")
    elif month == 4:
        print("April: Plant cool-season vegetables like lettuce and peas.")
    elif month == 5:
        print("May: Transplant seedlings outdoors after the last frost.")
    elif month == 6:
        print("June: Water regularly and watch for pests.")
    elif month == 7:
        print("July: Harvest summer vegetables and keep up with watering.")
    elif month == 8:
        print("August: Continue harvesting and plant fall crops.")
    elif month == 9:
        print("September: Start cleaning up summer plants and prepare for fall.")
    elif month == 10:
        print("October: Plant bulbs for spring flowers.")
    elif month == 11:
        print("November: Mulch beds to protect plants from frost.")
    elif month == 12:
        print("December: Plan next year's garden and review notes.")
    else:
        print("Invalid month.")

    # TODO: Add a function for season-based advice (Spring, Summer, Fall, Winter)
    #       instead of only doing month-based advice.

    # TODO: Add docstrings/comments explaining what this function does,
    #       its parameters, and return value.

    # TODO: Consider returning the advice string instead of printing it,
    #       so it can be tested and reused elsewhere (e.g. in a web app).


# TODO: Add a main() function and an `if __name__ == "__main__":` guard
#       instead of calling get_advice() directly at import time.
get_advice()
