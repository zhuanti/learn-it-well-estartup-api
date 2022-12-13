from django.urls import path

from api.views.user_review_views import *

# 將被auth_urls取代
app_name = 'user'

urlpatterns = [
    # path('all/', get_all_reviews),

    # 下面test/ 供成就相關表格進行測試
    path('test/', get_user_detail_test),  # 測試
    path('detail/', get_user_detail),  # 顯示使用者個人資訊
    path('detail/edit/', user_detail_edit),  # 編輯使用者個人資訊
    path('pwd/edit/', user_pwd_edit),  # 編輯使用者密碼

    # 學姊的範例測試
    # path('get/<int:pk>/', get_review),
    # path('get_critic_reviews/', get_critic_reviews),
]
