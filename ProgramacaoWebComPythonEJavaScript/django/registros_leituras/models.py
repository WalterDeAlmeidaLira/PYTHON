from django.db import models

# Create your models here.
class Topic(models.Model):
    # um assunto sobre o qual o usuario está aprendendo
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # organiza o painel do admin retornando uma string do modelo
        return self.text
    
class Entry (models.Model):
    # anotações sobre um assunto
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    #classe que envia metadados como nome que o djnago deve usar na tabela
    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        #devolve uma string do modelo
        return self.text[:50] + '...' # retorna o 50 primeiros caracteres

