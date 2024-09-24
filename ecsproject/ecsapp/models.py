from django.db import models

class JobSeekerRegistration(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100,blank=False)
    username = models.CharField(max_length=50,blank=False,unique=True)
    email = models.EmailField(max_length=50,blank=False,unique=True)
    phone = models.BigIntegerField(blank=False, unique=True)
    password = models.CharField(max_length=50, blank=False)
    registrationtime = models.DateTimeField(blank=False,auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "JobSeekerRegistrationTable"

class RecruiterRegistration(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100, blank=False)
    username = models.CharField(max_length=50, blank=False, unique=True)
    email = models.EmailField(max_length=50, blank=False, unique=True)
    phone = models.BigIntegerField(blank=False, unique=True)
    company = models.CharField(max_length=100, blank=False)
    role_choices = (("hr", "HR"), ("teamlead", "TeamLead"), ("manager", "manager"),("employee","Employee"))
    role = models.CharField(blank=False, choices=role_choices, max_length=10)
    password = models.CharField(max_length=50, blank=False)
    registrationtime = models.DateTimeField(blank=False, auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "RecruiterRegistrationTable"

class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50,unique=True,blank=False)
    password = models.CharField(max_length=50,blank=False)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "AdminTable"

class Contactus(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,unique=True,blank=False)
    email = models.EmailField(max_length=50, blank=False, unique=True)
    message = models.CharField(max_length=50,unique=True,blank=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "contactustable"

class Seekerapplyforjob(models.Model):
    id=models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=50,unique=True,blank=False)
    email = models.EmailField(max_length=50, blank=False, unique=True)
    phone = models.BigIntegerField(blank=False, unique=True)

    def __str__(self):
        return self.fullname

    class Meta:
        db_table = "Seekerapplyforjob_table"

class RecruiterPostedJobs(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=False)
    openings = models.PositiveIntegerField(blank=False)
    category_choices = (("fresher", "Fresher Jobs"), ("marketing", "Marketing Jobs"), ("contentwriting", "Content Writing Jobs"), ("hr","HR Jobs"),("datascience","Data Science"))
    category = models.CharField(max_length=100, blank=False,choices=category_choices)
    gender_choices = (("male", "Male"), ("female","Female"), ("all", "All"))
    gender = models.CharField(max_length=100, blank=False, choices=gender_choices)
    description = models.TextField(max_length=200,blank=False)
    contactdetails = models.EmailField(max_length=50, blank=False, unique=True)
    minsalary = models.PositiveIntegerField(blank=False)
    maxsalary = models.PositiveIntegerField(blank=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "RecruiterPostedJobs_table"

class JobsPostedByRecruiter(models.Model):
    recruiter = models.ForeignKey(RecruiterRegistration, on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=False)
    openings = models.PositiveIntegerField(blank=False)
    category_choices = (("fresher", "Fresher Jobs"), ("marketing", "Marketing Jobs"), ("contentwriting", "Content Writing Jobs"), ("hr","HR Jobs"),("datascience","Data Science"))
    category = models.CharField(max_length=100, blank=False,choices=category_choices)
    gender_choices = (("male", "Male"), ("female","Female"), ("all", "All"))
    gender = models.CharField(max_length=100, blank=False, choices=gender_choices)
    description = models.TextField(max_length=200,blank=False)
    contactdetails = models.EmailField(max_length=50, blank=False, unique=True)
    minsalary = models.PositiveIntegerField(blank=False)
    maxsalary = models.PositiveIntegerField(blank=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "JobsPostedByRecruiter_table"

class Resume(models.Model):
    #image = models.FileField(blank=False)
    id=models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50, blank=False)
    lastname = models.CharField(max_length=50, blank=False)
    age = models.PositiveIntegerField(blank=False)
    contact = models.BigIntegerField(blank=False)
    email = models.CharField(max_length=50, blank=False)
    gender_choices = (("M", "Male"), ("F", "Female"),("Others", "Others"))
    gender = models.CharField(max_length=100, blank=False, choices=gender_choices)
    address1 = models.CharField(max_length=300,blank=False)
    city=models.CharField(max_length=100,blank=False)
    state = models.CharField(max_length=200, blank=False)
    postalcode = models.IntegerField(blank=False)
    country = models.CharField(max_length=100, blank=False)
    skills = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.email

    class Meta:
        db_table = "Resume_table"