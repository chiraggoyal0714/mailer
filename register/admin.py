# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import MailList, MailListUser, MailSession, MailSessionUser, User
# Register your models here.

admin.site.register(MailList)
admin.site.register(MailListUser)
admin.site.register(MailSession)
admin.site.register(MailSessionUser)
admin.site.register(User)
