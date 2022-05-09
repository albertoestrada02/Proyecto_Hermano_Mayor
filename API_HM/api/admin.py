from django.contrib import admin
from .models import UserT
from .models import Church
from .models import Parameter

# Register your models here.
admin.site.register(UserT)
admin.site.register(Church)
admin.site.register(Parameter)