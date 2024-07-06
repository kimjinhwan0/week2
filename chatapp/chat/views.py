# chat/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Message
from .database import *

# 각 클래스마다, get, post, delete, put등의 rest api 형태에 관한 함수를 만들 수 있음.
# { 'id' : 1, 'pwd' : 3456 }, id, pwd: key 1, 3456이 value
class GetMessageView(APIView):
    def get(self, request, format=None): # request
        id = request.query_params.get('id') # .query_params를 하면 parameter를 얻어오는 거, .get('key') 하면 그 key에 해당하는 value를 가져와줌
        pwd = request.query_params.get('pwd')
        print("id", id, "pwd", pwd)
        message_id = insert_person(id, pwd)
        print("message_id", message_id)
        # request에 대한 response를 항상 client에게 보내줘야 함.
        # Response 객체를 import하고, Response({json 파일}, status=status.HTTP_200_OK)
        if id is not None:
            return Response({'message': 'OW now michigetnae'}, status=status.HTTP_200_OK)
        return Response({'error': 'id parameter is required'}, status=status.HTTP_400_BAD_REQUEST)