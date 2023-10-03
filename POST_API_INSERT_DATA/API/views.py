from django.shortcuts import render
from django.http import JsonResponse
from .dboperations import dbop_insert_data
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['POST'])
def API_Insert_Data(request):
    try:
        id_param = request.data.get('ID')
        dbop_insert_data(id_param)
        return Response({"success": True, "message":"Data inserted successfully."})
    except Exception as e:
        return Response({"success": False,"message": str(e)})



