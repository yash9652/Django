from django.shortcuts import redirect, render , get_object_or_404
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    return render(request,'blog/post_list.html',{"posts":posts})



def post_details(request,slug):
    post = get_object_or_404(Post,slug=slug)
    print(post.content)
    return render(request,"blog/post_detail.html",{"post":post})


def post_add(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("post_list")
    else:
        form = PostForm()
    return render(request,"blog/post_add.html",{"form":form})

