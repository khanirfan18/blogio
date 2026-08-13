from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
# Create your views here.

all_posts = [
    {
        "slug":"hike-in-the-mountains",
        "image":"mt.webp",
        "author":"irfan",
        "date": date(2026,8,13),
        "title": "Mountain Hiking",
        "excerpt": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Cum totam sunt illo deserunt quod vitae voluptatum facere, nulla, molestias dignissimos reiciendis ipsum quidem accusantium error pariatur eos? Facere, officia esse.",
        "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Cum totam sunt illo deserunt quod vitae voluptatum facere, nulla, molestias dignissimos reiciendis ipsum quidem accusantium error pariatur eos? Facere, officia esse.Lorem ipsum dolor sit amet consectetur adipisicing elit. Cum totam sunt illo deserunt quod vitae voluptatum facere, nulla, molestias dignissimos reiciendis ipsum quidem accusantium error pariatur eos? Facere, officia esse."
    },
    {
        "slug":"sunset-at-the-beach",
        "image":"pepebeach.webp",
        "author":"irfan",
        "date": date(2026,8,10),
        "title": "Sunset at the Beach",
        "excerpt": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Cum totam sunt illo deserunt quod vitae voluptatum facere, nulla, molestias dignissimos reiciendis ipsum quidem accusantium error pariatur eos? Facere, officia esse.",
        "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Cum totam sunt illo deserunt quod vitae voluptatum facere, nulla, molestias dignissimos reiciendis ipsum quidem accusantium error pariatur eos? Facere, officia esse.Lorem ipsum dolor sit amet consectetur adipisicing elit. Cum totam sunt illo deserunt quod vitae voluptatum facere, nulla, molestias dignissimos reiciendis ipsum quidem accusantium error pariatur eos? Facere, officia esse."
    },
    {
        "slug":"exploring-the-forest",
        "image":"pepeforest.webp",
        "author":"irfan",
        "date": date(2026,8,5),
        "title": "Exploring the Forest",
        "excerpt": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Cum totam sunt illo deserunt quod vitae voluptatum facere, nulla, molestias dignissimos reiciendis ipsum quidem accusantium error pariatur eos? Facere, officia esse.",
        "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Cum totam sunt illo deserunt quod vitae voluptatum facere, nulla, molestias dignissimos reiciendis ipsum quidem accusantium error pariatur eos? Facere, officia esse.Lorem ipsum dolor sit amet consectetur adipisicing elit. Cum totam sunt illo deserunt quod vitae voluptatum facere, nulla, molestias dignissimos reiciendis ipsum quidem accusantium error pariatur eos? Facere, officia esse."
    }
]


def get_date(post):
    return post['date']


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request,'blog/index.html',{
        "posts": latest_posts
    })


def posts(request):
    return render(request,'blog/all-posts.html',{
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request,'blog/post-detail.html',{
        "post": identified_post
    })