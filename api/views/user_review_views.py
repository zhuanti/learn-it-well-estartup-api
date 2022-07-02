from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import User

# 將被auth_views取代
# 每一個測試的api_view,一次只能取消註解一個

# 使用者列表測試
@api_view()
def get_all_reviews_test(request):
    users = User.objects.all()

    return Response({
        'success': True,
        'data': [
            {
                'id': user.pk,
                'name': user.name,
                'gender': user.gender,
                'live': user.live,
                'borth': user.borth,
            }
            for user in users
        ]
    })