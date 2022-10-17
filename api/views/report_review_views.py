from django.db import IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Report, Subject, User

from utils.decorators import user_login_required

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


# 新增科目
@api_view(['POST'])
@user_login_required
def addsub(request):
    # 學姊寫法同樣可在postman使用https://hsinyi-lin.gitbook.io/django-rest-api-orm/book-reviews/1.%E6%96%B0%E5%A2%9E%E8%A9%95%E8%AB%96
    data = request.data
    user_id = request.session['user_id']
    # 新增
    # try:
    report = Report.objects.create(user_id=user_id,
                                   classroom_type_no_id=data['classroom_type_no_id'],
                                   subject_no_id=data['subject_no_id'],
                                   settime_no_id=data['settime_no_id'],
                                   subject_detail=data['subject_detail'], )

    return Response({'success': True, 'message': '新增成功'})

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
                                   total_time=data['total_time'],)

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
@api_view()
@user_login_required
def get_reviews_report_test(request):
    # data = request.data
    data = request.query_params
    # data = request.GET
    user_id = data.get('user_id')
    no = data.get('no')

    # 透過特定使用者帳號抓取
    # informations = Report.objects.get(user_id=user_id)
    # 抓取最新的那筆資料
    informations = Report.objects.latest()
    # 透過特定no抓取
    # informations = Report.objects.get(no=no)
    return Response({
        'success': True,
        'data': [
            {
                'no': informations.pk,
                'user_id': informations.user_id,
                'classroom_type_no': informations.classroom_type_no.pk,
                'subject_no': informations.subject_no.pk,
                'settime_no': informations.settime_no.pk,
                'subject_detail': informations.subject_detail,
            }
        ]
    })


# 開始結束時間資料編輯
@api_view(['POST'])
@user_login_required
def report_recordtime_edit(request):
    data = request.data
    # data = request.query_params
    user_id = data.get('user_id')

    record = Report.objects.filter(user_id=user_id)

    if not record.exists():
        return Response({'success': False, 'message': '沒有此帳號最新讀書設定'}, status=status.HTTP_404_NOT_FOUND)

    try:
        record.update(entry_time=data['entry_time'], exit_time=data['exit_time'])
        return Response({'success': True, 'message': '編輯成功'})
    except:
        return Response({'success': False, 'message': '編輯失敗'}, status=status.HTTP_400_BAD_REQUEST)

# 報表個人資料顯示頁面
@api_view()
@user_login_required
def get_report_usernameweek(request):
    # users = User.objects.all()
    data = request.query_params
    user_id = data.get('user_id')

    # data = request.data

    users = User.objects.get(pk=user_id)

    return Response({
        'success': True,
        'data':
            {
                'name': users.name,
                'id': users.pk,
                'gender': users.gender,
                'live': users.live,
                'borth': users.borth,
            }
    })
# user detail那邊寫法
    # return Response({
    #                     'success': True,
    #                     'data': {
    #                         'name': user.name,
    #                         'id': user.pk,
    #                         'gender': user.gender,
    #                         'live': user.live,
    #                         'borth': user.borth,
    #                     }
    # })