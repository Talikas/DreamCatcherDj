from django.contrib import admin
from .models import User, Dream, Sleep, People, QuestionnaireEntry


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'password', 'level']


admin.site.register(User, UserAdmin)
admin.site.register(Dream)
admin.site.register(Sleep)
admin.site.register(QuestionnaireEntry)
admin.site.register(People)