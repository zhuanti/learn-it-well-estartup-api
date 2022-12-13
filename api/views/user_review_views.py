import cryptocode
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import User, Success_list, Success, Gender, Live

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
    usersuccesslists = Success_list.objects.filter(user=user_id)

    return Response({
        'success': True,
        'data': {
            'name': user.name,
            'id': user.pk,
            'point': user.point,
            'gender': user.gender.pk,
            'gender_list': [
                {
                    'gender_no': gender.pk,
                    'gender_gender': gender.gender,
                }
                for gender in Gender.objects.filter(no=user.gender.pk)
            ],
            'all_gender_list': [
                {
                    'gender_no': gender.pk,
                    'gender_gender': gender.gender,
                }
                for gender in Gender.objects.all()
            ],
            'live': user.live.pk,
            'live_list': [
                {
                    'live_no': live.pk,
                    'live_name': live.name,
                }
                for live in Live.objects.filter(no=user.live.pk)
            ],
            'all_live_list': [
                {
                    'live_no': live.pk,
                    'live_name': live.name,
                }
                for live in Live.objects.all()
            ],
            'borth': user.borth,
            'usersuccess_lists': [
                {
                    'no': usersuccesslist.pk,
                    'user_id': usersuccesslist.user.pk,
                    'success_no': usersuccesslist.success_no.pk,
                    'pace': usersuccesslist.pace,
                    'lockif': usersuccesslist.lockif,
                    'success_names': [
                        {
                            'suc_no': success.no,
                            'suc_name': success.name,
                            'suc_pace': success.pace,
                        }
                        for success in Success.objects.filter(pk=usersuccesslist.success_no.pk)
                    ],
                }
                for usersuccesslist in usersuccesslists
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
        pwd = cryptocode.encrypt(data['pwd'], '93842')
        user.update(pwd=pwd, name=data['name'], gender=data['gender'], live=data['live'], borth=data['borth'])
        return Response({'success': True, 'message': '編輯成功'})
    except:
        return Response({'success': False, 'message': '編輯失敗'}, status=status.HTTP_400_BAD_REQUEST)
