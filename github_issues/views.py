from os import get_inheritable
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import json
# Create your views here.


class All_Issues(APIView):

  def get(self,request,repo, repo_name):
    
    reques = requests.get(f'https://api.github.com/repos/{repo}/{repo_name}/issues?state=open')
  
    if reques.status_code == 200:
      array = []

      #filter the response data for number and  title
      res = json.loads(reques.content)
      for i in range(len(res)):
        data = {
          'number':res[i]['number'],
          'title': res[i]['title']

        }
        array.append(data)

      #bubble sort algorithm
      def bubble_sort(arr):
    
        for i in range( len(arr) - 1 ) :
          flag = 0

          for j in range(len(arr) - 1) :
            
            if arr[j]['title'] > arr[j + 1]['title'] : 
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
                flag = 1

          if flag == 0:
            break

        return arr
    
      data = bubble_sort(array)

    
    # data is json already no need to serialize
      return Response({'result': data}, status = 200)
    
    else :
      return Response({'message':'something went wrong'}, status = reques.status_code)
