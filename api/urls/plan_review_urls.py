from django.urls import path

from api.views.plan_review_views import *

app_name = 'plan'

urlpatterns = [
    # path('all/', get_all_reviews),

    # 下面test/ 供成就相關表格進行測試
    path('get/', get_all_reviews_test),  # 顯示讀書規劃
    path('add/', addplan),  # 新增讀書規劃
    path('showedit/', showeditplan),  # 顯示特定讀書規劃
    path('editplan/', editplan),  # 編輯讀書規劃
    path('delete/', deleteplan),  # 刪除讀書規劃
    # path('delete/<int:id>', deleteplan),  # 刪除讀書規劃

    # path('addplantest/', addplantest),
    path('editplantest/', editplantest),  # 編輯讀書規劃
    path('deletetest/', deleteplantest),  # 刪除讀書規劃
    # path('showedittest/', showeditplantest),  # test顯示特定讀書規劃
    # path('gettest/', get_all_reviews_testtest),  # 顯示讀書規劃
    # 學姊的範例測試
    # path('get/<int:pk>/', get_review),
    # path('get_critic_reviews/', get_critic_reviews),
]
