from django.views.generic import ListView
from django.views import View
from .models import Post
from .forms import CommentForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
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


class SinglePostView(View):
    template_name = "blog/post-detail.html"
    model = Post

    def get(self,request,slug):
        post = Post.objects.get(slug = slug)
        context = {
            "posts":post,
            "post_tags": post.caption.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id")
        }
        return render(request,"blog/post-detail.html",context)

    def post(self,request,slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("blog:post-detail-page",args=[slug]))


        #else if form is invalid!
        post = Post.objects.get(slug = slug)
        context = {
            "posts":post,
            "post_tags": post.caption.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id")
        }
        return render(request,"blog/post-detail.html",context)


# class CommentView(FormView):
#     template_name = "post-detail.html"
#     form_class = CommentForm
#     success_url = reverse_lazy('post-detail-page')

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
    


