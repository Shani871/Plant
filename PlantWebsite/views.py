from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def portfolio(request):
    return render(request, 'portfolio.html')
def checkout(request):
    return render(request, 'checkout.html')
def blog(request):
    return render(request, 'blog.html')
