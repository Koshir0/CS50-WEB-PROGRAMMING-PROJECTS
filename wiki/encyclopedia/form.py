from django import forms

class NewEntryForm(forms.Form):
    title   = forms.CharField(label="Title")
    content = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":10, "class":"form-control"}))
