from django.shortcuts import render
# Create your views here.
from django.shortcuts import redirect

from .forms import LoginForm

from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import View


class LoginView(View):
    
    form = LoginForm()
    message = None
    template = 'users/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('users:dashboard')
        return render(request, self.template, self.get_context())

    def post(self, request, *args, **kwargs):
        username_post = request.POST['username']
        password_post = request.POST['password']
        user = authenticate( username = username_post, password = password_post)
        if user is not None:
            login_django(request, user)
            return redirect('users:dashboard')
        else:
            self.message = "Username o password incorrecto"
        return render(request, self.template, self.get_context())

    def get_context(self):
        return {'form':self.form, 'message':self.message}

class DashboardView(LoginRequiredMixin, View):
    login_url='users:login'
    
    def get (self, request, *args,**kwargs):
        return render(request, 'users/dashboard.html')

@login_required(login_url='users:login')
def logout(request):
    logout_django(request)
    return redirect('users:login')



