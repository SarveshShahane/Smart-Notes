from django import forms

class NoteForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    tags = forms.CharField(max_length=100)
    