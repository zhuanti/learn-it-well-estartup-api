from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Report

# 每一個測試的api_view,一次只能取消註解一個

# 讀書時長報表測試
@api_view()
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