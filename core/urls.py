"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

urlpatterns = [
        path('api/auth/', include('api.urls.auth_urls')),
        path('api/discusroom/', include('api.urls.discusroom_review_urls')),
        path('api/report/', include('api.urls.report_review_urls')),
        path('api/success/', include('api.urls.success_review_urls')),
        path('api/plan/', include('api.urls.plan_review_urls')),
        path('api/user/', include('api.urls.user_review_urls')),
        path('api/', include('api.urls.other_review_urls')),
]