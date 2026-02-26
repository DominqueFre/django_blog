from django.shortcuts import render, get_object_or_404 #,redirect
from django.views import generic
from .models import Post

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = 'blog/index.html'
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.
    **Context**
    ``post``
        An instance of :model:`blog.Post`.
    **Template:**
    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )


# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'blog/post_detail.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs) 
#         context['post_list'] = Post.objects.filter(status=1).order_by('-created_on')[:5]
#         return context


 # def delete_post(request, slug):
#     post = get_object_or_404(Post, slug=slug) 
#    if request.method == 'POST':
#       post.delete()
#      return redirect('home')
#   return render(request, 'blog/post_confirm_delete.html', {'post': post})
