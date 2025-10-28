from django.contrib import admin
from testapp.models import Hydjobs,Banglorejobs,Punejobs
# Register your models here.
class HydjobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(Hydjobs,HydjobsAdmin)
class BanglorejobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(Banglorejobs,BanglorejobsAdmin)
class PunejobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(Punejobs,PunejobsAdmin)