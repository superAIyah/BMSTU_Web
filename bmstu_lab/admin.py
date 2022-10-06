from django.contrib import admin

from .models import Articles, Autors, Subjects
admin.site.register(Autors)
admin.site.register(Articles)
admin.site.register(Subjects)
# Register your models here.
