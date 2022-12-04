from django.db import IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Report, Subject, User, Dplan_filter_view, Day_subcinterval_view, Wplan_fliter_view, \
    Weekreport_subinterval_view, Success_list, Success, Pace, Day_view, Countnum_view, Weekdate_view, Chinese_day_view, \
    English_day_view, Math_day_view, Science_day_view, Social_day_view, Other_day_view, Chinese_week_view, \
    English_week_view, Math_week_view, Science_week_view, Social_week_view, Other_week_view, Weekdatetime_final_view

from utils.decorators import user_login_required

import datetime

from django.db.models import Max


#
# from datetime import datetime


# 每一個測試的api_view,一次只能取消註解一個

# 讀書時長報表測試
@api_view()
@user_login_required
def get_all_reviews_test(request):
    reports = Report.objects.all()

    return Response({
        'success': True,
        'data': [
            {
                'no': report.pk,
                'classroom_type_no': report.classroom_type_no.pk,
                'set_time': report.settime_no.pk,
            }
            for report in reports
        ]
    })

# 日報表讀書規劃
# @api_view()
# @user_login_required
# def get_plan_day(request):
#     data = request.query_params
#
#     user_id = data.get('user_id')
#     plans = Dayplan_filter_view.objects.filter(user_id=user_id)
#     if not plans.exists():
#         return Response({'success': False, 'message': '本日無讀書規劃'}, status=status.HTTP_404_NOT_FOUND)
#     return Response({
#         'success': True,
#         'data': [
#             {
#                 'no': plan.pk,
#                 'user': plan.user.pk,
#                 'name': plan.name,
#                 'pace': plan.pace,
#             }
#             for plan in plans
#         ]
#     })

# 週報表讀書規劃
# @api_view()
# @user_login_required
# def get_plan_week(request):
#     data = request.query_params
#
#     user_id = data.get('user_id')
#     plans = Weekplan_fliter_view.objects.filter(user_id=user_id)
#     if not plans.exists():
#         return Response({'success': False, 'message': '本週無讀書規劃'}, status=status.HTTP_404_NOT_FOUND)
#     return Response({
#         'success': True,
#         'data': [
#             {
#                 'no': plan.pk,
#                 'user': plan.user.pk,
#                 'name': plan.name,
#                 'pace': plan.pace,
#             }
#             for plan in plans
#         ]
#     })

# 日報表圖表資訊取得
# @api_view()
# @user_login_required
# def get_chartreport_day(request):
#     data = request.query_params
#     user = data.get('user_id')
#     user = str(user).strip()
#
#     rinfos = Day_subcinterval_view.objects.filter(user=user)
#
#     if not rinfos.exists():
#         return Response({'success': False, 'message': '未查詢到'}, status=status.HTTP_404_NOT_FOUND)
#
#     return Response({
#         'success': True,
#         'data': [
#             {
#                 'combinef': rinfo.pk,
#                 'user_id': rinfo.user.pk,
#                 'subject_no_id': rinfo.subject_no.pk,
#                 'user_daysubtotal_hours': rinfo.user_daysubtotal_hours
#             }
#             for rinfo in rinfos
#         ]
#     })

# 週報表圖表資訊取得
# @api_view()
# @user_login_required
# def get_chartreport_week(request):
#     data = request.query_params
#     user = data.get('user_id')
#     user = str(user).strip()
#
#     rinfos = Weekreport_subinterval_view.objects.filter(user=user)
#
#     if not rinfos.exists():
#         return Response({'success': False, 'message': '未查詢到'}, status=status.HTTP_404_NOT_FOUND)
#
#     return Response({
#         'success': True,
#         'data': [
#             {
#                 'combinef': rinfo.pk,
#                 'user_id': rinfo.user.pk,
#                 'subject_no_id': rinfo.subject_no.pk,
#                 'user_total_hours': rinfo.user_total_hours
#             }
#             for rinfo in rinfos
#         ]
#     })

