from django.contrib import admin
from .models import Report
from .models import User
from .models import Tweet

admin.site.register(Report)
admin.site.register(User)
admin.site.register(Tweet)