from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@api_view(['GET'])
def boasVindas(request):
    if request.method == 'GET':
        return Response("olá envie uma data e a taxa de referência que você deseja consultar")
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def buscaDados(request):
    data = request.GET.get('data')
    slcTaxa = request.GET.get('slcTaxa')

    if data and slcTaxa:
        try:
            data = datetime.strptime(data,'%Y-%m-%d').date()            
            data1 = str(data)
            data1 = data1.replace('-','')    
            data_formatada = data.strftime('%d/%m/%Y')
            print(data1,data_formatada)

        except:
            return Response({"error": "O formato da data está incorreto ",
                             "data":"use AAAA-MM-DD, somente números",
                             "exemplo":"2024-12-31"}, status=400)
        
        
        url = f'https://www2.bmf.com.br/pages/portal/bmfbovespa/lumis/lum-taxas-referenciais-bmf-enUS.asp?Data={data_formatada}&Data1={data1}&slcTaxa={slcTaxa}'
        
        chrome_options = Options()
        chrome_options.add_argument("--headless") 
        chrome_options.add_argument("--disable-gpu") 
        navegador = webdriver.Chrome(options=chrome_options)
        navegador.get(url)
        tabela = navegador.find_element(By.TAG_NAME,'tbody')
        print(tabela)

        return Response(tabela)
    else:
        return Response({"error": "Parâmetros 'data' e 'slcTaxa' são obrigatórios"}, status=400)

