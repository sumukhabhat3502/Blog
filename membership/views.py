from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
# from django.contrib.auth.models import User,auth
from base.models import userProfile
from membership import models
from .forms import ProfilePage, SignUp, EditProfile
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView, CreateView

# Create your views here.


class UserReg(generic.CreateView):
    form_class = SignUp
    template_name = 'registration/register.html'
    success_url = reverse_lazy('createuserprofile')


class Upd_Pro(generic.UpdateView):
    form_class = EditProfile
    template_name = 'registration/profile_edit.html'
    success_url = reverse_lazy('home')

    def get_object(self,):
        return self.request.user


class PassWord(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('login')


class ProfileView(DetailView):
    model = userProfile
    template_name = 'registration/user-profile.html'

    def get_context_data(self, *args, **kwargs):
        users = userProfile.objects.all()
        context = super(ProfileView, self).get_context_data(*args, **kwargs)
        current_user = get_object_or_404(userProfile, id=(self.kwargs['pk']))
        context["current_user"] = current_user
        return context


class EditProfileView(generic.UpdateView):
    model = userProfile
    template_name = 'registration/edit_user_profile.html'
    fields = ['bio_data', 'profile_pic', 'Twitter_url',
              'Instagram_url', 'linkedin_url', 'website_url']
    success_url = reverse_lazy('home')


class CreatePro(CreateView):
    model = userProfile
    form_class = ProfilePage
    template_name = 'registration/create_user_pro.html'
    # fields= '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
