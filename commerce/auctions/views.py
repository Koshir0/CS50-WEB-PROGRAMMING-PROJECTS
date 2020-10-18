
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import *
import operator



def index(request):
    items = AuctionItems.objects.all()
    if request.user.is_authenticated:
        username = request.user.username
        watchlists = Watchlist.objects.filter(username=username)
        return render(request, "auctions/index.html",{
        "items" : items,
        "watchnum":len(watchlists)
        })

    
    
    return render(request, "auctions/index.html",{
        "items" : items
        })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")





@login_required
def create(request):
    # global categories
   
    # categories = ["Fashion", "Toys", "Home", "Posters", "Electronics"]
    categories = category.objects.all()

    if request.user.is_authenticated:
        # categories = categories.filter(category=category)
        username = request.user.username
        watchlists = Watchlist.objects.filter(username=username)
        
        if request.method == "POST":

            args = {
            "title":request.POST.get("title"),
            "description":request.POST.get("description"),
            "image":request.POST.get("image"),
            "price":float(request.POST.get("price")),
            "category":request.POST.get("category"),
            "listed_by":username,
            "starting_bid":float(request.POST.get("starting_bid"))

            }
            # title = request.POST.get("title")
            # description = request.POST.get("description")
            # image = request.POST.get("image")
            # price = float(request.POST.get("price"))
            # category = request.POST.get("category")
            try:
                item = AuctionItems(item=args["title"], description=args["description"], image=args["image"], price=args["price"], category=args["category"], listed_by=args["listed_by"], starting_bid=args["starting_bid"])
                print(item)
                item.save()

                return HttpResponseRedirect(reverse("index"),{
                    "watchnum":len(watchlists)
                    })
            except IntegrityError:
                
                return render(request, "auctions/create.html", {
                    "message": "There is an error.",
                    "watchnum":len(watchlists),
                    "categories":categories
                })
        return render(request, "auctions/create.html",{
            "watchnum":len(watchlists),
            "categories":categories
            })



@login_required
def listing(request, listing_id):
    if request.user.is_authenticated:
        username = request.user.username
        listing = AuctionItems.objects.get(id=listing_id)
        money = bids.objects.filter(bid_item=listing.item).count()
        comments=Comments.objects.filter(comment_item=listing.item)
        all_bid = bids.objects.filter(bid_item=listing.id)
        watchlists = Watchlist.objects.filter(username=username)
        return render(request, "auctions/listing.html", {
            "listing":listing,
            "watchnum":len(watchlists),
            "bids":len(all_bid),
            "all_bid":all_bid,
            "comments":comments,
            "bids":money
            })
    # else:
    #     HttpResponseRedirect(reverse("not_allowed"))


@login_required
def watch(request, listing_id):
    if request.user.is_authenticated:
        username = request.user.username
        listing = AuctionItems.objects.get(id=listing_id)

    # print(type(listing))
        watchlist = Watchlist(item=listing.item, description=listing.description, image=listing.image, price=listing.price, username=username)
        watchlist.save()
        watchlists = Watchlist.objects.filter(username=username)
        return render(request, "auctions/listing.html",{
            "listing":listing,
            "watchnum":len(watchlists)
            })
    
@login_required
def watchlist(request):
    if request.user.is_authenticated:
        username = request.user.username
        watchlists = Watchlist.objects.filter(username=username)

        return render(request, "auctions/watchlist.html",
            {
            "watchlists":watchlists,
            "watchnum":len(watchlists)
            })

@login_required
def delete(request, listing_id):
    if request.user.is_authenticated:
        username = request.user.username
        listing = Watchlist.objects.get(id=listing_id)
        listing.delete()
        watchlists = Watchlist.objects.filter(username=username)
        # # print(type(listing))
        # watchlist = Watchlist(item=listing.item, description=listing.description, image=listing.image, price=listing.price)
        # watchlist.save()
        return HttpResponseRedirect(reverse("watchlist"),
            {
            "watchnum":len(watchlists)
            })
    


