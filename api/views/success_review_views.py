from datetime import datetime

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Success, Success_list, User, All_tot_time_view, Report, Subject, Dis_tot_time_view, Study_tot_time_view

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

    success_lists = Success_list.objects.filter(user_id=user_id) # user's success
    all_tot_time = All_tot_time_view.objects.filter(user_id=user_id)  # all read time
    dis_tot_time = Dis_tot_time_view.objects.filter(user_id=user_id)
    study_tot_time = Study_tot_time_view.objects.filter(user_id=user_id)

    success_nos = Success.objects.all() # success name
    subject_nos = Subject.objects.all()



    while not success_lists.exists(): # user don't have successs
        for success_no in success_nos:
            Success_list.objects.create(user_id=user_id, success_no=success_no, pace=0,
                                        lockif=0)

        success_lists = Success_list.objects.filter(user_id=user_id) # user's success

    while not all_tot_time.exists():
        for subject_no in subject_nos:
            Report.objects.create(user_id=user_id,
                                  classroom_type_no_id="4",
                                  subject_no_id=subject_no.pk,
                                  entry_time=datetime.now(),
                                  exit_time=datetime.now(),
                                  )
        all_tot_time = All_tot_time_view.objects.filter(user_id=user_id)  # all read time

    while not dis_tot_time.exists():
        for subject_no in subject_nos:
            Report.objects.create(user_id=user_id,
                                  classroom_type_no_id="3",
                                  subject_no_id=subject_no.pk,
                                  entry_time=datetime.now(),
                                  exit_time=datetime.now(),
                                  )
        dis_tot_time = Dis_tot_time_view.objects.filter(user_id=user_id)

    while not study_tot_time.exists():
        for subject_no in subject_nos:
            Report.objects.create(user_id=user_id,
                                  classroom_type_no_id="1",
                                  subject_no_id=subject_no.pk,
                                  entry_time=datetime.now(),
                                  exit_time=datetime.now(),
                                  )
        study_tot_time = Study_tot_time_view.objects.filter(user_id=user_id)


    return Response({
        'success': True,
        'data': {
            'all_tot_time': [
                {
                    'total_min': all_tot_time.total_min
                }
                for all_tot_time in all_tot_time
            ],
            'dis_tot_time': [
                {
                    'dis_total_min': dis_tot_time.dis_total_min
                }
                for dis_tot_time in dis_tot_time
            ],
            'study_tot_time': [
                {
                    'study_total_min': study_tot_time.study_total_min
                }
                for study_tot_time in study_tot_time
            ],
            'sus_all': [
                {
                    'no': success_list.pk,
                    'user_id': success_list.user.pk,
                    'success_no': success_list.success_no.pk,
                    'pace': success_list.pace,
                    'lockif': success_list.lockif,
                    'success_names': [
                        {
                            'suc_no': success.no,
                            'suc_name': success.name,
                            'suc_pace': success.pace,
                            'suc_classroom': success.classroom_no.pk,
                        }
                        for success in Success.objects.filter(pk=success_list.success_no.pk)
                    ],
                }
                for success_list in success_lists
            ]
        }
    })