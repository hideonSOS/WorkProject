from django.contrib import admin
from .models import test_database1
from .models import test_database2

admin.site.register(test_database1)
admin.site.register(test_database2)