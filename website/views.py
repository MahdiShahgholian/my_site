from django.shortcuts import render, HttpResponseRedirect
from .forms import ContactForm, NewsletterForm
from django.contrib import messages

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            
            form.save()
            messages.success(request, 'Form submission successful')

    form = ContactForm()     
    return render(request, 'website/contact.html', {"form": form})

def newsletter_view(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect('/')
    
def test_view(request):
    return render(request, 'website/test.html')