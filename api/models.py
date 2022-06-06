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

# 討論室文字紀錄
class Discussroom_record(models.Model):
    no = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(Subject, models.DO_NOTHING)
    comment = models.CharField()
    discussroom_no = models.ForeignKey(Discussroom, models.DO_NOTHING)
    datetime = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'discussroom_record'


