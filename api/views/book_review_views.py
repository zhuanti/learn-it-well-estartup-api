from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Book


@api_view()
def get_all_reviews(request):
    books = Book.objects.all()
    # print(books)
    return Response({
        'success': True,
        'data':[
            {
                'id': book.no,
                'user_id': book.user.pk,
                'name': book.name,
                'title': book.title,
                'comment': book.comment
            }
            for book in books
        ]

    })
    # data=[]
    # for item in items:
    #     data.append({...})

@api_view()
def get_review(request, pk):
    try:
        books = Book.objects.get(pk=pk)
    except:
        return Response ({'success': False, 'message':'查無資料'}, status=status.HTTP_404_NOT_FOUND)
    return Response({
        'success': True,
        'data':
            {
                'id': books.no,
                'user_id':books.user.pk,
                'name':books.name,
                'title':books.title,
                'comment':books.comment
            }
    })

# @api_view()
# def get_critic_reviews(request):
