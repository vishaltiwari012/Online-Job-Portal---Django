from django.contrib import admin
from . models import Login,JobSeeker,Recruiter,Enquiry,Jobs,Apply,News

# Register your models here.
admin.site.register(Login)
admin.site.register(JobSeeker)
admin.site.register(Recruiter)
admin.site.register(Enquiry)
admin.site.register(Jobs)
admin.site.register(Apply)
admin.site.register(News)
