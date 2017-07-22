from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views.generic import View
from account.forms import UserForm, LoginForm
from blog.models import Weblog


class UserFormView(View):
    form_class = UserForm
    template_name = 'account/register_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('blog:create')
        return render(request, self.template_name, {'form': form})


class UserLoginView(View):
    form_class = LoginForm
    template_name = 'account/login_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                for blog in Weblog.objects.all():
                    if user.username == blog.author:
                        return redirect('blog:index', blog.pk)
                return redirect('blog:create')
        else:
            return render(request, self.template_name, {'form': form})
