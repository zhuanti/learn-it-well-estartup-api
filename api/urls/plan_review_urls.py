from django.urls import path

from api.views.plan_review_views import *


app_name = 'plan'

urlpatterns = [
    # path('all/', get_all_reviews),
    
    # 下面test/ 供成就相關表格進行測試
    path('get/', get_all_reviews_test),
    path('add/', addplan),
    path('edit/<int:pk>', showeditplan),
    path('editplan/<int:pk>', editplan),
    path('delete/', deleteplan),

    # 學姊的範例測試
    # path('get/<int:pk>/', get_review),
    # path('get_critic_reviews/', get_critic_reviews),
]