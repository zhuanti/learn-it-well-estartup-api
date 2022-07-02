from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Plan

# 每一個測試的api_view,一次只能取消註解一個

from utils.decorators import user_login_required


# 學習規劃測試
@api_view()
@user_login_required
def get_all_reviews_test(request):
    plans = Plan.objects.all()

    return Response({
        'success': True,
        'data': [
            {
                'no': plan.pk,
                'user': plan.user.pk,
                'pace': plan.pace,
            }
            for plan in plans
        ]
    })