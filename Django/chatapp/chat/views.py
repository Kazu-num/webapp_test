from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm
import subprocess
from django.http import HttpResponseRedirect

def root_redirect(request):
    return HttpResponseRedirect('/chat/')

def run_python_process(content):
    result = subprocess.run(['python', '-c', content], capture_output=True, text=True)
    return result.stdout

def chat_view(request):
    messages = Message.objects.all()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save()
            output = run_python_process(message.content)
            Message.objects.create(user='System', content=output)
            return redirect('chat')
    else:
        form = MessageForm()
    return render(request, 'chat/chat.html', {'messages': messages, 'form': form})
