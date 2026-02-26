from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import About

# Create your views here.


class AboutList(generic.ListView):

    queryset = About.objects.all()
    template_name = 'about/about.html'
    paginate_by = 1


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
