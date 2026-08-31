from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from datetime import date
from django.views.generic import ListView,DetailView
from .models import Post
# Create your views here.



def get_date(post):
    return post['date']


class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"] #order the posts by date
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]  # give only 3 posts
        return data


class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = 'all_posts'


class SinglePostView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["caption"] = self.object.caption.all()
        return context