# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class MailList(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'mail_list'
    def __str__(self):
        return self.name

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'user'

    def __str__(self):
        return self.email

class MailListUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    mail_list_id = models.BigIntegerField()
    user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mail_list_user'

    def __str__(self):
        return "mail_list_id is:    "+str(self.mail_list_id) + "    user_id is:     " + str(self.user_id)


class MailSession(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.CharField(max_length=10000)
    subject = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'mail_session'
    def __str__(self):
        return "content is:     " + self.content +"     subject is :" + self.subject + "    date is : " + str(self.date)

class MailSessionUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    mail_session_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mail_session_user'
    def __str__(self):
        return "mail_session_id is :    " + str(self.mail_session_id) + "   user_id is :    " + str(self.user_id) + "   flag is: " + str(self.flag)
