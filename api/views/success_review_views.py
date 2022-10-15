from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Success, Success_list, User

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
# @user_login_required
def get_all_reviews(request):
    data = request.data
    # user_id = data.get('user_id')
    # user = User.objects.filter(pk=user_id)
    success_lists = Success_list.objects.all()
    success = Success.objects.all()

    return Response({
        'success': True,
        'data': [
            {
                'no': success.pk,
                'name': success.name,
                'pace': success.pace,
                'success_list': [
                    {
                        'success_list_no': success_list.pk,
                        'user_id': success_list.user.pk,
                        'sucess_no': success_list.success_no,
                        'pace': success_list.pace,
                        'lockif': success_list.lockif,
                    }
                    for success_list in Success_list.objects.all()
                ],
                # 'no': success_list.pk,
                # 'user_id': success_list.user.pk,
                # 'success': [
                #     {
                #         'success_no': success.pk,
                #         'name': success.name,
                #         'pace': success.pace,
                #     }
                #     for success in Success.objects.filter(success_no=success_list.pk)
                # ],
                # 'pace': success_list.pace,
                # 'lockif': success_list.lockif
            }
            # for success_list in success_lists
        ]
    })
