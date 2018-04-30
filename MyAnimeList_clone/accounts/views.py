from django.shortcuts import render
from django.urls import reverse_lazy
from accounts.forms import SignUpForm
from django.views.generic import CreateView,DetailView,UpdateView
from accounts.forms import ProfileForm
from accounts.models import UserProfile
from django.shortcuts import get_object_or_404 

from django.contrib.auth.mixins import LoginRequiredMixin

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

class ProfileUpdateView(LoginRequiredMixin,UpdateView):
    model = UserProfile
    form_class = ProfileForm
    slug_field = 'pk'
    template_name='accounts/profile_update.html'

    def get_initial(self):
        initial = super(ProfileUpdateView,self).get_initial()

        profile_object = self.get_object()

        initial['profile_picture'] = profile_object.profile_picture

        return initial

    def get_object(self,*args,**kwargs):
        profile = get_object_or_404(UserProfile,pk=self.kwargs['slug'])
        return profile