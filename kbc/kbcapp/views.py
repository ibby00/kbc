from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import KbcApp
from .serializers import KbcAppSerializer

@csrf_exempt
def kbcapp_list(request):
    if request.method == 'GET':
        kbc_app = KbcApp.objects.all()
        serializer = KbcAppSerializer(kbc_app, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = request.data.get('id')
        print(data)
        return JsonResponse(data, safe=False)

class KbcAppApi(APIView):
    def get(self, request):
        language = request.query_params.get('language')
        title = request.query_params.get('title')
        style = request.query_params.get('style')
        kbc_app = KbcApp.objects.all()
        if language:
            kbc_app = kbc_app.filter(language=language)
        if title:
            kbc_app = kbc_app.filter(title=title)
        if style:
            kbc_app = kbc_app.filter(style=style)
        serializer = KbcAppSerializer(kbc_app, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        language = data.get('language')

        if not data.get('title'):
            print(data.get('title'))
            return Response({"error": "Title is Blanked"}, status=400)
        elif data.get('title'):
            data["title"] = data.get('title') + " AI World"

        if language == 'python':
            data["language"] = language + " Programming "

        if language == 'html':
            data["language"]= language + " Markup language"

        serializer = KbcAppSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        print(data.get('language'))
        return Response(serializer.data, status=201)