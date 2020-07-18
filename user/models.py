from django.db import models


class Subject(models.Model):
    subject = models.CharField(primary_key=True, max_length=30, null=False)

    def __str__(self):
        return f'{self.subject}'


class Grade(models.Model):
    grade = models.IntegerField(primary_key=True, null=False)

    def __str__(self):
        return f'{self.grade}'


class Class(models.Model):
    classes = models.IntegerField(primary_key=True, null=False)

    def __str__(self):
        return f'{self.classes}'


class User(models.Model):
    name = models.CharField(max_length=10, null=False)
    id = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=30, null=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='user_subjects')
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='user_grades')

    USERNAME_FIELD = 'id'  # email을 사용자의 식별자로 설정
    REQUIRED_FIELDS = '__all__'  # 필수입력값

    def __str__(self):
        return f'{self.name}'

    def get_subjects_list(self):
        subjects = Subject.objects.filter().order_by('subject')
        return subjects

    def get_grades_list(self):
        grades = Grade.objects.filter().order_by('grade')
        return grades
