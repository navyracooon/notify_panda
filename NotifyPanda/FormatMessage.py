from typing import Iterable, Union

from ParsePanda.Assignment import Assignment


class FormatAssignments:
    @staticmethod
    def format_assignments(
            assignments: Union[Assignment, Iterable[Assignment]]) \
            -> list[str]:
        output = []
        if not hasattr(assignments, "__iter__"):
            assignments = list(assignments)
        for assignment in assignments:
            output.append(f"タイトル：{assignment.title}\n"
                          f"期日：{assignment.dueTime.strftime('%m月%d日%H時%M分')}\n"
                          f"説明：{assignment.instructions}\n"
                          "リンク：https://panda.ecs.kyoto-u.ac.jp/portal/site/"
                          f"{assignment.context}")
        return output
