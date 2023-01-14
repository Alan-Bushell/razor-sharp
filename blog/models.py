from django.db import models
from django.contrib.auth.models import User
from accounts.models import Account, UserProfile


# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """Blog post model"""
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(Account, on_delete=models.CASCADE,
                               related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = models.ImageField(blank=True, upload_to='blogimages')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(choices=STATUS, default=0)
    likes = models.ManyToManyField(Account,
                                   related_name='blogpost_like',
                                   blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """User comment model"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    username = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.username.username}"
