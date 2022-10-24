from django.urls import path

from api.views.other_review_views import *

urlpatterns = [

    path('studyroom/all/', get_all_reviews_studyroom),
    path('studyroom/get/<int:pk>', get_room_no),  # 加入房間編號
    path('studyroom/Sserch/', Sserch),
    path('studyroom/getinfo/', get_studyroom_info), # 自習室抓取資訊
    path('studyroom/self/', setthings),
    # 下面test/ 供其他細項相關表格進行測試
    path('impeach/test/', get_all_reviews_impeach_test),
    path('studyroom/test/', get_all_reviews_studyroom_test),
    path('news/', News)

    # 學姊的範例測試
    # path('get/<int:pk>/', get_review),
    # path('get_critic_reviews/', get_critic_reviews),
]
