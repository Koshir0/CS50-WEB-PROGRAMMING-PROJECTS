from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *



def index(request):
    now = timezone.now()
    upcoming = Post.objects.filter(created_date__gte=now).order_by('created_date')
    passed = Post.objects.filter(created_date__lt=now).order_by('-created_date')
    # print(list(upcoming) + list(passed))
    posts_list = list(upcoming) + list(passed)
    page = request.GET.get('page', 1)

    paginator = Paginator(posts_list, 10)
    # print(paginator.count)
    try:
        allposts = paginator.page(page)
    except PageNotAnInteger:
        allposts = paginator.page(1)
    except EmptyPage:
        allposts = paginator.page(paginator.num_pages)
        
    
   
    return render(request, "network/index.html",{
        # "posts":Post.objects.all(),
        "posts":list(upcoming) + list(passed),
        "allposts":allposts
        })

def indexcopy(request):
    now = timezone.now()
    upcoming = Post.objects.filter(created_date__gte=now).order_by('created_date')
    passed = Post.objects.filter(created_date__lt=now).order_by('-created_date')
    # print(list(upcoming) + list(passed))
    posts_list = list(upcoming) + list(passed)
    page = request.GET.get('page', 1)

    paginator = Paginator(posts_list, 10)
    # print(paginator.count)
    try:
        allposts = paginator.page(page)
    except PageNotAnInteger:
        allposts = paginator.page(1)
    except EmptyPage:
        allposts = paginator.page(paginator.num_pages)
        
    
   
    return render(request, "network/indexcopy.html",{
        # "posts":Post.objects.all(),
        "posts":list(upcoming) + list(passed),
        "allposts":allposts
        })



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"].capitalize()
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"].capitalize()
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


def new_post(request):
    if request.user.is_authenticated:
        # username = request.user.username
        posts=Post.objects.all()
        print(posts)
        if request.method == "POST":
            args = {
            "new_post" : request.POST.get("new_post"),
            }  
            try:
                new_post = Post(post=args["new_post"], user=request.user)
                new_post.save()
                return HttpResponseRedirect(reverse("index"),{
                    "posts":posts
                    })
            except IntegrityError:
                return HttpResponse("some error")
        else:
            return render(request, "network/index.html",{
                "posts":posts
                })
    else:
        return render(request, "network/404.html",{
            "error":"You should login first "      
                  })







def edit(request, postid):
    post_id = postid
    post = Post.objects.filter(id = post_id)
    # print(post)
    if request.method == "POST":
            args = {
            "update_post" : request.POST.get("update_post"),
            }  
            try:
                post.update(post=args["update_post"])
                return HttpResponseRedirect(reverse("index"),{
                    "posts":Post.objects.all()
                    })
            except IntegrityError:
                
                return render(request, "network/404.html",{"error":"some error"})
                
    return render(request, "network/edit.html", {
        "post_id":post_id,
        "post":post
        })


def profile(request, user_id):
    if request.user.is_authenticated:
        now = timezone.now()
        upcoming = Post.objects.filter(created_date__gte=now, user__in=User.objects.filter(id=user_id)).order_by('created_date')
        passed = Post.objects.filter(created_date__lt=now, user__in=User.objects.filter(id=user_id)).order_by('-created_date')
        username1 = User.objects.get(id=request.user.id)
        for post in passed:
            username = post.user
        user = User.objects.get(id=user_id)
        state = False
        for f in user.followers.all():
            if request.user.username == str(f):
                state = True
            else:
                state = False
        posts_list = list(upcoming) + list(passed)
        page = request.GET.get('page', 1)

        paginator = Paginator(posts_list, 10)
        # print(paginator.count)
        try:
            allposts = paginator.page(page)
        except PageNotAnInteger:
            allposts = paginator.page(1)
        except EmptyPage:
            allposts = paginator.page(paginator.num_pages)
        
    
        return render(request, "network/profile.html",{
            "posts":allposts,
            "username":str(username),
            "user_id":user_id,
            "followers":user.followers.all().count(),
            "following":user.following.all().count(),
            "state":state

            })



def follow(request, user_id):
    if request.user.is_authenticated:
        UserFollowing.objects.create(user_id=User.objects.get(id=request.user.id),
                             following_user_id=User.objects.get(id=user_id))
        return render(request, "network/follow.html", {"message": f"{request.user.username} following  {User.objects.get(id=user_id)}" })
    else:
        return render(request, "network/404.html",{"error":"something wrong"})

def unfollow(request, user_id):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        following = user.following.all()
        for follow in following:
            print(follow.following_user_id)
            if follow.following_user_id == User.objects.get(id=user_id):
                
                follow.delete()
                print("unfollow process done")
            else:
                print("not yet ")
                
        
        return render(request, "network/unfollow.html",{
            "following":following
            })


def following(request, user_id):
    user = User.objects.get(id=user_id)
    following = user.following.all()
    # print(following.following_user_id.all())
    followingPosts = []
    for follow in following:
        username = follow.following_user_id
        username_id = User.objects.get(username=username)
        users = [{"username_id":User.objects.get(username=username)}]
        for l in users:
            followingPosts.append({"posts":Post.objects.filter(user__in=User.objects.filter(username=l["username_id"])),
                "author":l["username_id"]})
        
    print(followingPosts)
        
    return render(request, "network/following.html",{
        # "followers":user.followers.all(),
        "following":following,
        # "f":UserFollowing.objects.filter(user_id=user),
        "followingPosts":followingPosts,
        # "obj":obj
        })


def followers(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, "network/followers.html",{
        "followers":user.followers.all()
        })




def likes(request, postid):  
    post = Post.objects.get(id = postid) 
    postlike = like.objects.create(user_like=User.objects.get(id=request.user.id), post_like=post )
    # print(len(post.likesto.all()))
    return HttpResponseRedirect(reverse("indexcopy"))




def unlike(request, postid):  
    post = Post.objects.get(id = postid) 
    postunlike = like.objects.filter(user_like=User.objects.get(id=request.user.id), post_like=post )
    # print(postunlike)
    for unlike in postunlike:
        unlike.delete()
        print("unlike")
    return HttpResponseRedirect(reverse("indexcopy"))

