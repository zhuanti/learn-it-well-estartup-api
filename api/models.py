# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

# 使用者資訊
class User(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    pwd = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=5)
    live = models.CharField(max_length=100)
    photo = models.TextField(blank=True, null=True)
    borth = models.DateField(blank=True, null=True)
    purview = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'user'

# 教室類別
class Classroom(models.Model):
    no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'classroom'

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

# 讀書時長報表
class Report(models.Model):
    no = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    classroom_type_no = models.ForeignKey(Classroom, models.DO_NOTHING)
    subject_no = models.ForeignKey(Subject, models.DO_NOTHING)
    set_time = models.IntegerField()
    entry_time = models.DateField(blank=True, null=True)
    exit_time = models.DateField(blank=True, null=True)
    total_time = models.DateField(blank=True, null=True)
    subject_detail = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'report'

# 學習規劃
class Plan(models.Model):
    no = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    name = models.CharField(max_length=100)
    pace = models.IntegerField()
    datetime = models.DateField(blank=True, null=True)
    ftime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plan'

# 成就輔助
class Success(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    pace = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'success'

# 成就列表
class Success_list(models.Model):
    no = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    success_no = models.ForeignKey(Success, models.DO_NOTHING)
    pace = models.IntegerField()
    lockif = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'success_list'

# 討論室
class Discussroom(models.Model):
    # SUBJECT_CHOICES = (
    #     ('1', '國文'),
    #     ('2', '數學'),
    #     ('3', '英文'),
    #     ('4', '物理'),
    #     ('5', '化學'),
    #     ('6', '地科'),
    #     ('7', '生物'),
    #     ('8', '地理'),
    #     ('9', '歷史'),
    #     ('10', '公民'),
    #     ('11', '其他'),
    # )
    no = models.AutoField(primary_key=True)
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
    no = models.AutoField(primary_key=True)
    discussroom_no = models.ForeignKey(Discussroom, models.DO_NOTHING)
    user = models.ForeignKey(User, models.DO_NOTHING)
    comment = models.CharField(max_length=1000)
    datetime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discussroom_record'
        
# 討論室提問
class Discussroom_question(models.Model):
    no = models.AutoField(primary_key=True)
    discussroom_no = models.ForeignKey(Discussroom, models.DO_NOTHING)
    quser = models.ForeignKey(User, models.DO_NOTHING)
    title = models.CharField(max_length=1000)
    datetime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discussroom_question'

# 討論室提問答案
class Discussroom_ans(models.Model):
    no = models.AutoField(primary_key=True)
    question_no = models.ForeignKey(Discussroom_question, models.DO_NOTHING)
    auser = models.ForeignKey(User, models.DO_NOTHING)
    comment = models.CharField(max_length=1000)
    datetime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discussroom_ans'

# 自習室
class Studyroom(models.Model):
    no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    total_people = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'studyroom'

# 檢舉
class Impeach(models.Model):
    no = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    reason = models.CharField(max_length=1000)
    discussroom_no = models.ForeignKey(Discussroom, models.DO_NOTHING)
    datetime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'impeach'


# 以下為學姊範例程式碼
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


