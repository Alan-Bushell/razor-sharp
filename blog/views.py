from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm

# Create your views here.


class PostList(generic.ListView):
    """Class to return the blog page with posts"""
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/blog.html'
    paginate_by = 6


class PostDetail(View):
    """Class & Method to call the post details pages."""

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """Method to post comments"""

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on")
        username = request.user
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.username = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        template = "blog/post_detail.html"
        context = {
            "post": post,
            "comments": comments,
            "liked": liked,
            "comment_form": CommentForm(),
            "username": username,
        }
        return render(request, template, context)


class PostLike(View):
    """Method to like a post"""
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
