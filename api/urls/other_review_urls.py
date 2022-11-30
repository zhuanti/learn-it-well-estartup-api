from django.urls import path

from api.views.other_review_views import *

urlpatterns = [

    path('studyroom/all/', get_all_reviews_studyroom),
    path('studyroom/get/<int:pk>', get_room_no),  # 加入房間編號
    path('studyroom/update/entrytime/', sroom_entrytime),  # 多人自習室更新開始時間
    path('studyroom/update/exittime/', sroom_exittime),  # 多人自習室更新結束時間
    path('studyroom/Sserch/', Sserch),
    path('studyroom/getinfo/', get_studyroom_info),  # 個人自習室抓取資訊
    path('studyroom/self/', setthings),  # 個人自習室寫入讀書資訊到report
    # path('studyroom/self/update/entrytime/', self_entrytime),  # 個人自習室更新開始時間
    path('studyroom/self/update/exittime/', self_exittime),  # 個人自習室更新結束時間

    # 移到subject寫
    # path('studyroom/getminfo/', get_mstudyroom_info),  # 多人自習室抓取資訊
    # path('studyroom/many/', msetthings),  # 多人自習室寫入讀書資訊到report

    # 下面test/ 供其他細項相關表格進行測試
    path('impeach/test/', get_all_reviews_impeach_test),
    path('studyroom/test/', get_all_reviews_studyroom_test),
    path('news/', News)

    # 學姊的範例測試
    # path('get/<int:pk>/', get_review),
    # path('get_critic_reviews/', get_critic_reviews),
]
