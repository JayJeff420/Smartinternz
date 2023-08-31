from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import os
import openai

openai.api_key = "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"
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": ""
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
# Create your views here.
def chat(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def chatAPI(request):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        prompt="",
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    response={"this":"that"}
    return JsonResponse(response)