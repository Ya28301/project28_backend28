from django.shortcuts import render

def login_page(request):
    return render(request, 'content/login.html')
