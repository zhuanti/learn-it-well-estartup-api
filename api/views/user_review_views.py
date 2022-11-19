from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import User, Success_list, Success

from utils.decorators import user_login_required


# 將被auth_views取代
# 每一個測試的api_view,一次只能取消註解一個

# 測試使用者列表顯示
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


# 顯示使用者個人資料
@api_view()
@user_login_required
def get_user_detail(request):
    data = request.query_params
    user_id = data.get('user_id')

    user = User.objects.get(pk=user_id)
    dsuccesslists = Success_list.objects.filter(user=user_id)

    return Response({
        'success': True,
        'data': {
            'name': user.name,
            'id': user.pk,
            'gender': user.gender,
            'live': user.live,
            'borth': user.borth,
            'dsuccess_lists': [
                {
                    'no': dsuccesslist.pk,
                    'user_id': dsuccesslist.user.pk,
                    'success_no': dsuccesslist.success_no.pk,
                    'pace': dsuccesslist.pace,
                    'lockif': dsuccesslist.lockif,
                    'success_names': [
                        {
                            'suc_no': success.no,
                            'suc_name': success.name,
                            'suc_pace': success.pace,
                        }
                        for success in Success.objects.filter(pk=dsuccesslist.success_no.pk)
                    ],
                }
                for dsuccesslist in dsuccesslists
            ]
        }
    })


# 編輯使用者個人資料
@api_view(['POST'])
@user_login_required
def user_detail_edit(request):
    data = request.data
    user_id = data.get('user_id')

    user = User.objects.filter(pk=user_id)

    if not user.exists():
        return Response({'success': False, 'message': '沒有此帳號'}, status=status.HTTP_404_NOT_FOUND)

    try:
        user.update(pwd=data['pwd'], name=data['name'], live=data['live'], borth=data['borth'])
        return Response({'success': True, 'message': '編輯成功'})
    except:
        return Response({'success': False, 'message': '編輯失敗'}, status=status.HTTP_400_BAD_REQUEST)
