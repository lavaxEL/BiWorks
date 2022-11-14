from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.utils.text import capfirst
from django.utils.translation import ugettext, ugettext_lazy as _
import smtplib
import random
from django.db.models import Q
from profiles.models import Profile

class AuthenticationConfirmForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """
    username = forms.CharField(max_length=254)
    password = forms.CharField(label=_("Password"), max_length=254)
    code = forms.CharField(label=_("Email-code"), max_length=254)
    error_messages = {
        'invalid_login': _("Please enter a correct %(username)s and email-code. "
                           "Note that both fields may be case-sensitive."),
        'inactive': _("This account is inactive."),
    }

    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        print("iz klassa")
        print(request.POST)

        self.request = request
        self.user_cache = None
        super(AuthenticationConfirmForm, self).__init__(*args, **kwargs)

        # Set the label for the "username" field.
        UserModel = get_user_model()
        self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
        self.fields['password'].widget.attrs['readonly'] = True
        if self.fields['username'].label is None:
            self.fields['username'].label = capfirst(self.username_field.verbose_name)




user = "iugenissparta666@mail.ru"
passwd = "9mFrNpMAhgk08sJmrutg"
server = "smtp.mail.ru"
port = 587
subject = "Код подтверждения."
charset = 'Content-Type: text/plain; charset=utf-8'
mime = 'MIME-Version: 1.0'

def login_view(request, *args, **kwargs):
    form = AuthenticationForm(request, data=request.POST or None)
    form_confirm= AuthenticationConfirmForm(request, data=request.POST or None)

    print(request.POST)
    if form.is_valid():
        user_ = form.get_user()
        code=random.randint(100000, 999999)
        body = "\r\n".join((f"From: {user}", f"To: {str(user_)}",
                            f"Subject: {subject}", mime, charset, "", str(code)))
        profile = Profile.objects.filter(Q(user=user_))
        obj1 = profile.first()
        my_code=obj1.code
        if ("code" in request.POST and request.POST.get('code') == str(my_code)):
            login(request, user_)
            return redirect("/")
        else:
            try:
                profile = Profile.objects.filter(Q(user=user_))
                obj1 = profile.first()
                obj1.code=code
                obj1.save()
                smtp = smtplib.SMTP(server, port)
                smtp.starttls()
                smtp.ehlo()
                smtp.login(user, passwd)
                smtp.sendmail(user, str(user_), body.encode('utf-8'))
            except smtplib.SMTPException as err:
                print('Что - то пошло не так...')
                raise err
            finally:
                smtp.quit()
            context = {
                "form": form_confirm,
                "btn_label": "Login",
                "title": "Confirm"
            }
            return render(request, "accounts/auth.html", context)

    context = {
        "form": form,
        "btn_label": "Login",
        "title": "Login"
    }
    print("just update")
    return render(request, "accounts/auth.html", context)

def logout_view(request, *args, **kwargs):
    if request.method == "POST":
        logout(request)
        return redirect("/login")
    context = {
        "form": None,
        "description": "Are you sure you wanna leave?",
        "btn_label": "Sign out",
    }
    return render(request, "accounts/auth.html", context)


def register_view(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=True)
        user.set_password(form.cleaned_data.get("password1"))
        login(request, user)
        profile = Profile.objects.filter(Q(user=user))
        obj1 = profile.first()
        obj1.coins=1000
        obj1.save()
        return redirect("/")
    context = {
        "form": form,
        "btn_label": "Sign up",
        "title": "Welcome to BiWorks"
    }
    return render(request, "accounts/auth.html", context)