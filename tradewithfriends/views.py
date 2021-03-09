from django.shortcuts import render
from tradewithfriends.main import get_profile_data

def view_profile(request, username="Jon"):
    result = render(request, 'profile.html', {'holdings_pct': get_profile_data(username), 'username':username})
    return result

def login(request):
    result = render(request, 'login.html')
    return result
