# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.loader import get_template
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from board.forms import *


def main_page(request):
	template = get_template('main_page.html')
	variables = Context({
		'user': request.user
	})
	output = template.render(variables)
	return HttpResponse(output)

def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')

def register_page(request):
    print request.method
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
                email = form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()

    variables = RequestContext(request, {
        'form': form
    })
    return render_to_response('registration/register.html', variables)
