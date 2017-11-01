from django.db import models
from djchoices import DjangoChoices, ChoiceItem
from miscellaneous.models import TimeStampMixin

class AttendenceChoices(DjangoChoices):
    PRESENT = ChoiceItem("P")
    ABSENT = ChoiceItem("A")
    LEAVE = ChoiceItem("L")


class Student(TimeStampMixin):
    """
        Student Model
    """
    user = models.ForeignKey("authentication.User")

    class Meta:
        app_label = "attendence"


class Attendence(TimeStampMixin):
    """
        Attendence Model
    """
    student = models.ForeignKey("attendence.Student")
    date = models.DateField()
    status = models.CharField(max_length=1, choices=AttendenceChoices.choices)

    class Meta:
        app_label = "attendence"
        unique_together = ('student', 'date')
