from django.urls import path

from api.views.success_review_views import *


app_name = 'success'

urlpatterns = [
    path('list/', get_all_reviews),
    path('list/update/', success_fin),
    
    # 下面test/ 供成就相關表格進行測試
    # path('test/', get_all_reviews_test),


    # 學姊的範例測試
    # path('get/<int:pk>/', get_review),
    # path('get_critic_reviews/', get_critic_reviews),
]