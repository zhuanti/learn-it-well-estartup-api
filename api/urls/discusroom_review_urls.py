from django.urls import path

from api.views.discusroom_review_views import *


app_name = 'discusroom'

urlpatterns = [
    path('all/', get_all_reviews),
    path('rec/', rec_reviews),
    path('addroom/',addroom),
    path('addroom_subject/',get_subject_reviews),

    # 下面test/ 供討論室相關表格進行測試
    path('test/', get_all_reviews_test),

    # 學姊的範例測試
    # path('get/<int:pk>/', get_review),
    # path('get_critic_reviews/', get_critic_reviews),
]
