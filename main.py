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

    week_upcoming, day_upcoming, hour_upcoming \
        = CheckUpcomingAssignments.get_three_major_less_than(assignment_list)

    week_upcoming, day_upcoming, hour_upcoming \
        = tuple(FormatAssignments.format_assignments(assignments)
                for assignments in (week_upcoming, day_upcoming, hour_upcoming)
                )

    upcoming = {
            week_upcoming: "〆切まで1週間以内\n",
            day_upcoming: "【緊急】〆切まで24時間以内\n",
            hour_upcoming: "【大至急】〆切まで1時間以内\n",
            }

    line_api_url = "https://notify-api.line.me/api/notify"

    for uc in upcoming.keys():
        if len(uc) == 0:
            continue
        requests.post(line_api_url,
                      headers={"Authorization": f"Bearer {user.access_token}"},
                      data={"message": f"{upcoming[uc]}\n{uc}"}
                      )


if __name__ == "__main__":
    UserManager.generate_userlist()
    for user in UserManager.get_userlist():
        main(user)

    DEBUG = False if os.environ.get("DEBUG") == "False" else True
    if DEBUG:
        print("Message sent successfully!")
