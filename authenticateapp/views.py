from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import datetime
import base64

# Create your views here.
def home(request):
    return render(request, "index.html")


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")
        if pass1 != pass2:
            messages.error(request, "Password does not match")
        newuser = User.objects.create_user(
            username=username, email=email, password=pass1
        )
        newuser.first_name = fname
        newuser.last_name = lname
        newuser.save()
        messages.success(request, "Welcome to the YouBlog, registered!!")
        return redirect("home")
    else:
        return HttpResponse("404 error")


def userlogin(request):
    if request.method == "POST":
        logname = request.POST["logname"]
        logpass = request.POST["logpass"]

        user = authenticate(username=logname, password=logpass)

        if user is not None:
            login(request, user)
            messages.success(request, "successfuly logged in")
            return redirect("home")
        else:
            messages.error(
                request,
                "Invalid  User name or Passwoord, Or you are not registered Yet",
            )
            return redirect("home")
    else:
        return HttpResponse("404")


def userlogout(request):
    logout(request)
    messages.success(request, "successfuly logged out!")
    return redirect("home")


def search(request):
    query = request.GET["query"]
    allblogs = Writeblog.objects.none()
    allblogstopic = Writeblog.objects.filter(blogtopic__icontains=query)
    allblogscontent = Writeblog.objects.filter(blogpost__icontains=query)
    allblogs = allblogstopic.union(allblogscontent)

    prams = {"allblogs": allblogs, "query": query}
    return render(request, "search.html", prams)

def base(request):
    return render(request, "base.html")