# 新增科目(根據登入的使用帳號做新增)
@api_view(['POST'])
@user_login_required
def addsub(request):
    # 學姊寫法同樣可在postman使用https://hsinyi-lin.gitbook.io/django-rest-api-orm/book-reviews/1.%E6%96%B0%E5%A2%9E%E8%A9%95%E8%AB%96
    data = request.data
    user_id = request.session['user_id']
    # 新增
    try:
        Report.objects.create(user_id=user_id,
                              classroom_type_no_id=2,
                              subject_no_id=data['subject_no_id'],
                              settime_no_id=data['settime_no_id'],
                              subject_detail=data['subject_detail'], )

        return Response({'success': True, 'message': '新增成功'})
    except IntegrityError:
        return Response({'success': False, 'message': '新增失敗'}, status=status.HTTP_409_CONFLICT)

    subjects = Subject.objects.filter(subject_no_id=report.subject_no)
    return Response({
        'success': True,
        'data':
            {
                'no': report.pk,
                'user_id': report.user_id,
                'classroom_type_no': report.classroom_type_no.pk,
                'subject_no': report.subject_no.pk,
                'settime_no': report.settime_no.pk,
                'subject_detail': report.subject_detail,
                'subject': [
                    {
                        'sub_no': subject.no,
                        'sub_name': subject.name
                    } for subject in subjects
                ]
            }
    })


@api_view(['POST'])
@user_login_required
def disinout(request):
    data = request.data
    user_id = request.session['user_id']
    # try:
    report = Report.objects.create(no=data['no'],
                                   user_id=user_id,
                                   classroom_type_no_id=data['classroom_type_no_id'],
                                   # subject_no_id=data['subject_no_id'],
                                   # subject_detail=data['subject_detail'],
                                   entry_time=data['entry_time'],
                                   exit_time=data['exit_time'],
                                   total_time=data['total_time'], )

    return Response({'success': True, 'message': '新增成功'})
    report = Report.objects.filter(user_id=report.user_id)
    return Response({
        'success': True,
        'data':
            {
                'no': report.pk,
                'user_id': report.user_id,
                'classroom_type_no': report.classroom_type_no.pk,
                # 'subject_no': report.subject_no.pk,
                # 'settime_no': report.settime_no.pk,
                # 'subject_detail': report.subject_detail,
                'subject': [
                    {
                        'sub_no': subject.no,
                        'sub_name': subject.name
                    } for subject in subjects
                ],
                'entry_time': report.entry_time,
                'exit_time': report.exit_time,
                'total_time': report.total_time,
            }
    })


# 照著其他人寫的新增所寫的，postman成功
# data = request.data
# user_id = request.session['user_id']
# # 新增
# # try:
# report = Report.objects.create(no=data['no'],
#                                user_id=user_id,
#                                classroom_type_no_id=data['classroom_type_no_id'],
#                                subject_no_id=data['subject_no_id'],
#                                settime_no_id=data['settime_no_id'],
#                                subject_detail=data['subject_detail'], )
# # entry_time=data['entry_time'],
# # exit_time=data['exit_time'], )
#
# return Response({'success': True, 'message': '新增成功'})
#
# except IntegrityError:
#     return Response({'success': False, 'message': '新增失敗'}, status=status.HTTP_409_CONFLICT)
#


