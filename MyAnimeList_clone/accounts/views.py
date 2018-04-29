from django.shortcuts import render
from django.urls import reverse_lazy
from accounts.forms import SignUpForm
from django.views.generic import CreateView,DetailView

from accounts.models import UserProfile

def SignUp(request):
    
    if request.method == 'POST':
        signup_form = SignUpForm(data=request.POST)

        if signup_form.is_valid():
            user = signup_form.save()

            profile = UserProfile.objects.create(user=user,username=user.username)
            profile.save()
    else:
        signup_form = SignUpForm()
    
    return render(request,'accounts/signup.html',context={'form':signup_form})

class ProfileDetailView(DetailView):
    model = UserProfile
    slug_field = 'pk'
    template_name = 'accounts/profile_detail.html'