import django_filters
from django import forms
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Impeach, Studyroom, Settime, Subject
from api.models import Settime

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


# 個人自習室設定時間及科目
@api_view()
@user_login_required
def setthings(request):

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
