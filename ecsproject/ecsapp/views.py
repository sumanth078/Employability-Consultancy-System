from django.shortcuts import render, redirect
from .forms import JobSeekerRegistrationForm, RecruiterRegistrationForm, UpdateSeekerForm, UpdateRecruiterForm, \
    PostedJobsForm, SeekerapplyforjobForm, ResumeForm
from .models import JobSeekerRegistration, Admin, RecruiterRegistration, RecruiterPostedJobs
from django.db.models import Q
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def seekerregistrationpage(request):
    form = JobSeekerRegistrationForm()
    if request.method == "POST":
        form = JobSeekerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Successfully Registered"
            return render(request,"seekerlogin.html",{"msg":msg})
        else:
            msg="Registration Failed"
            return render(request, "seekerregistration.html", {"msg":msg})
    return render(request,"seekerregistration.html",{"form":form})

def seekerloginpage(request):
    return render(request,"seekerlogin.html")

def checkseekerlogin(request):
    uname = request.POST["username"]
    pwd=request.POST["password"]

    flag = JobSeekerRegistration.objects.filter( Q(username=uname) & Q(password=pwd))
    print(flag)
    if flag:
        user = JobSeekerRegistration.objects.get(username=uname)
        print(user)
        print(user.id,user.fullname)
        return render(request,"seekerhome.html")
    else:
        msg="Login Failed"
        return render(request,"seekerlogin.html",{"msg":msg})

def seekerhome(request):
    return render(request,"seekerhome.html")

def applypostedjobs(request):
    return HttpResponse('You are successfully applied for this job.')

def seekerjobs(request):
    viewjobslist = RecruiterPostedJobs.objects.all()
    count = RecruiterPostedJobs.objects.count()
    return render(request,"seekerjobs.html",{"viewjobslist":viewjobslist, "count":count})

def seekerlogout(request):
    return render(request,"seekerlogin.html")

def resumepage(request):
    return render(request,"resume.html")

def internshipspage(request):
    return render(request,"internships.html")

