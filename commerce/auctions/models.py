from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
# from datetime import datetime


class User(AbstractUser):
    pass


class AuctionItems(models.Model):
	item = models.CharField(max_length=200)
	description = models.CharField(max_length=400,blank = True, null = True)
	image = models.CharField(max_length=400)
	created_date = models.DateTimeField(default=timezone.now()) 
	price = models.IntegerField()
	starting_bid = models.IntegerField()
	category = models.CharField(max_length=64, null = True, blank = True)
	listed_by = models.CharField(max_length=100)

	def __str__(self):
		return f"{self.item} {self.price} {self.category} {self.description}"

	
class bids(models.Model):
	bid_item = models.CharField(max_length=200)
	bid_user = models.CharField(max_length=100)
	bid_price = models.IntegerField()

	def __str__(self):
		return f"{self.bid_price} {self.bid_user} {self.bid_item} "

class Comments(models.Model):
	comment = models.CharField(max_length=240 ,blank = True)
	comment_user = models.CharField(max_length=100)
	comment_item = models.CharField(max_length=240 )

	def __str__(self):
		return f"{self.comment} {self.comment_user} {self.comment_item} "


class Watchlist(models.Model):
	username = models.CharField(max_length=200)
	item = models.CharField(max_length=200)
	description = models.CharField(max_length=400,blank = True, null = True)
	image = models.CharField(max_length=400)
	price = models.IntegerField()


	def __str__(self):
		return f"{self.username} {self.item} "
	


class closed_auctions(models.Model):
	winner = models.CharField(max_length=200) 
	item= models.CharField(max_length=200)
	starting_bid=models.IntegerField()
	image=models.CharField(max_length=400)
	price=models.IntegerField()
	final_bid = models.IntegerField()
	closed_date = models.DateTimeField(default=timezone.now())


	def __str__(self):
		return f"{self.item} {self.price} {self.winner} {self.final_bid}"

class category(models.Model):
	cate = models.CharField(max_length=64)

