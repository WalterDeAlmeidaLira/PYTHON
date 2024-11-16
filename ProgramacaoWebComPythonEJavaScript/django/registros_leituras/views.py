from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import TopicForm 
from .models import Topic, Entry
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request,'registros_leituras/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics }
    return render(request,'registros_leituras/topics.html',context) 

def topic(request,topic_id):
    try:
        topic = Topic.objects.get(id=topic_id)
    except Topic.DoesNotExist:
        return HttpResponse("<h1>Erro: Tópico não encontrado.</h1>")
    except Exception as e:
        return HttpResponse(f"<h1>Erro ao carregar: {e}</h1>")

    entries = topic.entry_set.order_by('-date_added')
    context = {
        'topic':topic,
        'entries':entries
        }
    return  render(request,"registros_leituras/topic.html",context)

def new_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect(reverse('topics'))
    else:
        form = TopicForm()

    context = {'form': form}
    return render(request, 'registros_leituras/new_topic.html', context)

