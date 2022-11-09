import argparse
import os
import sqlite3

from dotenv import load_dotenv


class DBManager:
    @staticmethod
    def add_user(username: str, password: str, access_token: str) -> None:
        if not os.path.isfile("notify_panda.db"):
            DBManager.initialize_database()
        db_connection = sqlite3.connect("notify_panda.db")
        db_cursor = db_connection.cursor()
        db_cursor.execute("INSERT INTO users VALUES (?,?,?)",
                          (username, password, access_token))
        db_connection.commit()
        db_connection.close()

    @staticmethod
    def initialize_database() -> None:
        load_dotenv(".env")
        db_connection = sqlite3.connect("notify_panda.db")
        db_cursor = db_connection.cursor()
        db_cursor.execute("CREATE TABLE users"
                          "(username text, password text, access_token text)")
        db_connection.commit()
        db_connection.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description="Input USERNAME, PASSWORD, ACCESS_TOKEN in order")
    parser.add_argument("username", type=str)
    parser.add_argument("password", type=str)
    parser.add_argument("access_token", type=str)
    args = parser.parse_args()
    DBManager.add_user(args.username, args.password, args.access_token)
