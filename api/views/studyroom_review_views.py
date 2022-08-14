# # from django.db import IntegrityError
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
#
# # 每一個測試的api_view,一次只能取消註解一個
# from api.models import Studyroom
# from utils.decorators import user_login_required
#
#
# # 新增科目
# @api_view(['POST'])
# @user_login_required
# def addsub(request):
#     data = request.data
#     # 新增
#     try:
#         Studyroom.objects.create(subject_no_id=data['subject_no_id'], set_time=data['set_time'],
#                                  subject_detail=data['subject_detail'], )
#
#         return Response({'success': True, 'message': '新增成功'})
#
#     except IntegrityError:
#         return Response({'success': False, 'message': '新增失敗'}, status=status.HTTP_409_CONFLICT)
