from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import User

from utils.decorators import user_login_required

# 將被auth_views取代
# 每一個測試的api_view,一次只能取消註解一個

# 使用者列表測試
@api_view()
@user_login_required
def get_user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except:
        return Response({'success': False, 'message': '查無資料'}, status=status.HTTP_404_NOT_FOUND)

    return Response({
        'success': True,
        'data': {
                'id': user.id.pk,
                'name': user.name,
                'gender': user.gender,
                'live': user.live,
                'borth': user.borth,
            }
    })