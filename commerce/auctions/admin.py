from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(User)
admin.site.register(AuctionItems)
admin.site.register(Watchlist)
admin.site.register(bids)
admin.site.register(closed_auctions)
admin.site.register(Comments)
admin.site.register(category)

