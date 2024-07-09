from django.shortcuts import redirect
from django.urls import reverse

def unauthenticated_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('home'))  # Redirect to the home page or another page if the user is already logged in
        return view_func(request, *args, **kwargs)
    return _wrapped_view