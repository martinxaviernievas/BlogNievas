from django.shortcuts import render, reverse,redirect
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    post = Post.objects.all()
    return render(request, 'templates/index.html', {'post': post})


@login_required
def post_detail(request,post_id):
    post = Post.objects.get(id=post_id)

    comments = post.comments.filter(active=True)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.post = post
            new_form.save()
            return HttpResponseRedirect(reverse('post_detail', args=[post_id]))

    else:
        form = CommentForm

    return render(request, 'templates/post_detail.html', {'post': post, 'comments': comments ,'form':form})

