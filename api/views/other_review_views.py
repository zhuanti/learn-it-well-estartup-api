from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Impeach, Studyroom


from utils.decorators import user_login_required


# 自習室列表
@api_view()
@user_login_required
def get_all_reviews_studyroom(request):
    studyrooms = Studyroom.objects.all()

    return Response({
        'success': True,
        'data': [
            {
                'no': studyroom.pk,
                'name': studyroom.name,
                'total_people': studyroom.total_people,
            }
            for studyroom in studyrooms
        ]
    })

# 每一個測試的api_view,一次只能取消註解一個

# 檢舉測試
@api_view()
@user_login_required
def get_all_reviews_impeach_test(request):
    impeachs = Impeach.objects.all()

    return Response({
        'success': True,
        'data': [
            {
                'no': impeach.pk,
                'user': impeach.user.pk,
                'reason': impeach.reason,
            }
            for impeach in impeachs
        ]
    })

# 自習室測試
@api_view()
@user_login_required
def get_all_reviews_studyroom_test(request):
    studyrooms = Studyroom.objects.all()

    return Response({
        'success': True,
        'data': [
            {
                'no': studyroom.pk,
                'name': studyroom.name,
                'total_people': studyroom.total_people,
            }
            for studyroom in studyrooms
        ]
    })