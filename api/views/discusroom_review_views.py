from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Discussroom, Discussroom_record, Discussroom_question, Discussroom_ans

# 每一個測試的api_view,一次只能取消註解一個

# 討論室列表
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
            }
            for discussroom in discussrooms


        ]
            # json.dumps(discussrooms, cls=MyEncoder)
    })

# 討論室文字紀錄測試
# @api_view()
# def get_all_reviews_test(request):
#     discussroom_records = Discussroom_record.objects.all()
#
#     return Response({
#         'success': True,
#         'data': [
#             {
#                 'no': discussroom_record.pk,
#                 'comment': discussroom_record.comment
#             }
#             for discussroom_record in discussroom_records
#
#
#         ]
#             # json.dumps(discussrooms, cls=MyEncoder)
#     })

# 討論室提問測試
# @api_view()
# def get_all_reviews_test(request):
#     discussroom_questions = Discussroom_question.objects.all()
#
#     return Response({
#         'success': True,
#         'data': [
#             {
#                 'no': discussroom_question.pk,
#                 'title': discussroom_question.title
#             }
#             for discussroom_question in discussroom_questions
#
#
#         ]
#             # json.dumps(discussrooms, cls=MyEncoder)
#     })

# 討論室提問答案測試
# @api_view()
# def get_all_reviews_test(request):
#     discussroom_anss = Discussroom_ans.objects.all()
#
#     return Response({
#         'success': True,
#         'data': [
#             {
#                 'no': discussroom_ans.pk,
#                 'comment': discussroom_ans.comment
#             }
#             for discussroom_ans in discussroom_anss
#
#
#         ]
#             # json.dumps(discussrooms, cls=MyEncoder)
#     })


# 以下為學姊範例程式碼

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
