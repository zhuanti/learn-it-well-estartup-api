from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError

from api.models import Plan
import datetime
# 每一個測試的api_view,一次只能取消註解一個

from utils.decorators import user_login_required


# 學習規劃新增
@api_view(['POST'])
@user_login_required
def addplan(request):
    data = request.data
    user_id = request.session['user_id']
    # 新增
    try:
        Plan.objects.create(
            user_id=user_id,
            name=data['name'],
            pace=0,
            # 0為未完成,1為完成
            datetime=datetime.datetime.now())

        return Response({'success': True, 'message': '新增成功'})

    except IntegrityError:
        return Response({'success': False, 'message': '新增失敗'}, status=status.HTTP_409_CONFLICT)


# 學習規劃編輯
@api_view(['POST'])
@user_login_required
def editplan(request):
    data = request.data

    no = data.get('no')
    plans = Plan.objects.filter(no=no)
    if not plans.exists():
        return Response({'success': False, 'message': '沒有此讀書規劃'}, status=status.HTTP_404_NOT_FOUND)

    try:
        plans.update(name=data['name'], pace=data['pace'], datetime=data['datetime'])
        return Response({'success': True, 'message': '編輯成功'})
    except:
        return Response({'success': False, 'message': '編輯失敗'}, status=status.HTTP_400_BAD_REQUEST)


# 學習規劃測試
@api_view()
@user_login_required
def get_all_reviews_test(request):
    # plans = Plan.objects.all()
    data = request.data

    user_id = data.get('user_id')
    plans = Plan.objects.filter(user_id=user_id)
    if not plans.exists():
        return Response({'success': False, 'message': '沒有此帳號讀書計畫'}, status=status.HTTP_404_NOT_FOUND)
    # if not in2.exists():
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


# 學習規劃刪除
@api_view(['POST'])
@user_login_required
def deleteplan(request):
    data = request.data

    no = data.get('no')
    plans = Plan.objects.filter(no=no)

    if not plans.exists():
        return Response({'success': False, 'message': '沒有此讀書規劃'}, status=status.HTTP_404_NOT_FOUND)
    try:
        plans.delete()
        return Response({'success': True, 'message': '刪除成功'})

    except IntegrityError:
        return Response({'success': False, 'message': '刪除失敗'}, status=status.HTTP_400_BAD_REQUEST)
