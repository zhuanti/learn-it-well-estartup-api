from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Discussroom, Discussroom_record, Discussroom_question, Discussroom_ans

# 每一個測試的api_view,一次只能取消註解一個

# 討論室列表
@api_view()
def get_all_reviews(request):
    discussrooms = Discussroom.objects.all()
    # print(discussrooms)

    return Response({
        'success': True,
        'data': [
            {
                'no': discussroom.pk,
                'schoolsys_no': discussroom.schoolsys_no.pk,
                'subject_no': discussroom.subject_no.pk,
                'name': discussroom.name,
                'pwd': discussroom.pwd,
                'total_people': discussroom.total_people,
            }
            for discussroom in discussrooms


        ]
            # json.dumps(discussrooms, cls=MyEncoder)
    })