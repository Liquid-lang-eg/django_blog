from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.utils.timezone import now
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



# def post_list(request):
#     posts = Post.objects.all().order_by('-pub_date')
#     return render(request, 'posts/post_list.html', {'posts': posts})
class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name = "posts"

# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     comments = post.comments_post.filter(parent=None)
#     return render(request, 'posts/post_detail.html', {'post': post, 'comments': comments})

class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"

# def add_post(request):
#
#     if not request.user.is_authenticated:
#         return redirect('user:sign_in')
#
#     if request.method == 'POST':
#         form = PostForm(data=request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.user = request.user
#             form.save()
#             return redirect('blog:post_list')
#     else:
#         form = PostForm
#
#     return render(request, 'posts/add_post.html', {'form': form})

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "posts/add_post.html"
    success_url = reverse_lazy("user:sign_in")
    fields = ['title', 'text',]
    login_url = 'user:sign_in'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# def add_comment(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     if not request.user.is_authenticated:
#         return redirect('user:sign_in')
#
#     if request.method == 'POST':
#         form = CommentForm(data=request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.user = request.user
#             comment.Post = post
#
#             parent_id = request.POST.get('parent_id')
#             if parent_id:
#                 parent_comment = get_object_or_404(Comment, id=parent_id)
#                 comment.parent = parent_comment
#             form.save()
#             return redirect('blog:post_detail', pk=pk)
#     else:
#         form = CommentForm
#
#     return render(request, 'posts/add_post.html', {'post': post, 'form': form})
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'posts/add_post.html'
    login_url = 'user:sign_in'
    fields = ['content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.Post = get_object_or_404(Post, pk=self.kwargs['pk'])
        parent_id = self.request.POST.get('parent_id')
        if parent_id:
            form.instance.parent = get_object_or_404(Comment, id=parent_id)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.object.Post.pk})
# def edit_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     if not request.user.is_authenticated:
#         return redirect('user:sign_in')
#
#     if post.user != request.user:
#         return redirect('blog:post_list')
#
#     if request.method == 'POST':
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.if_edited = True
#             post.edited_at = now()
#             form.save()
#             return redirect('blog:post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'posts/edit_post.html', {'form': form, 'post': post})

class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'posts/edit_post.html'
    success_url = reverse_lazy('blog:post_list')
    fields = ['title', 'text']
    login_url = 'user:sign_in'

    def form_valid(self, form):
        form.instance.edited_at = now()
        form.instance.if_edited = True
        form.instance.user = self.request.user
        return super().form_valid(form)

# def delete_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     if not request.user.is_authenticated:
#         return redirect('user:sign_in')
#
#     if post.user != request.user:
#         return redirect('blog:post_list')
#
#     if request.method == 'POST':
#         post.delete()
#         return redirect('blog:post_list')
#
#     return render(request, 'posts/confirm_delete.html', {'post': post})

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'posts/confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')
    login_url = 'user:sign_in'

