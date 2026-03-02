from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib import messages
# from urllib3 import request
from .models import About
from .forms import CollaborateForm
# Create your views here.


class AboutList(generic.ListView):

    queryset = About.objects.all()
    about= About.objects.all().order_by('-created_on').first()

    template_name = "about/about.html"
    collaborate_form = CollaborateForm()

def collaborate(request):

    about = About.objects.all().order_by('-created_on').first()
    collaborate_form = CollaborateForm()

    
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)

        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Collaboration request submitted successfully!")

    about = About.objects.all().order_by('-created_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form,
        }
        )

# def about_detail(request):
#     """
#     Display an individual :model:`about.About`.
#     **Context**
#     ``about``
#         An instance of :model:`about.About`.
#     **Template:**
#     :template:`about/about_detail.html`
#     """

#     queryset = About.objects.all()
#     about = get_object_or_404(queryset,)

#     return render(
#         request,
#         "about/about_detail.html",
#         {"about": about},
#     )