# 取得使用者填寫讀書資訊
@api_view()
@user_login_required
def get_reviews_insideshow(request):
    data = request.data
    # data = request.query_params
    # data = request.GET
    user_id = data.get('user_id')
    # (下方取得時間去做比較的搭配)
    # 1. start = datetime.timedelta(hours=23, minutes=59, seconds=59)
    # user_id = str(user_id).strip()
    informations = Report.objects.filter(user_id=user_id)
    # 嘗試過取得最新此使用者的紀錄寫法 (含錯誤的顯示)
    # informations = Report.objects.aggregate(max_id=Max('no')) informations.get('max_id') ->AttributeError at /api/report/inside/ 'str' object has no attribute 'pk'
    # informations = Report.objects.all().order_by("-no")[0] ->TypeError at /api/report/inside/ 'Report' object is not iterable
    # 1. in2 = informations.exclude(entry_time__gte=start)/informations = Report.objects.filter(user_id=user_id, entry_time_gte=start) ->AttributeError at /api/report/inside/ type object 'datetime.datetime' has no attribute 'timedelta'
    # in2 = informations.aggregate(Max('no'))/in2 = Report.objects.all().aggregate(Max('no')) ->AttributeError at /api/report/inside/ 'dict' object has no attribute 'exists'
    # in2 = in1.filter().latest('no')
    # last = Report.obejcts.order_by('pk').last()

    # informations = Reports.objects.all()
    if not informations.exists():
        return Response({'success': False, 'message': '沒有此帳號最新讀書設定'}, status=status.HTTP_404_NOT_FOUND)
    # if not in2.exists():
    #     return Response({'success': False, 'message': '沒有此帳號最新讀書設定'}, status=status.HTTP_404_NOT_FOUND)

    return Response({
        'success': True,
        'data': [
            {
                'no': information.pk,
                'user_id': information.user_id,
                'classroom_type_no': information.classroom_type_no.pk,
                'subject_no': information.subject_no.pk,
                'settime_no': information.settime_no.pk,
                'subject_detail': information.subject_detail,
            }
            for information in informations

        ]
    })


# 取得fk內容寫法(按照學姊的寫)https://hsinyi-lin.gitbook.io/django-rest-api-orm/book-reviews/1.%E6%96%B0%E5%A2%9E%E8%A9%95%E8%AB%96
# reports = Report.objects.all()
#
# return Response({
#     'success': True,
#     'data': [
#         {
#             'no': report.pk,
#             'user_id': report.user_id,
#             'classroom_type_no': report.classroom_type_no.pk,
#             'subject_no_id': report.subject_no.pk,
#             'set_time': report.settime_no.pk,
#             'subject_detail': report.subject_detail,
#         }
#         for report in reports
#     ]
# })
# data = request.data
# user_id = data.get('user_id')
#
# user_id = str(user_id).strip()
#
# informations = Reports.objects.filter(user_id=user_id)
#
# # informations = Reports.objects.all()
# if not informations.exists():
#     return Response({'success': False, 'message': '沒有此帳號最新讀書設定'}, status=status.HTTP_404_NOT_FOUND)
#
# return Response({
#     'success': True,
#     'data': [
#         {
#             'no': information.pk,
#             'user_id': information.user_id,
#             'classroom_type_no_id': information.classroom_type_no_id,
#             'subject_no_id': information.subject_no_id,
#             'settime_no_id': information.settime_no_id,
#             'subject_detail': information.subject_detail,
#         }
#         for information in informations
#
#     ]
# })

# 抓取所有report裡面的資料
@api_view()
@user_login_required
def get_reviews_reportdata(request):
    informations = Report.objects.all()

    return Response({
        'success': True,
        'data': [
            {
                'no': information.pk,
                'user_id': information.user_id,
                'classroom_type_no': information.classroom_type_no.pk,
                'subject_no': information.subject_no.pk,
                'settime_no': information.settime_no.pk,
                'subject_detail': information.subject_detail,
            }
            for information in informations

        ]
    })


# 抓取特定使用者report裡面的資料(若使用者同時具有多筆紀錄會失敗)
# mydata = Members.objects.all().order_by('firstname').values()
# SELECT * FROM members ORDER BY firstname;
# select * from report where user_id = 'test@gmail.com' order by "no"  desc limit 1
# 個人自習室顯示
@api_view()
@user_login_required
def get_reviews_report_test(request):
    data = request.query_params

    user_id = data.get('user_id')
    user_id = str(user_id).strip()

    reports = Report.objects.filter(user_id=user_id)

    if not reports.exists():
        return Response({'success': False, 'message': '沒有此帳號'}, status=status.HTTP_404_NOT_FOUND)

    report = reports.latest()

    return Response({
        'success': True,
        'data':
            {
                'no': report.pk,
                'user_id': report.user_id,
                'classroom_type_no': report.classroom_type_no.pk,
                'subject_no': report.subject_no.pk,
                'subject_no_lists': [
                    {

                        'sub_no': subject.pk,
                        'sub_name': subject.name,
                    }
                    for subject in Subject.objects.filter(no=report.subject_no.pk)
                ],
                'settime_no': report.settime_no.pk,
                'subject_detail': report.subject_detail,
            }
    })


