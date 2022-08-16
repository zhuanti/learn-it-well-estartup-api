from json import JSONDecodeError

from django.db import IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Subject

# 每一個測試的api_view,一次只能取消註解一個

from utils.decorators import user_login_required


@api_view()
@user_login_required
def get_all_reviews(request):
    subjects = Subject.objects.all()

    return Response({
        'success': True,
        'data': [
            {
                'no': subject.pk,
                'name': subject.name,
            }
            for subject in subjects

        ]
    })
