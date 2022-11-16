from django.contrib import admin
from .models import Note, Day, Month

admin.site.register(Month)
admin.site.register(Day)
admin.site.register(Note)

# Register your models here.
