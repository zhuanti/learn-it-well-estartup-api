import base64

import cryptocode as cryptocode
from django.db import IntegrityError

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import User, Gender, Live

from utils.decorators import user_login_required


# 除了取得資料其他都用post
# 登出
@api_view(['POST'])
@user_login_required
def logout(request):
    data = request.data
    request.session.flush()
    return Response({'success': True, 'message': '登出成功'})


# 登入
@api_view(['POST'])
def login(request):
    data = request.data

    if 'user_id' in request.session:
        return Response({'success': False, 'message': '已登入過'}, status=status.HTTP_403_FORBIDDEN)

    try:
        user = User.objects.get(pk=data['id'])
    except:
        return Response({'success': False, 'message': '登入失敗，帳號或密碼錯誤'}, status=status.HTTP_404_NOT_FOUND)

    # request.session['user_id'] = user.id
    # request.session.save()
    # return Response({'success': True, 'message': '登入成功', 'sessionid': request.session.session_key})

    # 解密
    decrypted = cryptocode.decrypt(user.pwd, '93842')

    # 資料表解密後的密碼是否跟使用者傳入的密碼相同
    if decrypted == data['pwd']:
        request.session['user_id'] = user.id
        request.session.save()
        return Response({'success': True, 'message': '登入成功', 'sessionid': request.session.session_key})
    else:
        return Response({'success': False, 'message': '登入失敗，帳號或密碼錯誤'}, status=status.HTTP_404_NOT_FOUND)


# 註冊
@api_view(['POST'])
def register(request):
    data = request.data

    # # 圖片轉base64字串
    # photo = request.FILES['photo']
    # photo_string = str(base64.b64encode(photo.read()))[2:-1]

    # 新增使用者資料
    try:
        # 這邊 encrypt 是雜湊的名稱 (密碼資料,加密形式) 加密形式在登入與註冊的設定要一樣
        pwd = cryptocode.encrypt(data['pwd'], '93842')
        User.objects.create(id=data['id'], pwd=pwd, name=data['name'],
                            gender_id=data['gender'], live_id=data['live'],
                            # photo=data['photo'],
                            # photo=photo_string,
                            borth=data['borth'], purview=data['purview'])

        return Response({'success': True, 'message': '註冊成功'})


    except IntegrityError:
        return Response({'success': False, 'message': '此帳號已被註冊'}, status=status.HTTP_409_CONFLICT)

    except:
        return Response({'success': False, 'message': '輸入格式錯誤，請確認生日及其他欄位的填寫格式'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# 忘記密碼
# @api_view()
@api_view(['POST'])
def forget(request):
    data = request.data

    try:
        user = User.objects.get(id=data['id'])

    except:
        return Response({'success': False, 'message': '查無資料'}, status=status.HTTP_404_NOT_FOUND)

    return Response({
        'success': True,
        'message': '即將發送郵件重設密碼',
        'data':
            {
                'id': user.pk
            }
    })


# 重設忘記密碼
@api_view(['POST'])
def forget_rest(request):
    data = request.data
    id = data.get('id')
    user = User.objects.filter(pk=id)

    if not user.exists():
        return Response({'success': False, 'message': '沒有此帳號'}, status=status.HTTP_404_NOT_FOUND)

    try:
        pwd = cryptocode.encrypt(data['pwd'], '93842')
        user.update(pwd=pwd)
        return Response({'success': True, 'message': '編輯成功'})

    except:
        return Response({'success': False, 'message': '編輯失敗'}, status=status.HTTP_400_BAD_REQUEST)


# 居住地&性別列表
@api_view()
def get_live_gender(request):

    genders = Gender.objects.all()
    lives = Live.objects.all()

    return Response({
        'success': True,
        'data':
            {
                'gender_lists': [
                    {
                        'gender_no': gender.pk,
                        'gender_gender': gender.gender,
                    }
                    for gender in genders
                ],
                'live_lists': [
                    {
                        'live_no': live.pk,
                        'live_name': live.name,
                    }
                    for live in lives
                ],
            }
    })


