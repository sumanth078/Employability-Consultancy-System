from django.contrib import admin
from .models import JobSeekerRegistration, Admin, RecruiterRegistration, Contactus, RecruiterPostedJobs, Resume

admin.site.register(JobSeekerRegistration)
admin.site.register(RecruiterRegistration)
admin.site.register(Admin)
admin.site.register(Contactus)
admin.site.register(RecruiterPostedJobs)
admin.site.register(Resume)