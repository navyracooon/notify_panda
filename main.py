import os

import requests

from NotifyPanda.CheckUpcomingAssignments import CheckUpcomingAssignments
from NotifyPanda.FormatMessage import FormatAssignments
from NotifyPanda.UserManager import UserManager
from ParsePanda.PandaParser import PandaParser
from ParsePanda.User import User


def main(user: User):
    PandaParser.set_user(user)
    assignment_list = PandaParser.parse_all_assignment_info()
    PandaParser.logout_panda()

    week_upcoming, day_upcoming, hour_upcoming \
        = CheckUpcomingAssignments.get_three_major_less_than(assignment_list)

    week_upcoming, day_upcoming, hour_upcoming \
        = tuple(FormatAssignments.format_assignments(assignments)
                for assignments in (week_upcoming, day_upcoming, hour_upcoming)
                )

    upcoming = {
            " 1週間以内": week_upcoming,
            " 24時間以内": day_upcoming,
            " 1時間以内": hour_upcoming,
            }

    line_api_url = "https://notify-api.line.me/api/notify"

    for title, outputs in upcoming.items():
        if len(outputs) == 0:
            continue
        for index, output in enumerate(outputs):
            if index == 0:
                requests.post(
                    line_api_url,
                    headers={"Authorization": f"Bearer {user.access_token}"},
                    data={"message": f"\n⎯⎯⎯⎯ {title}⎯⎯⎯⎯⎯"}
                    )
            requests.post(
                line_api_url,
                headers={"Authorization": f"Bearer {user.access_token}"},
                data={"message": f"\n{output}"}
                )
            if index == len(outputs) - 1:
                requests.post(
                    line_api_url,
                    headers={"Authorization": f"Bearer {user.access_token}"},
                    data={"message": f"\n⎯⎯⎯⎯ {title}⎯⎯⎯⎯⎯"}
                    )


if __name__ == "__main__":
    UserManager.generate_userlist()
    for user in UserManager.get_userlist():
        main(user)

    DEBUG = False if os.environ.get("DEBUG") == "False" else True
    if DEBUG:
        print("Message sent successfully!")
