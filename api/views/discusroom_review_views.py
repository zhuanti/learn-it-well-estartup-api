from json import JSONDecodeError

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


# 新增房間
@api_view(['POST'])
@user_login_required
def addroom(request):
    data = request.data
    # Subjects = Subject.objects.all()
    # 新增
    try:
        Discussroom.objects.create(subject_no_id=data['subject_no_id'],
                                   name=data['name'], total_people=data['total_people'], )

        return Response({'success': True, 'message': '新增成功'})


    except IntegrityError:
        return Response({'success': False, 'message': '此房間已被創建'}, status=status.HTTP_409_CONFLICT)


# 顯示加入房間編號、問題列表
@api_view()
@user_login_required
def get_room_no(request, pk):
    data = request.query_params
    user_id = data.get('user_id')

    user = str(user_id).strip()

    try:
        discussroom = Discussroom.objects.get(pk=pk)
        # discussroom.discussroom_question = Discussroom_question.object.get(pk=pk)
    except:
        return Response({'success': False, 'message': '查無此房間'}, status=status.HTTP_404_NOT_FOUND)
    return Response({
        'success': True,
        'data':
            {
                'user': [
                    {
                        'user_name': user_name.name,
                    }
                    for user_name in User.objects.filter(pk=user)
                ],
                'no': discussroom.pk,
                # 'schoolsys_no': discussroom.schoolsys_no.pk,
                'subject_no': discussroom.subject_no.pk,
                'name': discussroom.name,
                'pwd': discussroom.pwd,
                'total_people': discussroom.total_people,
                'discussroom_qus_lists': [
                    {
                        'dis_ques_no': discussroom_question.pk,
                        'title': discussroom_question.title,
                        'quser_id': discussroom_question.quser.pk,
                        'discussroom_ans_lists': [
                            {

                                'dis_ans_no': discussroom_ans.pk,
                                'dis_ans_ques_no': discussroom_ans.question_no.pk,
                                'auser_id': discussroom_ans.auser.pk,
                                'comment': discussroom_ans.comment,
                            }
                            for discussroom_ans in Discussroom_ans.objects.filter(question_no=discussroom_question.pk)
                        ],
                    }
                    for discussroom_question in Discussroom_question.objects.filter(discussroom_no=discussroom.pk)
                ],

            }
    })

# 顯示問題編號
@api_view()
@user_login_required
def get_qus_no(request, pk):
    try:
        discussroom_qus = Discussroom_question.objects.get(pk=pk)
    except:
        return Response({'success': False, 'message': '查無此問題'}, status=status.HTTP_404_NOT_FOUND)
    return Response({
        'success': True,
        'data':
            {
                'no': discussroom_qus.pk,
                'dis_no': discussroom_qus.discussroom_no.pk,
                'title': discussroom_qus.title,
            }
    })


# 討論室提問
@api_view(['POST'])
@user_login_required
def add_qus(request, pk):
    data = request.data
    # try:
    #     discussroom = Discussroom_question.objects.get(discussroom_no_id=pk)
    # except:
    #     return Response({'success': False, 'message': '查無此房間'}, status=status.HTTP_404_NOT_FOUND)
    # discussroom_questions = Discussroom_question.objects.all()
    # 注意：因使用POST，data
    try:
        Discussroom_question.objects.create(discussroom_no_id=pk,
                                            title=data['title'], quser_id=data['quser_id'], datetime=data['datetime'])

        return Response({'success': True, 'message': '新增成功'})


    except IntegrityError:
        return Response({'success': False, 'message': '新增失敗'}, status=status.HTTP_409_CONFLICT)


# # 新增房間
# @api_view(['POST'])
# # @user_login_required
# def addroom(request):
#     data = request.data
#     # Subjects = Subject.objects.all()
#     # 新增
#     try:
#         Discussroom.objects.create(subject_no_id=data['subject_no_id'],
#                                    name=data['name'], total_people=data['total_people'], )
#
#         return Response({'success': True, 'message': '新增成功'})
#
#
#     except IntegrityError:
#         return Response({'success': False, 'message': '此房間已被創建'}, status=status.HTTP_409_CONFLICT)


# 討論室問題、回答列表
@api_view()
def get_ans_list(request, pk):
    try:
        discussroom = Discussroom.objects.get(pk=pk)
    except:
        return Response({'success': False, 'message': '查無此房間'}, status=status.HTTP_404_NOT_FOUND)
    return Response({
        'success': True,
        'data':
            {
                'discussroom_qus_lists': [
                    {
                        'discussroom_no': discussroom_question.pk,
                        'title': discussroom_question.title,
                        'quser_id': discussroom_question.quser.pk,
                        'discussroom_ans_lists': [
                            {

                                'question_no': discussroom_ans.pk,
                                'auser_id': discussroom_ans.auser.pk,
                                'comment': discussroom_ans.comment,
                            }
                            for discussroom_ans in Discussroom_ans.objects.filter(question_no=discussroom_question.pk)
                        ],
                    }
                    for discussroom_question in Discussroom_question.objects.filter(discussroom_no=discussroom.pk)
                ],
            }
    })


# 討論室回答
@api_view(['POST'])
@user_login_required
def add_ans(request, pk):
    # discussroom_questions = Discussroom_question.objects.all()
    # 注意：因使用POST，data
    data = request.data
    try:
        Discussroom_ans.objects.create(question_no_id=pk,
                                       auser_id=data['auser_id'], comment=data['comment'], datetime=data['datetime'])

        return Response({'success': True, 'message': '新增成功'})


    except IntegrityError:
        return Response({'success': False, 'message': '新增失敗'}, status=status.HTTP_409_CONFLICT)


# 討論室抓使用者
@api_view()
@user_login_required
def getuser(request, pk):
    # users = User.objects.all()
    try:
        user = User.objects.get(pk=pk)
        return Response({
            'success': True,
            'data': [
                {
                    'id': user.pk,
                    'name': user.name,
                }

            ]
        })
    except JSONDecodeError:
        return Response({'success': False, 'message': '查無此人'}, status=status.HTTP_404_NOT_FOUND)


# 查詢
@api_view()
@user_login_required
def get_critic_reviews(request):
    # 注意：因使用GET，使用query_params
    data = request.query_params
    name = data.get('name')

    # 去除前後空白
    name = str(name).strip()
    discussrooms = Discussroom.objects.filter(name=name)

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
