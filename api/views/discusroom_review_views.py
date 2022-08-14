from django.db import IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Discussroom, Discussroom_record, Discussroom_question, Discussroom_ans, User, Subject

# 每一個測試的api_view,一次只能取消註解一個

from utils.decorators import user_login_required


# 討論室列表
@api_view()
@user_login_required
def get_all_reviews(request):
    discussrooms = Discussroom.objects.all()
    # print(discussrooms)

    return Response({
        'success': True,
        'data': [
            {
                'no': discussroom.pk,
                # 'schoolsys_no': discussroom.schoolsys_no.pk,
                'subject_no': discussroom.subject_no.pk,
                'name': discussroom.name,
                'pwd': discussroom.pwd,
                'total_people': discussroom.total_people,
            }
            for discussroom in discussrooms

        ]
        # json.dumps(discussrooms, cls=MyEncoder)
    })


# 討論室聊天內容
@api_view()
@user_login_required
def rec_reviews(request):
    # 注意：因使用POST，data
    data = request.query_params
    user_id = data.get('user_id')

    user_id = str(user_id).strip()

    # get 後面加東西，可能部會成功，故fileter 方便
    discussroom_recs = Discussroom_record.objects.filter(user_id=user_id)

    return Response({
        'success': True,
        'data': [
            {
                'no': discussroom_rec.pk,
                'discussroom_no': discussroom_rec.discussroom_no.pk,
                'user_id': discussroom_rec.user.pk,
                'comment': discussroom_rec.comment,
                'datetime': discussroom_rec.datetime
            }
            for discussroom_rec in discussroom_recs
        ]
    })


# 討論室文字紀錄測試
@api_view()
@user_login_required
def get_all_reviews_test(request):
    discussroom_records = Discussroom_record.objects.all()

    return Response({
        'success': True,
        'data': [
            {
                'no': discussroom_record.pk,
                'comment': discussroom_record.comment
            }
            for discussroom_record in discussroom_records

        ]
    })


# 討論室提問測試
@api_view()
def get_qus(request):
    discussroom_questions = Discussroom_question.objects.all()

    return Response({
        'success': True,
        'data': [
            {
                'no': discussroom_question.pk,
                'title': discussroom_question.title,
                'quser_id': discussroom_question.quser.pk,

            }
            for discussroom_question in discussroom_questions


        ]
            # json.dumps(discussrooms, cls=MyEncoder)
    })

# 討論室提問答案測試
@api_view(['POST'])
# @user_login_required
def get_ans(request):
    discussroom_anss = Discussroom_ans.objects.all()
    data = request.data

    return Response({
        'success': True,
        'data': [
            {
                'no': discussroom_ans.pk,
                'comment': discussroom_ans.comment
            }
            for discussroom_ans in discussroom_anss


        ]
            # json.dumps(discussrooms, cls=MyEncoder)
    })

# 新增房間
@api_view(['POST'])
# @user_login_required
def addroom(request):
    data = request.data
    # Subjects = Subject.objects.all()
    #新增
    try:
        Discussroom.objects.create(no=data['no'], subject_no_id=data['subject_no_id'],
                            name=data['name'], total_people=data['total_people'],)

        return Response({'success': True, 'message': '新增成功'})

    except IntegrityError:
        return Response({'success': False, 'message': '此房間已被創建'}, status=status.HTTP_409_CONFLICT)


# 討論室抓使用者
@api_view()
@user_login_required
def getuser(request):
    users = User.objects.all()

    return Response({
        'success': True,
        'data': [
            {
                'no': users.pk,
                'name': users.name,
            }
            for users in users

        ]
    })


# 討論室房間新增-科目
# @api_view()
# # @user_login_required
# def get_subject_reviews(request):
#     subjects = Subject.objects.all()
#
#     return Response({
#         'success': True,
#         'data': [
#             {
#                 'no': subject.pk,
#                 'name': subject.name,
#             }
#             for subject in subjects
#
#         ]
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