# 開始結束時間資料編輯
@api_view(['POST'])
@user_login_required
def report_recordtime_edit(request):
    data = request.query_params
    # data = request.query_params
    user_id = data.get('user_id')
    user_id = str(user_id).strip()

    records = Report.objects.filter(user_id=user_id)

    if not records.exists():
        return Response({'success': False, 'message': '沒有此帳號最新讀書設定'}, status=status.HTTP_404_NOT_FOUND)

    record = records.latest()
    try:
        record.update(entry_time=datetime.datetime.now(), exit_time=datetime.datetime.now())
        return Response({'success': True, 'message': '編輯成功'})
    except:
        return Response({'success': False, 'message': '編輯失敗'}, status=status.HTTP_400_BAD_REQUEST)

# 報表每周基底測試
@api_view(['POST'])
@user_login_required
def add_report_week(request):
    data = request.query_params
    subject_nos = Subject.objects.all()
    week_days = Weekdatetime_final_view.objects.all()
    # try:
    for subject_no in subject_nos:
        for week_day in week_days:
            Report.objects.create(user_id=data['user_id'],
                                  classroom_type_no_id="4",
                                  subject_no_id=subject_no.pk,
                                  settime_no_id="5",
                                  entry_time=week_day.pk,
                                  exit_time=week_day.pk)

    return Response({'success': True, 'message': '新增成功'})

    # except IntegrityError:
    #     return Response({'success': False, 'message': '新增失敗'}, status=status.HTTP_409_CONFLICT)


