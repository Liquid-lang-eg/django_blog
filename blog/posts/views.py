from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.utils.timezone import now


def post_list(request):
    posts = Post.objects.all().order_by('-pub_date')
    return render(request, 'posts/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments_post.filter(parent=None)
    return render(request, 'posts/post_detail.html', {'post': post, 'comments': comments})


def add_post(request):

    if not request.user.is_authenticated:
        return redirect('user:sign_in')

    if request.method == 'POST':
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            form.save()
            return redirect('blog:post_list')
    else:
        form = PostForm

    return render(request, 'posts/add_post.html', {'form': form})


def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if not request.user.is_authenticated:
        return redirect('user:sign_in')

    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.Post = post

            parent_id = request.POST.get('parent_id')
            if parent_id:
                parent_comment = get_object_or_404(Comment, id=parent_id)
                comment.parent = parent_comment
            form.save()
            return redirect('blog:post_detail', pk=pk)
    else:
        form = CommentForm

    return render(request, 'posts/add_post.html', {'post': post, 'form': form})


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if not request.user.is_authenticated:
        return redirect('user:sign_in')

    if post.user != request.user:
        return redirect('blog:post_list')

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.if_edited = True
            post.edited_at = now()
            form.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/edit_post.html', {'form': form, 'post': post})

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if not request.user.is_authenticated:
        return redirect('user:sign_in')

    if post.user != request.user:
        return redirect('blog:post_list')

    if request.method == 'POST':
        post.delete()
        return redirect('blog:post_list')

    return render(request, 'posts/confirm_delete.html', {'post': post})