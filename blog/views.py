from django.shortcuts import render #,redirect
from django.views import generic
from .models import Post

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = 'blog/index.html'
    paginate_by = 6


# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'blog/post_detail.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs) 
#         context['post_list'] = Post.objects.filter(status=1).order_by('-created_on')[:5]
#         return context

# def post_detail(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     return render(request, 'blog/post_detail.html', {'post': post})


 # def delete_post(request, slug):
#     post = get_object_or_404(Post, slug=slug) 
#    if request.method == 'POST':
#       post.delete()
#      return redirect('home')
#   return render(request, 'blog/post_confirm_delete.html', {'post': post})
#   
# def post_detail(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#    if request.method == 'POST':
#       post.delete()
#     return redirect('home')
#   return render(request, 'blog/post_detail.html', {'post': post})
# 

# 
# def post_detail(request, slug):
#   post = get_object_or_404(Post, slug=slug)
# if request.method == 'POST':
#   post.delete()   