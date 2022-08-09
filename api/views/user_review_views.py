from rest_framework import status
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
    # get(pk=pk) all()

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


# 個人資料編輯
@api_view(['POST'])
@user_login_required
def user_detail_edit(request):
    data = request.data
    # data = request.query_params
    user_id = data.get('user_id')

    user = User.objects.filter(pk=user_id)

    try:
        user.update(name=data['name'], live=data['live'], borth=data['borth'])
        return Response({'success': True, 'message': '編輯成功'})
    except:
        return Response({'success': False, 'message': '編輯失敗'}, status=status.HTTP_400_BAD_REQUEST)
