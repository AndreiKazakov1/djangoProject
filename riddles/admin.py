from django.contrib import admin

# Register your models here.
from .models import Option, Riddle
from .models import Message
from .models import Mark

admin.site.register(Riddle)
admin.site.register(Option)
admin.site.register(Message)
admin.site.register(Mark)

