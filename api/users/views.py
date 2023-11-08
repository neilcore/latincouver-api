from django.shortcuts import render

def defaultPage(requests):
    return render(requests, 'users/defaultPage.html')
