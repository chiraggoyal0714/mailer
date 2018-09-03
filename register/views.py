# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.conf import settings
from register.models import *
from django.core.mail import send_mail
from django.http import HttpResponse


def update(request):
	invalue = request.POST['name']
	maillist = [str(ele) for ele in MailList.objects.all()]
	if invalue in maillist:
		listkey = MailList.objects.get(name=invalue)
		listkey = listkey.id
	else:
		maillistobj = MailList()
		maillistobj.name = invalue
		maillistobj.save()
		listkey = MailList.objects.get(name=invalue)
		listkey = listkey.id

	email = request.POST['email']
	list_mail = email.split(',')
	userlist = [str(ele) for ele in User.objects.all()]
	for i in list_mail:
		if i in userlist:
			userkey = User.objects.get(email=i)
			userkey = userkey.id
		else:
			user = User()
			user.email = i
			user.save()
			userkey = User.objects.get(email=i)
			userkey = userkey.id
			maillistuser = MailListUser()
			maillistuser.mail_list_id = listkey
			maillistuser.user_id = userkey
			maillistuser.save()
	return render(request, "success.html", {})

def sendSimpleEmail(request):

	listid = request.POST['listid']
	maillistuser = MailListUser.objects.filter(mail_list_id=listid)
	session = MailSession()
	session.subject = request.POST['subject']
	session.content = request.POST['content']
	session.save()
	session = MailSession.objects.latest('content')
	sessionid = session.id
	mailsession = MailSessionUser()  
	for i in maillistuser:
		user = User.objects.get(id=i.user_id)
		user = user.email
		res = send_mail(request.POST['subject'], request.POST['content'], settings.EMAIL_HOST_USER, [user], fail_silently = False, html_message = '<a href=http://127.0.0.1:8000/register/verify?userid='+str(i.user_id)+'&sessionid='+str(sessionid)+'>test</a>' )
		key = MailSession.objects.latest('id')
		mailsession = MailSessionUser()
		mailsession.mail_session_id = key.id
		mailsession.user_id = i.user_id
		mailsession.flag = 0
		mailsession.save()

	return HttpResponse('%s'%res)


def fetchquery(request):
	context = {
		'userid':request.GET.get('userid'),
		'sessionid':request.GET.get('sessionid'),
	}
	mailsessionuser=MailSessionUser.objects.get(mail_session_id=context['sessionid'],user_id=context['userid'])
	mailsessionuser.flag=1

	return render(request, "fetchquery.html", context)


def home(request):
	return render(request, "home.html", {})




def check(request):

	if (request.POST.get('user')=="swaglabs" and request.POST.get('passwd')=="swaglabs") :
		request.session['sessionElement'] = "Element"
		all_mails = MailList.objects.all()
		context = {
			'all_mails':all_mails
		}
		if(request.session['sessionElement'] == "Element"):
			return render(request, "form.html", context)
		else:
			return render(request, "fail.html", {})
	else:
		return render(request, "fail.html", {})