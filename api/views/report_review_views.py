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
                'set_time': report.settime_no.pk,
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
                              settime_no=data['settime_no'],
                              subject_detail=data['subject_detail'], )

        return Response({'success': True, 'message': '新增成功'})

    except IntegrityError:
        return Response({'success': False, 'message': '新增失敗'}, status=status.HTTP_409_CONFLICT)


# 取得使用者填寫讀書資訊
@api_view()
@user_login_required
def get_reviews_insideshow(request):
    data = request.data
    # data = request.query_params
    # data = request.GET
    user_id = data.get('user_id')

    user_id = str(user_id).strip()

    informations = Report.objects.filter(user_id=user_id)

    # informations = Reports.objects.all()
    if not informations.exists():
        return Response({'success': False, 'message': '沒有此帳號最新讀書設定'}, status=status.HTTP_404_NOT_FOUND)

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
