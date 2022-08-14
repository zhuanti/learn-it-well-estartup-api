from django.db import IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Report

from utils.decorators import user_login_required


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
                'set_time': report.set_time,
            }
            for report in reports
        ]
    })


# 新增科目
@api_view(['POST'])
@user_login_required
def addsub(request):
    data = request.data
    # 新增
    try:
        Report.objects.create(no=data['no'],
                              user_id=data['user_id'],
                              classroom_type_no_id=data['classroom_type_no_id'],
                              subject_no_id=data['subject_no_id'],
                              set_time=data['set_time'],
                              subject_detail=data['subject_detail'], )

        return Response({'success': True, 'message': '新增成功'})

    except IntegrityError:
        return Response({'success': False, 'message': '新增失敗'}, status=status.HTTP_409_CONFLICT)
