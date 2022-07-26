"""
https://www.youtube.com/watch?v=kbwk1Tw3OhE

Given 2 calendars, find the open meeting times of the 2 calendars.
Calendars are a list of lists (or tuples). 
    Inner lists are comprised of a start time and an end time

Calendars also have working hours where 
meetings cannot be scheduled outside of working hours


Took me 62 mins with a few interuptions to solve
"""

from dataclasses import dataclass


@dataclass
class Calendar:
    meeting_times: list
    working_hours: list


def find_open_times(calendar: Calendar) -> list:
    my_day_including_bounds = calendar.meeting_times.copy()
    my_day_including_bounds.insert(0, ["0:00", calendar.working_hours[0]])
    my_day_including_bounds.append([calendar.working_hours[1], "0:00"])
    return [
        [meeting[1], my_day_including_bounds[idx + 1][0]]
        for idx, meeting in enumerate(my_day_including_bounds[:-1])
        if meeting[1] != my_day_including_bounds[idx + 1][0]
    ]


def parse_string_times_to_floats(times: list) -> list:
    t1_hour, t1_min = times[0].split(":")
    t2_hour, t2_min = times[1].split(":")
    times = [int(x) for x in [t1_hour, t1_min, t2_hour, t2_min]]
    return times[0] + (times[1] / 60), times[2] + (times[3] / 60)


def parse_float_times_to_string(times: float) -> str:
    hours, min = str(times).split(".")
    return f"{hours}:{float(min)*6:.0f}"


def find_meeting_time(
    calendar1: Calendar, calendar2: Calendar, meeting_length: int = 0
) -> list:
    """_summary_

    1. find open windows (no meetings) of each calendar
    2. parse openings from strings to floats for comparison
    3. Compare the windows of each calendar to see shared open times
    4. Compare the length of the openings to our meeting length
        - make sure it is >= meeting length
    5. Save start and end times that meet all above requirements to a list
        - convert the floats back to strings for output

    Args:
        calendar1 (Calendar): first person's calendar obj
        calendar2 (Calendar): second person's calendar obj
        meeting_length (int): how long the meeting will be

    Returns:
        list[list[str,str]]: open times are returned in the same format of Calendar.times
    """
    c1_openings = find_open_times(calendar1)
    c2_openings = find_open_times(calendar2)

    open_times = []

    for c1 in c1_openings:
        for c2 in c2_openings:
            # parse the strings to get float values to represent time
            c1time_start, c1time_end = parse_string_times_to_floats(c1)
            c2time_start, c2time_end = parse_string_times_to_floats(c2)

            # if the first opening start time is later than the second period end time we can skip
            # same is true of the inverse second period start time to the first period end time
            if c1time_start >= c2time_end or c2time_start >= c1time_end:
                continue

            # if the start time of either the 1st or 2nd opening is between the other opening
            # we have a open calendar spot and can mark the opening
            if (
                c2time_start <= c1time_start < c2time_end
                or c1time_start <= c2time_start < c1time_end
            ):
                # we have found an opening, save the start and end times
                meeting_start = max(c1time_start, c2time_start)
                meeting_end = min(c1time_end, c2time_end)
                # now we check if that meeting is long enough
                if meeting_end - meeting_start >= meeting_length / 60:
                    # if all conditions are met, we add the time to a list
                    # after we convert back to a string
                    open_times.append(
                        [
                            parse_float_times_to_string(meeting_start),
                            parse_float_times_to_string(meeting_end),
                        ]
                    )

    return open_times


def main():
    jace = Calendar(
        [
            ["9:00", "10:30"],
            ["12:00", "13:00"],
            ["16:00", "18:00"],
        ],
        ["9:00", "20:00"],
    )
    tim = Calendar(
        [
            ["10:00", "11:30"],
            ["12:30", "14:30"],
            ["14:30", "15:00"],
            ["16:00", "17:00"],
        ],
        ["10:00", "18:30"],
    )
    avalible_times = find_meeting_time(jace, tim, 15)
    print(avalible_times)