@login_required
def bid(request, listing_id):
    listing = AuctionItems.objects.get(id=listing_id)
    money = bids.objects.filter(bid_item=listing.item).count()
    print(money)
    if request.user.is_authenticated:
        username = request.user.username
        watchlists = Watchlist.objects.filter(username=username)
        if request.method == "POST":
            args={
            "bid_user":username,
            "bid_price":float(request.POST.get("bid")),
            "bid_item":listing.item

            }
            if len(bids.objects.filter(bid_item=listing.item)) == 0:
                print("Im in first for")
                if args["bid_price"] > listing.starting_bid :
                    bid = bids(bid_user=args["bid_user"],bid_price=args["bid_price"],bid_item=args["bid_item"])
                    bid.save()
                    return render(request, "auctions/listing.html",{
                        "listing":listing,
                        "watchnum":len(watchlists),
                        "bids":len(bids.objects.filter(bid_item=listing.item)),
                        "all_bid":bids.objects.filter(bid_item=listing.item)
                        # "last_bid":last_bid
                        })
                else:
                    return render(request, "auctions/404.html",{
                            "error":"bid must be greater than starter price and all other bids"
                         })
            else:
                print("Im in 2 for")
                for bid in bids.objects.filter(bid_item=listing.item):
                    if args["bid_price"] > bid.bid_price  and args["bid_price"] > listing.starting_bid:
                        print(args["bid_price"], bid.bid_price)
                    else:
                        return render(request, "auctions/404.html",{
                            "error":"bid must be greater than starter price and all other bids"
                            })

                bid = bids(bid_user=args["bid_user"],bid_price=args["bid_price"],bid_item=args["bid_item"])
                bid.save()
                return render(request, "auctions/listing.html",{
                    "listing":listing,
                    "watchnum":len(watchlists),
                    "bids":money,
                    "all_bid":bids.objects.filter(bid_item=listing.item)
                    # "last_bid":last_bid
                    })
                    
            
        return render(request, "auctions/listing.html",{
                        "listing":listing,
                        "watchnum":len(watchlists),
                        "bids":money,
                        "all_bid":bids.objects.filter(bid_item=listing.item),
                        # "money":money
                        "last_bid":all_bid.last()
                        })
                
    


def not_allowed(request, listing_id):
    return render(request, "auctions/404.html")


@login_required
def close(request, listing_id):
    if request.user.is_authenticated:
        username = request.user.username
        listing = AuctionItems.objects.get(id=listing_id)
        comments=Comments.objects.filter(comment_item=listing.item)
        watchlists_re = Watchlist.objects.filter(item=listing.item)
        bides = bids.objects.filter(bid_item=listing.item)
        bide = {}
        
        for bid in bides:
            bidder = bid.bid_user
            bide[bidder] = bid.bid_price
        # print(bide)
        winner =max(bide.items(), key=operator.itemgetter(1))[0]

        close = closed_auctions(winner = winner, item=listing.item, starting_bid=listing.starting_bid, image=listing.image, price=listing.price, final_bid = bide[winner])
        close.save()
        if winner == username:
            bides.delete()
            comments.delete()
            listing.delete()
            watchlists_re.delete()
            return  render(request, "auctions/close.html",{
                "so":"So, You win the Auction"
                })
        else:
            watchlists_re.delete()
            bides.delete()
            comments.delete()
            listing.delete()
            return  render(request, "auction/close.html",{
                "close":"the auction is closed ",
                "winner":winner})




@login_required
def comment(request, listing_id):
    listing = AuctionItems.objects.get(id=listing_id)
    comments = Comments.objects.filter(comment_item=listing.item)
    money = bids.objects.filter(bid_item=listing.item).count()

    if request.user.is_authenticated:
        username = request.user.username
        watchlists = Watchlist.objects.filter(username=username)
        
        if request.method == "POST":

            args = {
            "comment":request.POST.get("comment"),
            "comment_item":listing.item
            }
           
           
            comment = Comments(comment=args["comment"], comment_user=username, comment_item=args["comment_item"])
            comment.save()
            
            return render(request, "auctions/listing.html",{
                "watchnum":len(watchlists),
                "listing":listing,
                "comments":comments,
                "bids":money
                })
    return render(request, 'auctions/listing.html',{
                "watchnum":len(watchlists),
                "listing":listing,
                "comments":comments,
                "bids":money
                }
           )
       
@login_required
def categories(request):
    # categories = ["Fashion", "Toys", "Home", "Posters", "Electronics"]
    categories = category.objects.all()
    return render(request, "auctions/categories.html",{
        "categories":categories
        })

@login_required
def all_cate(request, cate):
    all_list = AuctionItems.objects.filter(category=cate)
    return  render(request,"auctions/all_list.html" ,{
        "all_list":all_list,
        "cate": cate
        })
    
