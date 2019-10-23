from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(DilemmaModel)
# admin.site.register(Reason)\
class DilemmaAdmin(admin.ModelAdmin):
    readonly_fields = ('created_date',)

admin.site.register(Dilemma, DilemmaAdmin)
admin.site.register(DilemmaPartOne)
admin.site.register(DilemmaPartTwo)
admin.site.register(ReasonPartOne)
admin.site.register(ReasonPartTwo)

