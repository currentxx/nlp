from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ApiProje.models import Kurlar,Ozet,OzetveTamMetin
from ApiProje.serializers import KurSerializer, OzetSerializer,OzetTamSerializer
from ApiProje import Ozetleme

from rest_framework.decorators import api_view
from django.http import *

@api_view(['GET','POST'])
def index(request):
    if request.method=='GET':
        #return HttpResponse("Hello, world. You're at index.")
        kurlarimiz = Kurlar.objects.all()
        # Serializer tarafından tarat
        serializer = KurSerializer(kurlarimiz, many=True)
        # Json olarak dönder.
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = KurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def KurDetaylari(request,pk):
    try:
        # Eğer gelen id veri tabanında var ise, değişkene depola
        veri = Kurlar.objects.get(pk=pk)
    except Kurlar.DoesNotExist:
        # Bu ide sahip veri yok ise 404 http kodunu göster
        return Response(status=status.HTTP_404_NOT_FOUND)
        # Get isteği gelirse
    if request.method == 'GET':
        # Aranan id'deki veriyi depola
        serializer = KurSerializer(veri)
        # json olarak yolla
        return Response(serializer.data)
        # PUT İsteği gelirse
    elif request.method == 'PUT':
        # Gelen detayı serializer tarafından tarattır
        serializer = KurSerializer(veri, data=request.data)
        # Gelen data doğru ise
        if serializer.is_valid():
            # Snippet'i kaydet
            serializer.save()
            # Oluşan çıktıyı geri dönder
            return Response(serializer.data)
        # Eğer gelen data doğru değilde, 400 http kodunu yansıt
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Eğer Delete isteği gelirse
    elif request.method == 'DELETE':
        # İstekte bulunan id sahip veriyi sil.
        veri.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OzetGetir(APIView):
    def get(self,request):
        cumle="Those Who Are Resilient Stay In The Game Longer. On the mountains of truth you can never climb in vain: either you will reach a point higher up today, or you will be training your powers so that you will be able to climb higher tomorrow.” — Friedrich Nietzsche Challenges and setbacks are not meant to defeat you, but promote you. However, I realise after many years of defeats, it can crush your spirit and it is easier to give up than risk further setbacks and disappointments. Have you experienced this before? To be honest, I don’t have the answers. I can’t tell you what the right course of action is; only you will know. However, it’s important not to be discouraged by failure when pursuing a goal or a dream, since failure itself means different things to different people. To a person with a Fixed Mindset failure is a blow to their self-esteem, yet to a person with a Growth Mindset, it’s an opportunity to improve and find new ways to overcome their obstacles. Same failure, yet different responses. Who is right and who is wrong? Neither. Each person has a different mindset that decides their outcome. Those who are resilient stay in the game longer and draw on their inner means to succeed."
        ozet =Ozetleme.create_frequency_table(cumle)
        sentences =Ozetleme.sent_tokenize(cumle)
        sentence_scores = Ozetleme._score_sentences(sentences, ozet)
        threshold = Ozetleme._find_average_score(sentence_scores)
        summary = Ozetleme._generate_summary(sentences, sentence_scores, 1.5 * threshold)
        lst=[]
        lst.append(OzetveTamMetin(1,cumle,summary))
        serializer = OzetTamSerializer(lst, many=True)
        return Response(serializer.data)

class OzetCreate(APIView):
    def get(self, request):
        cumle = "Those Who Are Resilient Stay In The Game Longer. On the mountains of truth you can never climb in vain: either you will reach a point higher up today, or you will be training your powers so that you will be able to climb higher tomorrow.” — Friedrich Nietzsche Challenges and setbacks are not meant to defeat you, but promote you. However, I realise after many years of defeats, it can crush your spirit and it is easier to give up than risk further setbacks and disappointments. Have you experienced this before? To be honest, I don’t have the answers. I can’t tell you what the right course of action is; only you will know. However, it’s important not to be discouraged by failure when pursuing a goal or a dream, since failure itself means different things to different people. To a person with a Fixed Mindset failure is a blow to their self-esteem, yet to a person with a Growth Mindset, it’s an opportunity to improve and find new ways to overcome their obstacles. Same failure, yet different responses. Who is right and who is wrong? Neither. Each person has a different mindset that decides their outcome. Those who are resilient stay in the game longer and draw on their inner means to succeed."
        ozetmetin=Ozetleme.GetByOzet(cumle)

        lst={'id':1,'TamMetin': cumle,'OzetMetin': ozetmetin}
        serializer = OzetTamSerializer(data=lst)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class KurListesiGetirIdyeGore(APIView):
    def get(self,request,idler):
        kurlar = Kurlar.objects.all().filter(id=idler)
        serializer = KurSerializer(kurlar, many=True)
        return Response(serializer.data)

class KurListesiGetirDovizeGore(APIView):
     def get(self,request,isim):
         kurlar = Kurlar.objects.all().filter(doviz_ismi=isim)
         serializer = KurSerializer(kurlar, many=True)
         return Response(serializer.data)

class KurListesiCreate(APIView):
     def get(self,request):
         data = {'id': 6,'doviz_ismi': "Pound1", 'alis': 12341, 'satis': 456671,'fark':112,'kur_kodu':"P4"}
         serializer = KurSerializer(data=data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
         else:
             return Response(serializer.errors)
