from django.contrib import admin
from .models import EmailModel
# Register your models here.
class EmailAdmin(admin.ModelAdmin):
    list_display = ['Email','Message']

admin.site.register(EmailModel,EmailAdmin)
