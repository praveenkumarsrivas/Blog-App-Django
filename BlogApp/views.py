from django.shortcuts import render, redirect
from django.contrib import messages
import datetime
from BlogApp.models import Contact, Writeblog
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import PIL
from PIL import Image
from django.contrib.auth.models import User
# from .forms import ImageForm

# def upload_image(request):
#     """Process images uploaded by users"""
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             img_obj = form.instance
#             return render(request, 'write.html', {
#                 'form': form,
#                 'img_obj': img_obj
#             })
#     else:
#         form = ImageForm()
#     return render(request, 'write.html', {'form': form})


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        notes = request.POST.get("notes")
        time = datetime.datetime.now()
        if len(notes) <= 20:
            messages.error(
                request, "Your message should be longer than 20 characters!")
        else:
            con = Contact(name=name, email=email, notes=notes, time=time)
            con.save()
            messages.success(
                request, "Thank you for contacting! We will be back soon!")
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def writeblog(request, ):
    if request.method == "POST":
        author = request.POST.get("author")
        email = request.POST.get("email")
        blogtopic = request.POST.get("blogtopic")
        summary = request.POST.get("summary")
        avatar = request.POST.get("avatar")
        blogpost = request.POST.get("blogpost")
        readtime = (len(blogpost)) // 300
        submitdate = datetime.datetime.now()
        if len(blogpost) > 100:
            newblogpost = Writeblog(
                author=author,
                email=email,
                blogtopic=blogtopic,
                summary=summary,
                avatar=avatar,
                blogpost=blogpost,
                readtime=readtime,
                submitdate=submitdate,
            )
            newblogpost.save()
            messages.success(
                request,
                "your Blog posted Successfully, Please wait for some time to get approve from the Admin!!",
            )
            return render(request, "write.html")
        else:
            messages.error(request, "Blog Post can not be less then 100 words")
    return render(request, "write.html")


def read(request):
    allblogs = Writeblog.objects.all()
    content = {"allblogs": allblogs}
    return render(request, "read.html", content)


def readmore(request):
    allblogs = Writeblog.objects.all()
    content = {"allblogs": allblogs}
    # for blog in allblogs:
    #     if blog.blogtopic == topic:
    #         blogsend = blog.blogtopic
    #         content = {"blogsend": blogsend}
    #         return render(request, "readmore.html", content)
    return render(request, "read.html", content)


def userlogout(request):
    logout(request)
    messages.success(request, "successfuly logged out!")
    return redirect("home")


def search(request):
    query = request.GET["query"]
    if len(query) > 20:
        allblogs = Writeblog.objects.none()
    else:
        allblogstopic = Writeblog.objects.filter(blogtopic__icontains=query)
        allblogscontent = Writeblog.objects.filter(blogpost__icontains=query)
        allblogs = allblogstopic.union(allblogscontent)
    if allblogs.count() == 0:
        messages.warning(request, "no result found")

    prams = {"allblogs": allblogs, "query": query}
    return render(request, "search.html", prams)
