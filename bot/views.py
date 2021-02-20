from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Button,NumberId
import json



class GetList(APIView):
    def get(self,request):
        # df = pd.read_excel("mm.xlsx")
        # a = df['A']
        # b = df['B']
        # for i,j in zip(b,a):
        #     Button.objects.create(button=j).save()
        #     NumberId.objects.create(button=Button.objects.get(button=j),text=).save()

        data = {'list':[]}
        button = Button.objects.all()
        for i in button:
            data['list'].append({'name':i.button})
        return Response(data)

class NumberBut(APIView):
    def post(self,request):
        data = json.loads(request.body)
        try:
            get_butt = Button.objects.get(button=data['text'])
            text = NumberId.objects.get(button=get_butt)
            return Response({"text":text.text,"code":200})
        except:
            return Response({"code":401})