from django.db import models

from user.models import Subject, User, Grade, Class


class Event(models.Model):
    num = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='event_subjects', null=False)
    teacher_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_names', null=False)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='event_grades', null=False)
    classes = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='event_classes', null=False)
    start_date = models.DateField(null=False)
    finish_date = models.DateField(null=False)

    def __str__(self):
        return f'{self.name}'


