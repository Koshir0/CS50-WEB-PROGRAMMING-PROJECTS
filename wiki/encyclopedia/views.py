from django.shortcuts import render
import markdown
from .form import *
from . import util
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

import random
import re


md = markdown.Markdown()

def index(request):

	return render(request, "encyclopedia/index.html", {
		"entries": util.list_entries()
	})



def wiki(request, title):
	if title in util.list_entries():
		re = md.convert(util.get_entry(title))
		# print(re)
		return render(request, "encyclopedia/entry.html", {
			"entry": re,
			"title" : title
			})
	else:
		return render(request, "encyclopedia/entry.html")


def search(request):
	
	if request.method=="POST":
		query = request.POST.get('q')
		strings = util.list_entries()
		print(query.islower())
		if query.islower():
			substring = query.capitalize()
			strings_with_substring = [string for string in strings if substring in string]
			search = strings_with_substring
			# re = md.convert(util.get_entry(search))
			return render(request, "encyclopedia/search.html", {
					"entry": search,
					})
		else:
			substring = query
			strings_with_substring = [string for string in strings if substring in string]
			search = strings_with_substring
			# re = md.convert(util.get_entry(search))
			return render(request, "encyclopedia/search.html", {
					"entry": search,
					})
	else:
		return render(request, "encyclopedia/index.html")
	
		
	
def create(request):
	form = NewEntryForm()
	if request.method=="POST":
		title = request.POST.get('title')
		content = request.POST.get('content')
		if title in util.list_entries():
			error = "This entry is exist"
			return render(request, "encyclopedia/index.html", {
			"entries": util.list_entries(),
			"error" : error,
			"form": form
				})
		else:
			util.save_entry(title, content)
			return render(request, "encyclopedia/index.html", {
			"entries": util.list_entries(),
			"form": form
			})
	
	else:
		return render(request, "encyclopedia/create.html",{
			"form": form
			})





def randompage(request):
	entries = util.list_entries()
	entry = random.choice(entries)
	re = md.convert(util.get_entry(entry))
	return render(request, "encyclopedia/randompage.html", {
		"entry": re
		})




	
def update_page(request, title):
	if title in util.list_entries():
		content =util.get_entry(title)
		form = NewEntryForm()
		return render(request, "encyclopedia/update.html",{
			"form":form,
			"title":title,
			"content":content
			})
	
	


	
def update(request):
	if request.method=="POST":
		title = request.POST.get('title')
		content = request.POST.get('content')
		util.save_entry(title, content)
		return HttpResponseRedirect(reverse("entry", args=(title,)))
	
	


