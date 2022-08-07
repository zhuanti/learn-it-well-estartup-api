from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import User

from utils.decorators import user_login_required


# 將被auth_views取代
# 每一個測試的api_view,一次只能取消註解一個

# 使用者列表測試
@api_view()
@user_login_required
def get_user_detail_test(request):
    users = User.objects.all()
    #get(pk=pk) all()

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

# 個人資料顯示頁面
@api_view()
@user_login_required
def get_user_detail(request):
    data = request.query_params
    user_id = data.get('user_id')

    # data = request.data

    user = User.objects.get(pk=user_id)

    return Response({
        'success': True,
        'data': {
            'name': user.name,
            'id': user.pk,
            'gender': user.gender,
            'live': user.live,
            'borth': user.borth,
        }
    })