def seekercontactpage(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail(
            name,
            message,
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False)
    return render(request, 'seekercontact.html')

def seekeruploadresume(request):
    form2 = ResumeForm()

    if request.method == "POST":
        form2=ResumeForm(request.POST)
        if form2.is_valid():
            form2.save()
            msg = "Resume submitted succesfully"
            return render(request,"seekeruploadresume.html"  ,{"msg":msg})
        else:
            return HttpResponse("Failed to submit")

    return render(request,"seekeruploadresume.html",{"form":form2})

def seekerservicespage(request):
    return render(request,"seekerservices.html")

def seekerjobsbycategory(request):
    return render(request,"seekerjobsbycategory.html")

def seekerprofilepage(request,sid):
    seeker = JobSeekerRegistration.objects.get(id=sid)
    return render(request, "seekerprofile.html", {"seeker": seeker})

def seekerchangepwd(request):
    return render(request,"seekerchangepwd.html")

def seekerdashboard(request):
    return render(request,"seekerdashboard.html")

def seekerapplyforjob(request):
    form = SeekerapplyforjobForm()
    if request.method == "POST":
        formdata = SeekerapplyforjobForm(request.POST,request.FILES)
        if formdata.is_valid():
            formdata.save()
            msg="Job Applied Successfully"
            return render(request, "seekerapplyforjob.html", {"seekerapplyforjobform": form,"msg":msg})
        else:
            msg = "Failed to apply for this Job"
            return render(request, "seekerapplyforjob.html", {"seekerapplyforjobform": form, "msg": msg})
    return render(request,"seekerapplyforjob.html",{"seekerapplyforjobform":form})

def seekerappliedforthejobcount(request):
    countappliedjobs = SeekerapplyforjobForm.objects.all()
    cnt = SeekerapplyforjobForm.objects.count()
    return render(request,"recruitermanagejobs.html",{"countappliedjobs":countappliedjobs,"count":cnt})

def seekerupdatepwd(request):
    opwd=request.POST["opwd"]
    npwd=request.POST["npwd"]

    flag=JobSeekerRegistration.objects.filter(Q(password=opwd))

    if flag:
        JobSeekerRegistration.objects.update(password=npwd)
        msg="password updated successfully"
        return render(request,"seekerchangepwd.html",{"msg":msg})
    else:
        msg = "Old Password is incorrect"
        return render(request,"seekerchangepwd.html",{"msg":msg})

def adminloginpage(request):
    return render(request,"adminlogin.html")

def checkadminlogin(request):
    uname = request.POST["username"]
    pwd = request.POST["password"]

    flag = Admin.objects.filter(Q(username__exact=uname) & Q(password__exact=pwd))
    print(flag)

    if flag:
        admin = Admin.objects.get(username=uname)
        print(admin)
        return render(request, "adminhome.html", {"auname": admin.username})
    else:
        msg = "Login Failed"
        return render(request, "adminlogin.html", {"msg": msg})

def savejobseekercontact(request):
    email = request.POST["email"]

    flag = JobSeekerRegistration.objects.filter(Q(email=email))
    print(flag)

    if flag:
        seeker = JobSeekerRegistration.objects.get(email=email)
        print(seeker)
        return render(request, "seekercontact.html")
    else:
        msg = "Email is not registered"
        return render(request, "seekercontact.html", {"msg": msg})

def viewseekerdata(request):
    seekerlist = JobSeekerRegistration.objects.all()
    count = JobSeekerRegistration.objects.count()
    return render(request,"viewseekerdata.html",{"seekerlist":seekerlist,"count":count})

def viewrecruiterdata(request):
    recruiterlist = RecruiterRegistration.objects.all()
    count = RecruiterRegistration.objects.count()
    return render(request,"viewrecruiterdata.html",{"recruiterlist":recruiterlist,"count":count})

def deleteseeker(request,eid):
    JobSeekerRegistration.objects.filter(id=eid).delete()
    return redirect("viewseekerdata")

def deleterecruiter(request,eid):
    RecruiterRegistration.objects.filter(id=eid).delete()
    return redirect("viewrecruiterdata")

def recruiterregistrationpage(request):
    form = RecruiterRegistrationForm()
    if request.method == "POST":
        form = RecruiterRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Successfully Registered"
            return render(request,"recruiterlogin.html",{"msg":msg})
        else:
            msg="Registration Failed"
            return render(request, "recruiterregistration.html", {"msg":msg})
    return render(request,"recruiterregistration.html",{"form":form})

def recruiterloginpage(request):
    return render(request,"recruiterlogin.html")

def checkrecruiterlogin(request):
    uname = request.POST["username"]
    pwd = request.POST["password"]

    flag = RecruiterRegistration.objects.filter(Q(username__exact=uname) & Q(password__exact=pwd))
    print(flag)

    if flag:
        recruiter = RecruiterRegistration.objects.get(username=uname)
        print(recruiter)
        request.session["auname"] = recruiter.username
        return render(request, "recruiterhome.html", {"auname": recruiter.username})
    else:
        msg = "Login Failed"
        return render(request, "recruiterlogin.html", {"msg": msg})

def recruiterchangepwd(request):
    return render(request,"recruiterchangepwd.html")

def recruiterupdatepwd(request):
    opwd=request.POST["opwd"]
    npwd=request.POST["npwd"]

    flag=RecruiterRegistration.objects.filter(Q(password=opwd))

    if flag:
        RecruiterRegistration.objects.update(password=npwd)
        msg="password updated successfully"
        return render(request,"recruiterchangepwd.html",{"msg":msg})
    else:
        msg = "Old Password is incorrect"
        return render(request,"recruiterchangepwd.html",{"msg":msg})

def postjob(request):
    form = PostedJobsForm()
    if request.method == "POST":
        formdata = PostedJobsForm(request.POST,request.FILES)
        if formdata.is_valid():
            formdata.save()
            msg="Job Posted Successfully"
            return render(request, "postjob.html", {"postedjobform": form,"msg":msg})
        else:
            msg = "Failed to Post Job"
            return render(request, "postjob.html", {"postedjobform": form, "msg": msg})
    return render(request,"postjob.html",{"postedjobform":form})

def recruitermanagejobs(request):
    #countappliedjobs = SeekerapplyforjobForm.objects.all()
    postedjobslist = RecruiterPostedJobs.objects.all()
    count = RecruiterPostedJobs.objects.count()
    return render(request,"recruitermanagejobs.html",{"postedjobslist":postedjobslist,"count":count})

def deletepostedjobs(request,eid):
    RecruiterPostedJobs.objects.filter(id=eid).delete()
    return redirect("recruitermanagejobs")

def adminhomepage(request):
    return render(request, "adminhome.html")

def addrecruiter(request):
    return render(request, "addrecruiter.html")

def updateseeker(request):
    form = UpdateSeekerForm()
    if request.method == "POST":
        formdata = UpdateSeekerForm(request.POST)

        seekerid = formdata.data['id']
        seekerfullname = formdata.data['fullname']
        seekerusername = formdata.data['username']
        seekeremail = formdata.data['email']
        seekerphone = formdata.data['phone']

        flag = JobSeekerRegistration.objects.filter(id=seekerid)

        if flag:
            JobSeekerRegistration.objects.filter(id=seekerid).update(id=seekerid, fullname=seekerfullname, username=seekerusername, email=seekeremail, phone=seekerphone )
            msg="Seeker Updated Successfully"
            return render(request, "updateseeker.html", {"seekerform": form,"msg":msg})
        else:
            msg = "Seeker ID Not Found"
            return render(request, "updateseeker.html", {"seekerform": form, "msg": msg})

    return render(request,"updateseeker.html",{"seekerform":form})


def updaterecruiter(request):
    auname = request.session["auname"]
    form = UpdateRecruiterForm()
    if request.method == "POST":
        formdata = UpdateRecruiterForm(request.POST)

        recruiterid = formdata.data['id']
        recruiterfullname = formdata.data['fullname']
        recruiterusername = formdata.data['username']
        recruiteremail = formdata.data['email']
        recruiterphone = formdata.data['phone']
        recruitercompany = formdata.data['company']
        recruiterrole = formdata.data['role']

        flag = RecruiterRegistration.objects.filter(id=recruiterid)

        if flag:
            RecruiterRegistration.objects.filter(id=recruiterid).update(fullname=recruiterfullname, username=recruiterusername, email=recruiteremail, phone=recruiterphone, company=recruitercompany, role=recruiterrole )
            msg="Recruiter Updated Successfully"
            return render(request, "updaterecruiter.html", {"auname":auname,"recruiterform": form,"msg":msg})
        else:
            msg = "Recruiter ID Not Found"
            return render(request, "updaterecruiter.html", {"auname":auname,"recruiterform": form, "msg": msg})

    return render(request,"updaterecruiter.html",{"auname":auname,"recruiterform":form})

def addseeker(request):
    form = JobSeekerRegistrationForm()
    if request.method == "POST":
        formdata = JobSeekerRegistrationForm(request.POST)
        if formdata.is_valid():
            formdata.save()
            msg="Seeker Added Successfully"
            return render(request, "addseeker.html", {"seekerform": form,"msg":msg})
        else:
            msg = "Failed to Add Seeker"
            return render(request, "addseeker.html", {"seekerform": form, "msg": msg})
    return render(request,"addseeker.html",{"seekerform":form})

def adminlogout(request):
    return render(request,"adminlogin.html")


def recruiterhomepage(request):
    return render(request, "recruiterhome.html")

def newapplicants(request):
    return render(request,"newapplicants.html")

def addcandidate(request):
    return render(request,"addcandidate.html")

def managecandidate(request):
    return render(request,"managecandidate.html")

def searchresume(request):
    return render(request,"searchresume.html")

def addinterview(request):
    return render(request,"addinterview.html")

def interviewlist(request):
    return render(request,"interviewlist.html")

def recruitercontact(request):
    return render(request,"recruitercontact.html")

def recruiterprofile(request):
    return render(request,"recruiterprofile.html")

def recruiterlogout(request):
    return render(request,"recruiterlogin.html")

