from django.urls import path

from api.views.discusroom_review_views import *

app_name = 'discusroom'

urlpatterns = [
    path('all/', get_all_reviews),  # 列表
    path('rec/', rec_reviews),  # 聊天內容
    path('addroom/', addroom),  # 新增房間
    path('qus/<int:pk>', add_qus),  # 問題
    path('ans/<int:pk>', add_ans),  # 回答
    path('ans_list/', get_ans_list),  # 問題、回答列表
    path('get_critic_reviews/', get_critic_reviews),  # 搜尋
    path('get/<int:pk>', get_room_no),  # 加入房間編號

    # 下面test/ 供討論室相關表格進行測試
    path('test/', get_all_reviews_test),
    path('getuser/<pk>', getuser),
    # path('addroom_subject/',get_subject_reviews), # 新增房間時顯示科目名稱

    path('test/', get_all_reviews_test),  # 文字記錄

    # 學姊的範例測試
    # path('get/<int:pk>/', get_review),
    # path('get_critic_reviews/', get_critic_reviews),
]
