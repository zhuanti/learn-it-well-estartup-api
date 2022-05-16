from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Discussroom


# import json
# import datetime
# import numpy as np
#
# class MyEncoder(json.JSONEncoder):
#
#     def default(self, obj):
#         # 检查到是bytes类型的数据就转为str类型
#         if isinstance(obj, bytes):
#             return str(obj, encoding='utf-8')
#
#         # 检查到是intc类型的数据就转为str类型
#         if isinstance(obj, np.intc):
#             return str(obj)
#
#         # 检查到是float32类型的数据就转为str类型
#         if isinstance(obj, np.float32):
#             return str(obj)
#
#         # 检查到是datetime.datetime类型的数据就转为str类型
#         if isinstance(obj, datetime.datetime):
#             return obj.strftime("%Y-%m-%d %H:%M:%S")
#         return json.JSONEncoder.default(self, obj)


@api_view()
def get_all_reviews(request):
    discussrooms = Discussroom.objects.all()
    # print(discussrooms)

    return Response({
        'success': True,
        'data': [
            {
                'no': discussroom.pk,
                'schoolsys_no': discussroom.schoolsys_no.pk,
                'subject_no': discussroom.subject_no.pk,
                'name': discussroom.name,
                'pwd': discussroom.pwd,
                'total_people': discussroom.total_people,

                # no = models.IntegerField(primary_key=True)
                # schoolsys_no = models.IntegerField
                # subject_no = models.IntegerField
                # name = models.CharField(max_length=100)
                # pwd = models.CharField(max_length=30)
                # total_people = models.IntegerField

            }
            for discussroom in discussrooms


        ]
            # json.dumps(discussrooms, cls=MyEncoder)

    })




# @api_view()
# def get_all_reviews(request):
#     books = Book.objects.all()
#     # print(books)
#     return Response({
#         'success': True,
#         'data':[
#             {
#                 'id': book.no,
#                 'user_id': book.user.pk,
#                 'name': book.name,
#                 'title': book.title,
#                 'comment': book.comment
#             }
#             for book in books
#         ]
#
#     })
#     # data=[]
#     # for item in items:
#     #     data.append({...})
#
# @api_view()
# def get_review(request, pk):
#     try:
#         books = Book.objects.get(pk=pk)
#     except:
#         return Response ({'success': False, 'message':'查無資料'}, status=status.HTTP_404_NOT_FOUND)
#     return Response({
#         'success': True,
#         'data':
#             {
#                 'id': books.no,
#                 'user_id':books.user.pk,
#                 'name':books.name,
#                 'title':books.title,
#                 'comment':books.comment
#             }
#     })

# @api_view()
# def get_critic_reviews(request):
