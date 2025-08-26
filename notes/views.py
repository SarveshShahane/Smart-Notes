from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import forms
from .models import Note
from django.contrib import messages
# read notes
def home(request):
    notes=Note.objects.all().order_by('-time')
    context={'notes':notes}
    return render(request, "notes/home.html",context)


# create notes form route

def create_note(request):
    context={'form':forms.NoteForm()}
    if request.method == "POST":
        form = forms.NoteForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            tags = form.cleaned_data['tags']
            Note.objects.create(title=title, content=content, tags=tags)
            messages.success(request, 'Note created successfully!')
            return redirect('home')
    return render(request, "notes/create_note.html", context)

# search notes
def search_notes(request):
    query=request.GET.get('q')
    # search match results with title and tags
    results=Note.objects.filter(title__icontains=query) | Note.objects.filter(tags__icontains=query)
    context={'notes':results}
    return render(request, "notes/home.html", context)

# delete note
def delete_note(request,note_id):
    note=Note.objects.get(id=note_id)
    if(request.method== "POST"):
        note.delete()
        messages.success(request, 'Note deleted successfully!')
        return redirect('home')
    
    return render(request, "notes/delete_note.html",{'note':note})