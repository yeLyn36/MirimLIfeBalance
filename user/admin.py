from django.contrib import admin

# Register your models here.
from user.models import Subject, User, Grade, Class

admin.site.register(Subject)
admin.site.register(Grade)
admin.site.register(Class)
admin.site.register(User)