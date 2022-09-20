from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError

from api.models import Plan

# 每一個測試的api_view,一次只能取消註解一個

from utils.decorators import user_login_required

# 學習規劃新增
@api_view(['POST'])
@user_login_required
def addplan(request):
    data = request.data
    # 新增
    try:
        Plan.objects.create(no=data['no'],
                            user_id=data['user_id'],
                            name=data['name'],
                            pace=0,
                            # 0為未完成,1為完成
                            datetime=data['datetime'], )

        return Response({'success': True, 'message': '新增成功'})

    except IntegrityError:
        return Response({'success': False, 'message': '新增失敗'}, status=status.HTTP_409_CONFLICT)




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
