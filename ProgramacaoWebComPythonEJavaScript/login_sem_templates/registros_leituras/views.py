from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import TopicForm, EntryForm
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

def new_entry(request,topic_id):
    topic = Topic.objects.get(id = topic_id) # busca no banco pelo id da url

    if request.method != 'POST':
        # nenhum dado submetido
        form = EntryForm()
    else:
        #dados submetidos
        form = EntryForm(data = request.POST) # cria uma variavel data pois ainda nao está completo a requisicão
        if form.is_valid():
            new_entry = form.save(commit=False) # cria uma versao dos dados que serao salvos, mas ão salva os dados
            # print('dados do formulário',new_entry)
            new_entry.topic = topic # vincula o topico aos dados 
            new_entry.save()
            return HttpResponseRedirect(reverse('topic',args=[topic_id]))
        else:
            return HttpResponse('<h1>Erro ao cadastrar valores!</h1>')
        
    context = {'topic':topic,
               'form':form
               }
    
    return render(request,'registros_leituras/new_entry.html',context)

def edit_entry(request,entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic


    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic',args=[topic.id]))
        else:
            return HttpResponse('<h1>erro ao atualizar dados</h1>')

    context = {
        'topic': topic,
        'form': form,
        'entry':entry
    }

    return render(request,'registros_leituras/edit_entry.html',context)

