from django.contrib import admin

# Register your models here.
from .models import Trainer
from .models import Trainees
admin.site.register(Trainer)
admin.site.register(Trainees)
