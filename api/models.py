# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

# 學制類別
class Schoolsys(models.Model):
    no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'school_sys'

# 科目
class Subject(models.Model):
    no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'subject'

# 討論室
class Discussroom(models.Model):
    no = models.IntegerField(primary_key=True)
    schoolsys_no = models.ForeignKey(Schoolsys, models.DO_NOTHING)
    subject_no = models.ForeignKey(Subject, models.DO_NOTHING)
    name = models.CharField(max_length=100)
    pwd = models.CharField(max_length=30)
    total_people = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'discussroom'

# 使用者資訊
class User(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    pwd = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=5)
    live = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    borth = models.DateField
    purview = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'user'

# 討論室文字紀錄
class Discussroom_record(models.Model):
    no = models.IntegerField(primary_key=True)
    discussroom_no = models.ForeignKey(Discussroom, models.DO_NOTHING)
    user = models.ForeignKey(User, models.DO_NOTHING)
    comment = models.CharField(max_length=1000)
    datetime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discussroom_record'
        
# 討論室提問
class Discussroom_question(models.Model):
    no = models.IntegerField(primary_key=True)
    discussroom_no = models.ForeignKey(Discussroom, models.DO_NOTHING)
    quser = models.ForeignKey(User, models.DO_NOTHING)
    title = models.CharField(max_length=1000)
    datetime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discussroom_question'

# 討論室提問答案
class Discussroom_ans(models.Model):
    no = models.IntegerField(primary_key=True)
    question_no = models.ForeignKey(Discussroom_question, models.DO_NOTHING)
    auser = models.ForeignKey(User, models.DO_NOTHING)
    comment = models.CharField(max_length=1000)
    datetime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discussroom_ans'

# class Account(models.Model):
#     id = models.CharField(primary_key=True, max_length=100)
#     pwd = models.CharField(max_length=30)
#     name = models.CharField(max_length=30)
#     gender = models.BooleanField()
#     photo = models.TextField(blank=True, null=True)
#     birth = models.DateField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'account'
#
#
# class Book(models.Model):
#     no = models.AutoField(primary_key=True)
#     user = models.ForeignKey(Account, models.DO_NOTHING)
#     name = models.CharField(max_length=100)
#     title = models.CharField(max_length=100)
#     comment = models.TextField()
#
#     class Meta:
#         managed = False
#         db_table = 'book'
#
#
# class BookTag(models.Model):
#     no = models.AutoField(primary_key=True)
#     book_no = models.IntegerField()
#     name = models.CharField(max_length=20)
#
#     class Meta:
#         managed = False
#         db_table = 'book_tag'


