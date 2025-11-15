from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .chatbot import get_answer

@api_view(['POST'])
def chat(request):
    user_input = request.data.get("message", "")
    if not user_input:
        return Response({"error": "No message provided"}, status=400)
    answer = get_answer(user_input)
    return Response({"reply": answer})

def chat_page(request):
    return render(request, "chatbot_api/chat.html")