# 報表個人資料週顯示頁面
@api_view()
@user_login_required
def get_report_week(request):
    # users = User.objects.all()
    data = request.query_params
    user_id = data.get('user_id')
    user_id = str(user_id).strip()
    # data = request.data

    user = User.objects.get(pk=user_id)
    wplans = Wplan_fliter_view.objects.filter(user=user_id)
    wsuccesslists = Success_list.objects.filter(user=user_id)
    rinfos = Weekreport_subinterval_view.objects.filter(user=user_id)
    cinfos = Chinese_week_view.objects.filter(user=user_id)
    einfos = English_week_view.objects.filter(user=user_id)
    minfos = Math_week_view.objects.filter(user=user_id)
    sinfos = Science_week_view.objects.filter(user=user_id)
    soinfos = Social_week_view.objects.filter(user=user_id)
    oinfos = Other_week_view.objects.filter(user=user_id)
    # weekdates = Weekdate_view.objects.all()

    subject_nos = Subject.objects.all()
    week_days = Weekdatetime_final_view.objects.all()
    for subject_no in subject_nos:
        for week_day in week_days:
            Report.objects.create(user_id=data['user_id'],
                                  classroom_type_no_id="4",
                                  subject_no_id=subject_no.pk,
                                  settime_no_id="5",
                                  entry_time=week_day.pk,
                                  exit_time=week_day.pk)

    return Response({
        'success': True,
        'data':
            {
                'wuser_lists': [
                    {
                        'name': user.name,
                        'id': user.pk,
                        'gender': user.gender,
                        'live': user.live,
                        'borth': user.borth,
                    }
                ],

                'wplan_lists': [
                    {
                        'no': wplan.pk,
                        'user': wplan.user.pk,
                        'name': wplan.name,
                        'pace_no': wplan.pace_no.pk,
                        'datetime': wplan.datetime,
                        'pace_names': [
                            {
                                'no': pace.pk,
                                'name': pace.name,
                            }
                            for pace in Pace.objects.filter(pk=wplan.pace_no.pk)
                        ],
                    }
                    for wplan in wplans
                ],
                'wsuccess_lists': [
                    {
                        'no': wsuccesslist.pk,
                        'user_id': wsuccesslist.user.pk,
                        'success_no': wsuccesslist.success_no.pk,
                        'pace': wsuccesslist.pace,
                        'lockif': wsuccesslist.lockif,
                        'success_names': [
                            {
                                'suc_no': success.no,
                                'suc_name': success.name,
                                'suc_pace': success.pace,
                            }
                            for success in Success.objects.filter(pk=wsuccesslist.success_no.pk)
                        ],
                    }
                    for wsuccesslist in wsuccesslists
                ],
                'wchart_lists': [
                    {
                        'combinef': rinfo.pk,
                        'user_id': rinfo.user.pk,
                        'subject_no_id': rinfo.subject_no.pk,
                        'user_total_hours': rinfo.user_total_hours,
                        'subject_name': [
                            {
                                'sub_no': subject.no,
                                'sub_name': subject.name,
                            }
                            for subject in Subject.objects.filter(pk=rinfo.subject_no.pk)
                        ],
                    }
                    for rinfo in rinfos
                ],
                # 'startdate_lists': [
                #     {
                #         'startdate': wdate.startdate,
                #     }
                #     for wdate in weekdates
                # ],
                # 'secdate_lists': [
                #     {
                #         'secdate': wdate.secdate,
                #     }
                #     for wdate in weekdates
                # ],
                # 'thirddate_lists': [
                #     {
                #         'thirddate': wdate.thirddate,
                #     }
                #     for wdate in weekdates
                # ],
                # 'forthdate_lists': [
                #     {
                #         'forthdate': wdate.forthdate,
                #     }
                #     for wdate in weekdates
                # ],
                # 'fifdate_lists': [
                #     {
                #         'fifdate': wdate.fifdate,
                #     }
                #     for wdate in weekdates
                # ],
                # 'sixdate_lists': [
                #     {
                #         'sixdate': wdate.sixdate,
                #     }
                #     for wdate in weekdates
                # ],
                # 'enddate_lists': [
                #     {
                #         'enddate': wdate.enddate,
                #     }
                #     for wdate in weekdates
                # ],
                'chinese_lists': [
                    {
                        'combinef': cinfo.pk,
                        'user_id': cinfo.user.pk,
                        'subject_no_id': cinfo.subject_no.pk,
                        'subtotal_hours': cinfo.subtotal_hours,
                    }
                    for cinfo in cinfos
                ],
                'english_lists': [
                    {
                        'combinef': einfo.pk,
                        'user_id': einfo.user.pk,
                        'subject_no_id': einfo.subject_no.pk,
                        'subtotal_hours': einfo.subtotal_hours,
                    }
                    for einfo in einfos
                ],
                'math_lists': [
                    {
                        'combinef': minfo.pk,
                        'user_id': minfo.user.pk,
                        'subject_no_id': minfo.subject_no.pk,
                        'subtotal_hours': minfo.subtotal_hours,
                    }
                    for minfo in minfos
                ],
                'science_lists': [
                    {
                        'combinef': sinfo.pk,
                        'user_id': sinfo.user.pk,
                        'subject_no_id': sinfo.subject_no.pk,
                        'subtotal_hours': sinfo.subtotal_hours,
                    }
                    for sinfo in sinfos
                ],
                'social_lists': [
                    {
                        'combinef': soinfo.pk,
                        'user_id': soinfo.user.pk,
                        'subject_no_id': soinfo.subject_no.pk,
                        'subtotal_hours': soinfo.subtotal_hours,
                    }
                    for soinfo in soinfos
                ],
                'other_lists': [
                    {
                        'combinef': oinfo.pk,
                        'user_id': oinfo.user.pk,
                        'subject_no_id': oinfo.subject_no.pk,
                        'subtotal_hours': oinfo.subtotal_hours,
                    }
                    for oinfo in oinfos
                ],
            }
    })
