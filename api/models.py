# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



# 使用者資訊
from django.db.models import Model


class Live(models.Model):
    no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'live'

class Gender(models.Model):
    no = models.IntegerField(primary_key=True)
    gender = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'gender'

class User(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    pwd = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    gender = models.ForeignKey(Gender, models.DO_NOTHING)
    live = models.ForeignKey(Live, models.DO_NOTHING)
    photo = models.TextField(blank=True, null=True)
    borth = models.DateField(blank=True, null=True)
    purview = models.CharField(max_length=1)
    point = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'

#DateTimeField：主要存储时间相关的数据类型，格式为YYYY-MM-DD HH:MM:[ss[.uuuuuu]][TZ]

#注意：DateField与DateTimeField有两个属性，配置auto_now_add=True，创建数据记录的时候会把当前时间添加到数据库，
# 配置auto_now=True，每次更新数据记录的时候都会更新该字段


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
        db_table = 'schoolsys'


# 科目
class Subject(models.Model):
    no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'subject'


# 設定時間
class Settime(models.Model):
    no = models.IntegerField(primary_key=True)
    time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'settime'


# 讀書時長報表
class Report(models.Model):
    no = models.AutoField(primary_key=True, auto_created=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    classroom_type_no = models.ForeignKey(Classroom, models.DO_NOTHING)
    subject_no = models.ForeignKey(Subject, models.DO_NOTHING)
    settime_no = models.ForeignKey(Settime, models.DO_NOTHING)
    entry_time = models.DateTimeField(blank=True, null=True)
    exit_time = models.DateTimeField(blank=True, null=True)
    # entry_time = models.DateField(blank=True, null=True)
    # exit_time = models.DateField(blank=True, null=True)
    total_time = models.DateField(blank=True, null=True)
    subject_detail = models.CharField(max_length=50)

    class Meta:
        get_latest_by = 'no'
        managed = False
        db_table = 'report'


# # 讀書規劃(舊)
# class Plan(models.Model):
#     no = models.AutoField(primary_key=True, auto_created=True)
#     user = models.ForeignKey(User, models.DO_NOTHING)
#     name = models.CharField(max_length=100)
#     pace = models.IntegerField()
#     datetime = models.DateTimeField(auto_now_add=True)
#     ftime = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'plan'

# 讀書規劃test
class Pace(models.Model):
    no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'pace'


class Plan(models.Model):
    no = models.AutoField(primary_key=True, auto_created=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    name = models.CharField(max_length=100)
    pace_no = models.ForeignKey(Pace, models.DO_NOTHING)
    datetime = models.DateTimeField(auto_now_add=True)
    ftime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'plan'


# 成就輔助
class Success(models.Model):
    no = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=40)
    pace = models.IntegerField()
    classroom_no = models.ForeignKey(Classroom, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'success'


# 成就列表
class Success_list(models.Model):
    no = models.AutoField(primary_key=True, auto_created=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    success_no = models.ForeignKey(Success, models.DO_NOTHING)
    pace = models.IntegerField()
    lockif = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'success_list'


# 討論室
class Discussroom(models.Model):
    no = models.AutoField(primary_key=True, auto_created=True)
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
    no = models.AutoField(primary_key=True,auto_created=True)
    discussroom_no = models.ForeignKey(Discussroom, models.DO_NOTHING)
    user = models.ForeignKey(User, models.DO_NOTHING)
    comment = models.CharField(max_length=1000)
    datetime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discussroom_record'


# 討論室提問
class Discussroom_question(models.Model):
    no = models.AutoField(primary_key=True,auto_created=True)
    discussroom_no = models.ForeignKey(Discussroom, models.DO_NOTHING)
    quser = models.ForeignKey(User, models.DO_NOTHING)
    title = models.CharField(max_length=1000)
    datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discussroom_question'


# 討論室提問答案
class Discussroom_ans(models.Model):
    no = models.AutoField(primary_key=True,auto_created=True)
    question_no = models.ForeignKey(Discussroom_question, models.DO_NOTHING)
    auser = models.ForeignKey(User, models.DO_NOTHING)
    comment = models.CharField(max_length=1000)
    datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    # datetime = models.DateField(blank=True, null=True)

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
    no = models.AutoField(primary_key=True,auto_created=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    reason = models.CharField(max_length=1000)
    discussroom_no = models.ForeignKey(Discussroom, models.DO_NOTHING)
    datetime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'impeach'

# # 日報表圖表資訊
# class Day_subinterval_view(models.Model):
#     user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
#     subject_no_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
#     user_daysubtotal_hours = models.DecimalField(max_digits=19,decimal_places=2)
#
#     class Meta:
#         managed = False
#         db_table = 'day_subinterval_view'

# 日報表圖表資訊(old)
# class Day_subinterval_view(models.Model):
#     user = models.CharField(max_length=100)
#     subject_no_id = models.IntegerField()
#     user_daysubtotal_hours = models.DecimalField(max_digits=19, decimal_places=2)
#
#     class Meta:
#         unique_together = [['user', 'subject_no_id']]
#         # unique_together = (("user", "subject_no_id"),)
#         managed = False
#         db_table = 'day_subinterval_view'


# 日報表圖表資訊
class Day_subcinterval_view(models.Model):
    combinef = models.TextField(primary_key=True, max_length=100)
    # user_id = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subject_no = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    # subject_no_id = models.IntegerField()
    user_daysubtotal_hours = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'day_subcinterval_view'

# 日報表國文直條圖
class Chinese_day_view(models.Model):
    combinef = models.TextField(primary_key=True, max_length=100)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subject_no = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    user_daysubtotal_hours = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'chinese_day_view'

# 日報表英文直條圖
class English_day_view(models.Model):
    combinef = models.TextField(primary_key=True, max_length=100)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subject_no = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    user_daysubtotal_hours = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'english_day_view'

# 日報表數學直條圖
class Math_day_view(models.Model):
    combinef = models.TextField(primary_key=True, max_length=100)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subject_no = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    user_daysubtotal_hours = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'math_day_view'

# 日報表自然直條圖
class Science_day_view(models.Model):
    combinef = models.TextField(primary_key=True, max_length=100)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subject_no = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    user_daysubtotal_hours = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'science_day_view'

# 日報表社會直條圖
class Social_day_view(models.Model):
    combinef = models.TextField(primary_key=True, max_length=100)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subject_no = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    user_daysubtotal_hours = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'social_day_view'

# 日報表其他直條圖
class Other_day_view(models.Model):
    combinef = models.TextField(primary_key=True, max_length=100)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subject_no = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    user_daysubtotal_hours = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'other_day_view'

# 日報表讀書規劃
class Dplan_filter_view(models.Model):
    no = models.AutoField(primary_key=True, auto_created=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    name = models.CharField(max_length=100)
    pace_no = models.ForeignKey(Pace, models.DO_NOTHING)
    datetime = models.DateTimeField(auto_now_add=True)
    ftime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dplan_filter_view'

# # 週報表圖表資訊
# class Week_subinterval_view(models.Model):
#     user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
#     subject_no_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
#     user_daysubtotal_hours = models.DecimalField(max_digits=19, decimal_places=2)
#
#     class Meta:
#         managed = False
#         db_table = 'week_subinterval_view'

# 週報表圖表資訊
class Weekreport_subinterval_view(models.Model):
    combinef = models.TextField(primary_key=True, max_length=100)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subject_no = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    user_total_hours = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'weekreport_subinterval_view'

# # 週報表讀書規劃
# class Weekplan_fliter_view(models.Model):
#     no = models.AutoField(primary_key=True, auto_created=True)
#     user = models.ForeignKey(User, models.DO_NOTHING)
#     name = models.CharField(max_length=100)
#     pace = models.IntegerField()
#     datetime = models.DateTimeField(auto_now_add=True)
#     ftime = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'weekplan_filter_view'
# 週報表讀書規劃
class Wplan_fliter_view(models.Model):
    no = models.AutoField(primary_key=True, auto_created=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    name = models.CharField(max_length=100)
    pace_no = models.ForeignKey(Pace, models.DO_NOTHING)
    datetime = models.DateTimeField(auto_now_add=True)
    ftime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wplan_filter_view'

# 今日日期
class Day_view(models.Model):
    current_date = models.DateField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'day_view'

# 本週日期
class Weekdate_view(models.Model):
    startdate = models.DateField(primary_key=True)
    secdate = models.DateField()
    thirddate = models.DateField()
    forthdate = models.DateField()
    fifdate = models.DateField()
    sixdate = models.DateField()
    enddate = models.DateField()

    class Meta:
        managed = False
        db_table = 'weekdate_view'

#本週日期時間
class Weekdatetime_final_view(models.Model):
    startdate = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'weekdatetime_final_view'

# 多人自習室本日累積人數
class Countnum_view(models.Model):
    num = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'countnum_view'

# 週報表國文堆疊圖
class Chinese_week_view(models.Model):
    combinef = models.TextField(primary_key=True, max_length=100)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subject_no = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    subtotal_hours = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'chinese_final_view'

# 週報表英文堆疊圖
class English_week_view(models.Model):
    combinef = models.TextField(primary_key=True, max_length=100)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subject_no = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    subtotal_hours = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'english_final_view'

# 週報表數學堆疊圖
class Math_week_view(models.Model):
    combinef = models.TextField(primary_key=True, max_length=100)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subject_no = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    subtotal_hours = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'math_final_view'

# 週報表社會堆疊圖
class Social_week_view(models.Model):
    combinef = models.TextField(primary_key=True, max_length=100)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subject_no = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    subtotal_hours = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'social_final_view'

# 週報表自然堆疊圖
class Science_week_view(models.Model):
    combinef = models.TextField(primary_key=True, max_length=100)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subject_no = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    subtotal_hours = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'science_final_view'

# 週報表其他堆疊圖
class Other_week_view(models.Model):
    combinef = models.TextField(primary_key=True, max_length=100)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subject_no = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    subtotal_hours = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'other_final_view'

# 成就總讀書時長
class All_tot_time_view(models.Model):
    user_id = models.TextField(primary_key=True, max_length=100)
    total_min = models.DecimalField(max_digits=19, decimal_places=2)


    class Meta:
        managed = False
        db_table = 'all_tot_time_view'

# 成就dis總讀書時長
class Dis_tot_time_view(models.Model):
    user_id = models.TextField(primary_key=True, max_length=100)
    dis_total_min = models.DecimalField(max_digits=19, decimal_places=2)


    class Meta:
        managed = False
        db_table = 'dis_tot_time_view'

# 成就study總讀書時長
class Study_tot_time_view(models.Model):
    user_id = models.TextField(primary_key=True, max_length=100)
    study_total_min = models.DecimalField(max_digits=19, decimal_places=2)


    class Meta:
        managed = False
        db_table = 'study_tot_time_view'

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
