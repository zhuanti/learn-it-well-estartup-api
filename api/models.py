# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models






# 學制
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

# 使用者個人資料表
# class User(models.Model):
#     id = models.CharField(primary_key=True, max_length=100)
#     pwd = models.CharField(max_length=30)
#     name = models.CharField(max_length=30)
#     gender = models.BooleanField()
#     live = models.CharField(max_length=100)
#     photo = models.TextField(blank=True, null=True)
#     birth = models.DateField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'user'

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
