from django.shortcuts import render

def indexpage(request):
    return render(request,"index.html")

def aboutuspage(request):
    return render(request,"aboutus.html")

def jobspage(request):
    return render(request,"jobs.html")

def servicespage(request):
    return render(request,"services.html")

def contactuspage(request):
    return render(request,"contactus.html")
