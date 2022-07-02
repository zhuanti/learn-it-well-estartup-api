from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import User

# 除了取得資料其他都用post
from utils.decorators import user_login_required


@api_view(['POST'])
def login(request):
    data = request.data

    if 'user_id' in request.session:
        return Response({'success': False, 'message': '已登入過'}, status=status.HTTP_403_FORBIDDEN)

    try:
        user = User.objects.get(pk=data['id'], pwd=data['pwd'])
    except:
        return Response({'success': False, 'message': '登入失敗，帳號或密碼錯誤'}, status=status.HTTP_404_NOT_FOUND)

    request.session['user_id'] = user.id
    request.session.save()
    return Response({'success': True, 'message': '登入成功', 'sessionid': request.session.session_key})

@api_view(['POST'])
@user_login_required
def logout(request):
    data = request.data
    request.session.flush()
    return Response({'success': True, 'message': '登出成功'})