# 今日日期
# @api_view()
# @user_login_required
# def get_day(request):
#     days = Day_view.objects.all()
#
#     return Response({
#         'success': True,
#         'data': [
#             {
#                 'current_date': day.current_date,
#             }
#             for day in days
#         ]
#
#     })
# 本週日期
# @api_view()
# @user_login_required
# def get_week(request):
#     weekdates = Weekdate_view.objects.all()
#
#     return Response({
#         'success': True,
#         'data': {
#             'startdate_lists': [
#                 {
#                     'startdate': wdate.startdate,
#                 }
#                 for wdate in weekdates
#             ],
#             'secdate_lists': [
#                 {
#                     'secdate': wdate.secdate,
#                 }
#                 for wdate in weekdates
#             ],
#             'thirddate_lists': [
#                 {
#                     'thirddate': wdate.thirddate,
#                 }
#                 for wdate in weekdates
#             ],
#             'forthdate_lists': [
#                 {
#                     'forthdate': wdate.forthdate,
#                 }
#                 for wdate in weekdates
#             ],
#             'fifdate_lists': [
#                 {
#                     'fifdate': wdate.fifdate,
#                 }
#                 for wdate in weekdates
#             ],
#             'sixdate_lists': [
#                 {
#                     'sixdate': wdate.sixdate,
#                 }
#                 for wdate in weekdates
#             ],
#             'enddate_lists': [
#                 {
#                     'enddate': wdate.enddate,
#                 }
#                 for wdate in weekdates
#             ]
#         }
#
#     })
# 多人自習室本日累積人數
# @api_view()
# @user_login_required
# def get_countnum_reviews(request):
#     nums = Countnum_view.objects.all()
#
#     return Response({
#         'success': True,
#         'data': [
#             {
#                 'num': num.pk,
#             }
#             for num in nums
#
#         ]
#     })

