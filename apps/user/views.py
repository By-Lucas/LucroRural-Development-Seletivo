from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from django.contrib import messages
from django.contrib.messages import constants

from .forms import UserForm, ProfileForm, SignUpForm

class LoginView(auth_views.LoginView):
    template_name = 'login/login.html'
    next_page = 'profile'
    def get(self, request):
        return render(request, self.template_name, {'form': AuthenticationForm})

class LogoutView(auth_views.LogoutView):
    next_page = 'index'

class profileView(TemplateView):
    template_name = 'profile.html'

    def get(self, request):
        user = request.user
        profile = user.profile
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, self.template_name, context)

class ProfileUpdateView(TemplateView):
    template_name = 'profile-edit.html'

    def get(self, request):
        user = request.user
        profile = user.profile
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        user = request.user
        profile = user.profile
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.add_message(request, constants.SUCCESS, 'Perfil editado com sucesso!')
            return redirect(reverse_lazy('profile'))
        context = {
            'user_form':user_form,
            'profile_form':profile_form
        }
        return self.render_to_response(context)

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('index')
    template_name = 'register.html'