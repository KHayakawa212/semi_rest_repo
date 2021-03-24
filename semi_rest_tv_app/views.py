from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Show

#redirect to home page (shows)
def index(request):
    return redirect("/shows")

#********** RENDER METHODS **********
# Home Page (shows)
def get_shows(request):
    context = {
        "all_shows": Show.objects.all()
    }
    return render(request, "shows.html", context)

# Create Page (add new show)
def get_new_show(request):
    return render(request, "new_show.html")

# Update Page (edit existing show)
def get_edit_show(request, id):
    context = {
        "this_show": Show.objects.get(id=id)
    }
    return render(request, "edit_show.html", context)

# Show Details Page
def get_show_details(request, id):
    context = {
        "this_show": Show.objects.get(id=id)
    }
    return render(request, "show_details.html", context)

#********** LOGIC/CONTROL METHODS **********

#Post new show to database - redirect("/shows/<id>")
def post_new_show(request):
    errors = Show.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/new")
    else:
        new_show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])
        id = new_show.id
        return redirect(f"/shows/{id}")

#Post update specific show in database - redirect("/shows/<id>")
def post_update(request, id):
    errors = Show.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/shows/{id}/edit")
    else:
        this_show = Show.objects.get(id=id)
        print(request.POST['release_date'])
        if request.POST['title'] != this_show.title:
            this_show.title=request.POST['title']
            this_show.save()
        if request.POST['network'] != this_show.network:
            this_show.network=request.POST['network']
            this_show.save()
        if request.POST['release_date'] != this_show.release_date:
            this_show.release_date=request.POST['release_date']
            this_show.save()
        if request.POST['description'] != this_show.description:
            this_show.description=request.POST['description']
            this_show.save()
        return redirect(f"/shows/{id}")

#Post delete specific show from database - redirect("/shows")
def post_delete(request, id):
    show_delete = Show.objects.get(id=id).delete()
    return redirect("/")