# 報表個人資料日顯示頁面
@api_view()
@user_login_required
def get_report_day(request):
    # users = User.objects.all()
    data = request.query_params
    user_id = data.get('user_id')
    user_id = str(user_id).strip()
    # data = request.data

    user = User.objects.get(pk=user_id)
    dplans = Dplan_filter_view.objects.filter(user=user_id)
    dsuccesslists = Success_list.objects.filter(user=user_id)
    rinfos = Day_subcinterval_view.objects.filter(user=user_id)
    chineses = Chinese_day_view.objects.filter(user=user_id)
    englishs = English_day_view.objects.filter(user=user_id)
    maths = Math_day_view.objects.filter(user=user_id)
    sciences = Science_day_view.objects.filter(user=user_id)
    socials = Social_day_view.objects.filter(user=user_id)
    others = Other_day_view.objects.filter(user=user_id)
    days = Day_view.objects.all()
    return Response({
        'success': True,
        'data':
            {

                'duser_lists': [
                    {
                        'name': user.name,
                        'id': user.pk,
                        'gender': user.gender,
                        'live': user.live,
                        'borth': user.borth,
                    }
                ],
                'dplan_lists': [
                    {
                        'no': dplan.pk,
                        'user': dplan.user.pk,
                        'name': dplan.name,
                        'pace_no': dplan.pace_no.pk,
                        'datetime': dplan.datetime,
                        'pace_names': [
                            {
                                'no': pace.pk,
                                'name': pace.name,
                            }
                            for pace in Pace.objects.filter(pk=dplan.pace_no.pk)
                        ],
                    }
                    for dplan in dplans
                ],
                'dsuccess_lists': [
                    {
                        'no': dsuccesslist.pk,
                        'user_id': dsuccesslist.user.pk,
                        'success_no': dsuccesslist.success_no.pk,
                        'pace': dsuccesslist.pace,
                        'lockif': dsuccesslist.lockif,
                        'success_names': [
                            {
                                'suc_no': success.no,
                                'suc_name': success.name,
                                'suc_pace': success.pace,
                            }
                            for success in Success.objects.filter(pk=dsuccesslist.success_no.pk)
                        ],
                    }
                    for dsuccesslist in dsuccesslists
                ],
                'dchart_lists': [
                    {
                        'combinef': rinfo.pk,
                        'user_id': rinfo.user.pk,
                        'subject_no_id': rinfo.subject_no.pk,
                        'user_daysubtotal_hours': rinfo.user_daysubtotal_hours,
                        'dsubject_name': [
                            {
                                'sub_no': subject.no,
                                'sub_name': subject.name,
                            }
                            for subject in Subject.objects.filter(pk=rinfo.subject_no.pk)
                        ],
                    }
                    for rinfo in rinfos
                ],
                'day_lists': [
                    {
                        'current_date': day.current_date,
                    }
                    for day in days
                ],
                'chinese_lists': [
                    {
                        'combinef': chinese.pk,
                        'user_id': chinese.user.pk,
                        'subject_no_id': chinese.subject_no.pk,
                        'user_daysubtotal_hours': chinese.user_daysubtotal_hours,
                        'dsubject_name': [
                            {
                                'sub_no': subject.no,
                                'sub_name': subject.name,
                            }
                            for subject in Subject.objects.filter(pk=chinese.subject_no.pk)
                        ],
                    }
                    for chinese in chineses
                ],
                'english_lists': [
                    {
                        'combinef': english.pk,
                        'user_id': english.user.pk,
                        'subject_no_id': english.subject_no.pk,
                        'user_daysubtotal_hours': english.user_daysubtotal_hours,
                        'dsubject_name': [
                            {
                                'sub_no': subject.no,
                                'sub_name': subject.name,
                            }
                            for subject in Subject.objects.filter(pk=english.subject_no.pk)
                        ],
                    }
                    for english in englishs
                ],
                'math_lists': [
                    {
                        'combinef': math.pk,
                        'user_id': math.user.pk,
                        'subject_no_id': math.subject_no.pk,
                        'user_daysubtotal_hours': math.user_daysubtotal_hours,
                        'dsubject_name': [
                            {
                                'sub_no': subject.no,
                                'sub_name': subject.name,
                            }
                            for subject in Subject.objects.filter(pk=math.subject_no.pk)
                        ],
                    }
                    for math in maths
                ],
                'science_lists': [
                    {
                        'combinef': science.pk,
                        'user_id': science.user.pk,
                        'subject_no_id': science.subject_no.pk,
                        'user_daysubtotal_hours': science.user_daysubtotal_hours,
                        'dsubject_name': [
                            {
                                'sub_no': subject.no,
                                'sub_name': subject.name,
                            }
                            for subject in Subject.objects.filter(pk=science.subject_no.pk)
                        ],
                    }
                    for science in sciences
                ],
                'social_lists': [
                    {
                        'combinef': social.pk,
                        'user_id': social.user.pk,
                        'subject_no_id': social.subject_no.pk,
                        'user_daysubtotal_hours': social.user_daysubtotal_hours,
                        'dsubject_name': [
                            {
                                'sub_no': subject.no,
                                'sub_name': subject.name,
                            }
                            for subject in Subject.objects.filter(pk=social.subject_no.pk)
                        ],
                    }
                    for social in socials
                ],
                'other_lists': [
                    {
                        'combinef': other.pk,
                        'user_id': other.user.pk,
                        'subject_no_id': other.subject_no.pk,
                        'user_daysubtotal_hours': other.user_daysubtotal_hours,
                        'dsubject_name': [
                            {
                                'sub_no': subject.no,
                                'sub_name': subject.name,
                            }
                            for subject in Subject.objects.filter(pk=other.subject_no.pk)
                        ],
                    }
                    for other in others
                ],

            }
    })
