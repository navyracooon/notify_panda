import datetime
import json
import os

from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
from typing import Dict, List

from ParsePanda.Attachment import Attachment
from ParsePanda.Assignment import Assignment


class PandaParser:
    __logged_in = False
    __session = requests.session()

    @staticmethod
    def parse_all_assignment_info() -> List[Assignment]:
        request_dicts = PandaParser.get_all_assignment_info()["assignment_collection"]
        assignment_list = [
                Assignment(
                    access = request_dict["access"],
                    allPurposeItemText = request_dict["allPurposeItemText"],
                    allowPeerAssessment = request_dict["allowPeerAssessment"],
                    allowResubmission = request_dict["allowResubmission"],
                    anonymousGrading = request_dict["anonymousGrading"],
                    attachments = tuple(
                        Attachment(
                            name = attachment["name"], 
                            ref = attachment["name"],
                            size = attachment["size"], 
                            type = attachment["type"],
                            url = attachment["url"]
                            )
                        for attachment in request_dict["attachments"]
                        ),
                    author = request_dict["author"],
                    authorLastModified = request_dict["authorLastModified"],
                    closeTime = datetime.datetime.fromtimestamp(
                        request_dict["closeTime"]["epochSecond"]),
                    closeTimeString = request_dict["closeTimeString"],
                    # content = request_dict["content"],  # Mystery
                    context = request_dict["context"],
                    creator = request_dict["creator"],
                    draft = request_dict["draft"],
                    dropDeadTime = datetime.datetime.fromtimestamp(
                        request_dict["dropDeadTime"]["epochSecond"]),
                    dropDeadTimeString = request_dict["dropDeadTimeString"],
                    dueTime = datetime.datetime.fromtimestamp(
                        request_dict["dueTime"]["epochSecond"]),
                    dueTimeString = request_dict["dueTimeString"],
                    gradeScale = request_dict["gradeScale"],
                    gradeScaleMaxPoints = request_dict["gradeScaleMaxPoints"],
                    gradebookItemId = request_dict["gradebookItemId"],
                    gradebookItemName = request_dict["gradebookItemName"],
                    # groups = request_dict["groups"],  # Mystery
                    id = request_dict["id"],
                    instructions = BeautifulSoup(request_dict["instructions"], "html.parser").text,
                    ltiGradableLaunch = request_dict["ltiGradableLaunch"],
                    maxGradePoint = request_dict["maxGradePoint"],
                    modelAnswerText = request_dict["modelAnswerText"],
                    openTime = request_dict["openTime"],
                    openTimeString = request_dict["openTimeString"],
                    position = request_dict["position"],
                    privateNoteText = request_dict["privateNoteText"],
                    section = request_dict["section"],
                    status = request_dict["status"],
                    submissionType = request_dict["submissionType"],
                    timeCreated = datetime.datetime.fromtimestamp(
                        request_dict["timeCreated"]["epochSecond"]),
                    timeLastModified = datetime.datetime.fromtimestamp(
                        request_dict["timeLastModified"]["epochSecond"]),
                    title = request_dict["title"],
                    entityReference = request_dict["entityReference"],
                    entityURL = request_dict["entityURL"],
                    entityId = request_dict["entityId"],
                    entityTitle = request_dict["entityTitle"],
                )
                for request_dict in request_dicts
            ]
        return assignment_list

    @staticmethod
    def get_all_assignment_info() -> Dict:
        PandaParser.login_panda()
        all_assignment_info_url = "https://panda.ecs.kyoto-u.ac.jp/direct/assignment/my.json"
        request = PandaParser.__session.get(all_assignment_info_url)
        request_dicts = request.json()
        return request_dicts

    @staticmethod
    def login_panda() -> None:
        if not PandaParser.__logged_in:
            login_url = (
                "https://panda.ecs.kyoto-u.ac.jp/cas/login"
                "?service=https%3A%2F%2Fpanda.ecs.kyoto-u.ac.jp%2Fsakai-login-tool%2Fcontainer"
            )

            # !! TEMP !! #
            # THIS WILL BE REMOVED BY CREATING "UserManager.py"
            load_dotenv("ParsePanda/.env")
            username = os.environ.get("USERNAME")
            password = os.environ.get("PASSWORD")

            bf = PandaParser.__session.get(login_url)
            soup = BeautifulSoup(bf.text, "html.parser")

            raw_lt = soup.select("#fm1 > div.row.btn-row > input[type=hidden]:nth-of-type(1)")
            lt = raw_lt[0].attrs["value"]

            raw_execution = soup.select("#fm1 > div.row.btn-row > input[type=hidden]:nth-of-type(2)")
            execution = raw_execution[0].attrs["value"]

            PandaParser.__session.post(
                url = login_url,
                data = {
                "username": username,
                "password": password,
                "lt": lt,
                "execution": execution,
                "_eventId": "submit",
                }
            )

            PandaParser.__logged_in = True

if __name__ == "__main__":
    PandaParser.get_all_assignment_info()
