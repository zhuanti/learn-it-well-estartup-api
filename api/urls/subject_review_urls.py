from django.urls import path

from api.views.subject_review_views import *


app_name = 'subject'

urlpatterns = [
    path('all/<int:pk>', get_all_reviews),  # 多人列表
    path('selfall/', get_selfall_reviews),  # 個人列表
    path('studyroom/many/', msetthings),  # 多人自習室寫入讀書資訊到report
    path('studyroom/exittime/', together_exittime)  # 多人自習室更新結束時間

]
