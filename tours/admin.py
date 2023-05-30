from django.contrib import admin
from .models import Tours, TourProgram, TourProgramSchedule, TourDates, TourCategory


admin.site.register(Tours)
admin.site.register(TourProgram)
admin.site.register(TourProgramSchedule)
admin.site.register(TourDates)
admin.site.register(TourCategory)
