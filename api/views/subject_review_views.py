from json import JSONDecodeError

from django.db import IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Subject, Studyroom, Settime, Report

# 每一個測試的api_view,一次只能取消註解一個

from utils.decorators import user_login_required

# 多人自習室抓取時間及科目
@api_view()
@user_login_required
def get_all_reviews(request, pk):
    subjects = Subject.objects.all()
    settimes = Settime.objects.all()
    try:
        studyroom = Studyroom.objects.get(pk=pk)
    except:
        return Response({'success': False, 'message': '查無此房間'}, status=status.HTTP_404_NOT_FOUND)
    return Response({
        'success': True,
        'data':
            {
                # 自習室
                'no': studyroom.pk,
                'study_name': studyroom.name,
                'study_sub_names': [
                    {  # 科目
                        'sub_no': subject.no,
                        'sub_name': subject.name,
                    }
                    for subject in subjects
                ],
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

@api_view()
@user_login_required
def get_selfall_reviews(request):
    subjects = Subject.objects.all()

    return Response({
        'success': True,
        'data': [
            {
                'no': subject.pk,
                'name': subject.name,
            }
            for subject in subjects

        ]
    })
