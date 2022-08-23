from json import JSONDecodeError

from django.db import IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Settime
# from api.models import Subject, Studyroom

# 每一個測試的api_view,一次只能取消註解一個

from utils.decorators import user_login_required


# @api_view()
# @user_login_required
# def get_all_reviews(request, pk):
#     subjects = Subject.objects.all()
#     try:
#         studyroom = Studyroom.objects.get(pk=pk)
#     except:
#         return Response({'success': False, 'message': '查無此房間'}, status=status.HTTP_404_NOT_FOUND)
#     return Response({
#         'success': True,
#         'data':
#             {
#                 # 自習室
#                 'no': studyroom.pk,
#                 'study_name': studyroom.name,
#                 'study_sub_names': [
#                     {  # 科目
#                         'sub_no': subject.no,
#                         'sub_name': subject.name,
#                     }
#                     for subject in subjects
#                 ]
#
#             }
#
#     })

@api_view()
@user_login_required
def get_selfall_reviews(request):
    settimes = Settime.objects.all()

    return Response({
        'success': True,
        'data': [
            {
                'no': settime.pk,
                'time': settime.time,
            }
            for settime in settimes

        ]
    })


# # 新增時間
# @api_view(['POST'])
# @user_login_required
# def addtime(request):
#     data = request.data
#     # 新增
#     try:
#         Settime.objects.create(no=data['no'],
#                                time=data['time'], )
#
#         return Response({'success': True, 'message': '新增成功'})
#
#     except IntegrityError:
#         return Response({'success': False, 'message': '新增失敗'}, status=status.HTTP_409_CONFLICT)
