from django.shortcuts import render, get_object_or_404 #,redirect
from django.views import generic
from django.contrib import messages
# from requests import post 
from .models import Post
from .forms import CommentForm
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
    comments = post.comments.all().order_by("-created_onc")
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.commenter = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Comment submitted, now awaiting approval.")
    comment_form = CommentForm()
    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        }
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
