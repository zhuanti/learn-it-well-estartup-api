import django_filters
from django import forms
from django.db import IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Impeach, Studyroom, Settime, Subject, Report, Plan, User

from utils.decorators import user_login_required


# 每一個測試的api_view,一次只能取消註解一個
# 自習室列表
@api_view()
@user_login_required
def get_all_reviews_studyroom(request):
    studyrooms = Studyroom.objects.all()

    return Response({
        'success': True,
        'data': [
            {
                'no': studyroom.pk,
                'name': studyroom.name,
                'total_people': studyroom.total_people,
            }
            for studyroom in studyrooms
        ]
    })


# 顯示加入房間編號
@api_view()
@user_login_required
def get_room_no(request, pk):
    try:
        studyroom = Studyroom.objects.get(pk=pk)
    except:
        return Response({'success': False, 'message': '查無此房間'}, status=status.HTTP_404_NOT_FOUND)
    return Response({
        'success': True,
        'data':
            {
                'no': studyroom.pk,
                'name': studyroom.name,
                'total_people': studyroom.total_people,
            }
    })


# 個人自習室抓取時間及科目
@api_view()
@user_login_required
def get_studyroom_info(request):
    subjects = Subject.objects.all()
    settimes = Settime.objects.all()

    return Response({
        'success': True,
        'data':
            {
                'set_lists': [
                    {
                        'set_no': settime.pk,
                        'set_time': settime.time,
                    }
                    for settime in settimes
                ],

                'sub_lists': [
                    {
                        'sub_no': subject.pk,
                        'sub_name': subject.name,
                    }
                    for subject in subjects
                ],

            }
    })


# 個人自習室寫入讀書資訊到report
@api_view(['POST'])
@user_login_required
def setthings(request):
    data = request.data
    # 新增
    try:
        Report.objects.create(user_id=data['user_id'],
                              classroom_type_no_id="1",
                              subject_no_id=data['subject_no_id'],
                              settime_no_id=data['settime_no_id'],
                              subject_detail=data['subject_detail'])

        return Response({'success': True, 'message': '新增成功'})


    except IntegrityError:
        return Response({'success': False, 'message': '此房間已寫入'}, status=status.HTTP_409_CONFLICT)


# 多人自習室寫入讀書資訊到report
@api_view(['POST'])
@user_login_required
def msetthings(request):
    data = request.data
    # 新增
    try:
        Report.objects.create(user_id=data['user_id'],
                              classroom_type_no_id="1",
                              subject_no_id=data['subject_no_id'],
                              settime_no_id=data['settime_no_id'],
                              subject_detail=data['subject_detail'])

        return Response({'success': True, 'message': '新增成功'})


    except IntegrityError:
        return Response({'success': False, 'message': '此房間已寫入'}, status=status.HTTP_409_CONFLICT)


# 檢舉測試
@api_view()
@user_login_required
def get_all_reviews_impeach_test(request):
    impeachs = Impeach.objects.all()

    return Response({
        'success': True,
        'data': [
            {
                'no': impeach.pk,
                'user': impeach.user.pk,
                'reason': impeach.reason,
            }
            for impeach in impeachs
        ]
    })


# 自習室測試
@api_view()
@user_login_required
def get_all_reviews_studyroom_test(request):
    studyrooms = Studyroom.objects.all()

    return Response({
        'success': True,
        'data': [
            {
                'no': studyroom.pk,
                'name': studyroom.name,
                'total_people': studyroom.total_people,
            }
            for studyroom in studyrooms
        ]
    })


# 自習室查詢
@api_view()
@user_login_required
def Sserch(request):
    # 注意：因使用GET，使用query_params
    data = request.query_params
    # no = data.get('no')
    name = data.get('name')

    # 去除前後空白
    # no = str(no).strip()
    # if no==None:
    #     no="1"
    name = str(name).strip()
    studyrooms = Studyroom.objects.filter(name=name)

    return Response({
        'success': True,
        'data': [
            {
                'no': studyroom.pk,
                'name': studyroom.name,
                'total_people': studyroom.total_people,
            }
            for studyroom in studyrooms
        ]
    })


# 跑馬燈
@api_view()
@user_login_required
def News(request):
    data = request.query_params
    user_id = data.get('user_id')
    # 過濾使用者+完成度
    plans = Plan.objects.filter(user_id=user_id, pace=0)
    if not plans.exists():
        return Response({'success': False, 'message': '沒有此帳號讀書計畫'}, status=status.HTTP_404_NOT_FOUND)

    return Response({
        'success': True,
        'data': [
            {
                'no': plan.pk,
                # 'user': plan.user.pk,
                'name': plan.name,
                'pace': plan.pace,
                'user': plan.user_id,
                'user_lists': [
                    {

                        'user_no': user.pk,
                        'user_name': user.name,
                    }
                    for user in User.objects.filter(id=plan.user_id)
                ],
            }
            for plan in plans
        ]
    })

