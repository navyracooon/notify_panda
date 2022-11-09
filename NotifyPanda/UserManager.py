import os
import sqlite3
from typing import Literal

from dotenv import load_dotenv

from ParsePanda.User import User


class UserManager:
    __userlist: list[User] = list()
    __database: Literal["dotenv", "sqlite"] = None

    @staticmethod
    def generate_userlist() -> None:
        load_dotenv(".env")
        UserManager.__database = "sqlite" if (
                os.getenv("DATABASE") == "sqlite") else "dotenv"
        if UserManager.__database == "dotenv":
            UserManager.__userlist = [
                    User(username=os.getenv("USERNAME"),
                         password=os.getenv("PASSWORD"),
                         access_token=os.getenv("ACCESS_TOKEN"))]
        else:
            db_connection = sqlite3.connect("notify_panda.db")
            db_cursor = db_connection.cursor()
            users_raw = db_cursor.execute("SELECT * FROM users").fetchall()
            db_connection.close()

            UserManager.__userlist = [
                    User(user[0], user[1], user[2]) for user in users_raw]

    @staticmethod
    def get_userlist() -> list[User]:
        return UserManager.__userlist
