from datetime import datetime, timedelta


# Format number
def format_number(curr_num, match_num):

    """
    Give current number an example of number with decimals desired
    Function will return the correctly formatted string
    :param curr_num: current number
    :param match_num: example number
    :return: formatted current number as string
    """
    curr_num_string = f"{curr_num}"
    match_num_string = f"{match_num}"

    if "." in match_num_string:
        match_decimals = len(match_num_string.split(".")[1])
        curr_num_string = f"{curr_num:.{match_decimals}f}"
        curr_num_string = curr_num_string[:]
        return curr_num_string
    else:
        return f"{int(curr_num)}"


# Format Times
def format_time(timestamp):
    return timestamp.replace(microsecond=0).isoformat()


# Get ISO Times
def get_iso_times():

    # Get timestamps
    date_start_0 = datetime.now()
    date_start_1 = date_start_0 - timedelta(hours=100)
    date_start_2 = date_start_1 - timedelta(hours=100)
    date_start_3 = date_start_2 - timedelta(hours=100)
    date_start_4 = date_start_3 - timedelta(hours=100)

    # Format datetimes
    times_dict = {
        "range _1": {
            "from_iso": format_time(date_start_1),
            "to_iso": format_time(date_start_0),
        },
        "range _2": {
            "from_iso": format_time(date_start_2),
            "to_iso": format_time(date_start_1),
        },
        "range _3": {
            "from_iso": format_time(date_start_3),
            "to_iso": format_time(date_start_2),
        },
        "range _4": {
            "from_iso": format_time(date_start_4),
            "to_iso": format_time(date_start_3),
        }
    }

    # Return result
    return times_dict


def get_accept_price(current_price, side):
    return current_price * 1.05 if side == "BUY" else current_price * 0.95
