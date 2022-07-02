from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Success, Success_list

from utils.decorators import user_login_required
# 每一個測試的api_view,一次只能取消註解一個

# 成就輔助測試
# @api_view()
# def get_all_reviews_test(request):
#     successes = Success.objects.all()
#
#     return Response({
#         'success': True,
#         'data': [
#             {
#                 'no': success.pk,
#                 'name': success.name,
#                 'pace': success.pace,
#             }
#             for success in successes
#         ]
#     })

# 成就列表測試
@api_view()
@user_login_required
def get_all_reviews_test(request):
    success_lists = Success_list.objects.all()

    return Response({
        'success': True,
        'data': [
            {
                'no': success_list.pk,
                'success_no': success_list.success_no.pk,
                'pace': success_list.pace,
            }
            for success_list in success_lists
        ]
    })