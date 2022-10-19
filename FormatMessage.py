from typing import Iterable, Union

from ParsePanda.Assignment import Assignment

class FormatAssignments:
    @staticmethod
    def format_assignments(assignments: Union[Assignment, Iterable[Assignment]]) \
        -> Union[Assignment, Iterable[Assignment]]:
        output = ""
        if not hasattr(assignments, "__iter__"):
            assignments = list(assignments)
        for assignment in assignments:
            output += (f"タイトル：{assignment.title}\n"
                    f"期日：{assignment.dueTime.strftime('%m月%d日%H時%M分')}\n"
                    f"説明：{assignment.instructions}\n"
                    f"リンク：{assignment.entityURL}\n"
                    "\n")
        output = output.rstrip("\n")
        return output






