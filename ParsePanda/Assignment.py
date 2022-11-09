from dataclasses import dataclass
import datetime
from typing import Tuple

from ParsePanda.Attachment import Attachment


@dataclass(frozen=True)
class Assignment:
    access: str
    allPurposeItemText: str
    allowPeerAssessment: bool
    allowResubmission: bool
    anonymousGrading: bool
    attachments: Tuple[Attachment]
    author: str
    authorLastModified: str
    closeTime: datetime.datetime
    closeTimeString: str
    # content: None  # Mystery...
    context: str
    creator: str
    draft: bool
    dropDeadTime: datetime.datetime
    dropDeadTimeString: str
    dueTime: datetime.datetime
    dueTimeString: str
    gradeScale: str
    gradeScaleMaxPoints: str
    gradebookItemId: int
    gradebookItemName: str
    # groups: List  # Mystery...
    id: str
    instructions: str
    ltiGradableLaunch: str
    maxGradePoint: str
    modelAnswerText: str
    openTime: datetime.datetime
    openTimeString: str
    position: int
    privateNoteText: str
    section: str
    status: str
    submissionType: str
    timeCreated: datetime.datetime
    timeLastModified: datetime.datetime
    title: str
    entityReference: str
    entityURL: str
    entityId: str
    entityTitle: str
