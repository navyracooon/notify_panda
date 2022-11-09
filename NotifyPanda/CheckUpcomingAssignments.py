import datetime
from typing import Iterable, List, Literal, Tuple

from ParsePanda.Assignment import Assignment


class CheckUpcomingAssignments:
    __time_dict = {
        "one_week": datetime.timedelta(days=7),
        "one_day": datetime.timedelta(days=1),
        "one_hour": datetime.timedelta(hours=1),
        }

    @staticmethod
    def get_three_major_less_than(
            assignment_list: Iterable[Assignment], exclusive: bool = True) -> \
            List[Tuple[Assignment]]:
        week_upcoming, day_upcoming, hour_upcoming = tuple(
            CheckUpcomingAssignments.get_less_than(assignment_list, time)
            for time in ["one_week", "one_day", "one_hour"]
            )

        if exclusive:
            week_upcoming = [
                    uc for uc in week_upcoming if uc not in day_upcoming]
            day_upcoming = [
                    uc for uc in day_upcoming if uc not in hour_upcoming]

        return week_upcoming, day_upcoming, hour_upcoming

    @staticmethod
    def get_less_than(
            assignment_list: Iterable[Assignment],
            time: Literal["one_week", "one_day", "one_hour"]) \
            -> List[Assignment]:
        upcoming_list = list()

        for assignment in assignment_list:
            jpn = datetime.timezone(datetime.timedelta(hours=9))
            due = assignment.dueTime.replace(tzinfo=jpn)
            now = datetime.datetime.now(jpn)

            if due - now < datetime.timedelta(0):
                continue
            elif due - now < CheckUpcomingAssignments.__time_dict[time]:
                upcoming_list.append(assignment)

        return upcoming_list
