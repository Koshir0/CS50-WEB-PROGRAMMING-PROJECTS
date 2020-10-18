from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
	# img_gif = models.url()
	pass


class Post(models.Model):
	post = models.CharField(max_length=350,blank = True, null = True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	created_date = models.DateTimeField(default=timezone.now()) 
	
	
	def __str__(self):
		return f"Post {self.post} by {self.user} "

# class Person(models.Model):
# 	name = models.CharField(max_length=64)

# 	def __str__(self):
# 		return self.name


# class Follower(models.Model):
# 	name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="")
# 	users = models.ManyToManyField(User, blank=True, related_name="following")

# 	def __str__(self):
# 		return self.name.username


class UserFollowing(models.Model):
	user_id = models.ForeignKey("User",on_delete=models.CASCADE, related_name="following")

	following_user_id = models.ForeignKey("User",on_delete=models.CASCADE,  related_name="followers")

	# You can even add info about when user started following
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.user_id.username




# class Follow(models.Model):
#       following = models.ForeignKey(User,on_delete=models.CASCADE, related_name="who_follows")
#       follower = models.ForeignKey(User,on_delete=models.CASCADE, related_name="who_is_followed")
#       follow_time = models.DateTimeField(auto_now=True)

#       def __unicode__(self):
#           return str(self.follow_time)


class like(models.Model):
	user_like = models.ForeignKey("User",on_delete=models.CASCADE, related_name="likesby")
	post_like = models.ForeignKey("Post",on_delete=models.CASCADE, related_name="likesto")

	def __str__(self):
		return f"{str(self.user_like.username)} liked {self.post_like.post}"
