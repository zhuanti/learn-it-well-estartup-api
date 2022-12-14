from datetime import datetime

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Success, Success_list, User, All_tot_time_view, Report, Subject, Dis_tot_time_view, \
    Study_tot_time_view, Weekdatetime_final_view

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
def get_all_reviews(request):
    data = request.query_params
    user_id = data.get('user_id')

    success_lists = Success_list.objects.filter(user_id=user_id).order_by('success_no_id')  # user's success

    success_nos = Success.objects.all()  # success name

    # subject_nos = Subject.objects.all()
    # week_days = Weekdatetime_final_view.objects.all()

    while not success_lists.exists(): # user don't have successs
        for success_no in success_nos:
            Success_list.objects.create(user_id=user_id, success_no=success_no, pace=0,
                                        lockif=0)

        success_lists = Success_list.objects.filter(user_id=user_id).order_by('success_no_id') # user's success

    # while not all_tot_time.exists():
    # for subject_no in subject_nos:
    Report.objects.create(user_id=user_id,
                          classroom_type_no_id="4",
                          subject_no_id="6",
                          entry_time=datetime.now(),
                          exit_time=datetime.now(),
                          )
    all_tot_time = All_tot_time_view.objects.filter(user_id=user_id)  # all read time

    # while not dis_tot_time.exists():
    # for subject_no in subject_nos:
    Report.objects.create(user_id=user_id,
                          classroom_type_no_id="3",
                          subject_no_id="6",
                          entry_time=datetime.now(),
                          exit_time=datetime.now(),
                          )
    dis_tot_time = Dis_tot_time_view.objects.filter(user_id=user_id)

    # while not study_tot_time.exists():
    # for subject_no in subject_nos:
    Report.objects.create(user_id=user_id,
                          classroom_type_no_id="1",
                          subject_no_id="6",
                          entry_time=datetime.now(),
                          exit_time=datetime.now(),
                          )
    study_tot_time = Study_tot_time_view.objects.filter(user_id=user_id)


    data = []

    for success_list in success_lists:
        flag = Success.objects.filter(pk=success_list.success_no.pk).first().classroom_no.pk
        d = {
            'no': success_list.pk,
            'user_id': success_list.user.pk,
            'success_no': success_list.success_no.pk,
            'pace': success_list.pace,
            'lockif': success_list.lockif,
            'suc_no': Success.objects.filter(pk=success_list.success_no.pk).first().no,  # 成就流水號
            'suc_name': Success.objects.filter(pk=success_list.success_no.pk).first().name,
            'suc_pace': Success.objects.filter(pk=success_list.success_no.pk).first().pace,  # 進度
            'suc_classroom': Success.objects.filter(pk=success_list.success_no.pk).first().classroom_no.pk,
        }

        if flag == 1:

            d['res_time'] = int(study_tot_time.first().study_total_min)
        elif flag == 3:
            d['res_time'] = int(dis_tot_time.first().dis_total_min)
        else:
            d['res_time'] = int(all_tot_time.first().total_min)
        data.append(d)



    return Response({
        'success': True,
        'data': data
    })


    # 舊得抓取方法
    #
    # return Response({
    #     'success': True,
    #     'data': {
    #         'all_tot_time': [
    #             {
    #                 'total_min': all_tot_time.total_min
    #             }
    #             for all_tot_time in all_tot_time
    #         ],
    #         'dis_tot_time': [
    #             {
    #                 'dis_total_min': dis_tot_time.dis_total_min
    #             }
    #             for dis_tot_time in dis_tot_time
    #         ],
    #         'study_tot_time': [
    #             {
    #                 'study_total_min': study_tot_time.study_total_min
    #             }
    #             for study_tot_time in study_tot_time
    #         ],
    #         'sus_all': [
    #             {
    #                 'no': success_list.pk,
    #                 'user_id': success_list.user.pk,
    #                 'success_no': success_list.success_no.pk,
    #                 'pace': success_list.pace,
    #                 'lockif': success_list.lockif,
    #                 'success_names': [
    #                     {
    #                         'suc_no': success.no,
    #                         'suc_name': success.name,
    #                         'suc_pace': success.pace,
    #                         'suc_classroom': success.classroom_no.pk,
    #                     }
    #                     for success in Success.objects.filter(pk=success_list.success_no.pk)
    #                 ],
    #             }
    #             for success_list in success_lists
    #         ]
    #     }
    # })

# 編輯成就
@api_view(['POST'])
@user_login_required
def success_fin(request):

    data = request.data

    no = data['no']
    user_id = data['user_id']

    user = User.objects.filter(pk=user_id)
    success_list = Success_list.objects.filter(pk=no)


    if not success_list.exists():
        return Response({'success': False, 'message': '沒有此成就'}, status=status.HTTP_404_NOT_FOUND)

    try:
        success_list.update(lockif="1")
        user.update(point=int(user.first().point)+100)
        return Response({'success': True, 'message': '編輯成功'})

    except:
        return Response({'success': False, 'message': '編輯失敗'}, status=status.HTTP_400_BAD_REQUEST)
