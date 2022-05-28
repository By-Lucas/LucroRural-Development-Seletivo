from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

# AQUI É TODA A ESTRUTUDA DO ORM DO DJANGO
# É CRIADA A TABELA DO BANCO DE DADOS E CADA VARIAVEL DESSAS É UMA TLINHA DE INFORMAÇÃO DO BANCO DE DADOS DO DJANGO
# O DJANGO TEM SEU PROPRIO ORM, E JOGA TODAS ESAS INFORMAÇÕES NO BANCO DE DADOS QUE VEM PADRAO COM ELE QUE É SQLITE

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    idade = models.IntegerField(null=True, blank=True, default=0)
    cidade = models.CharField(max_length=20, null=True, blank=True)
    contato = models.CharField(max_length=11, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    endereco = models.CharField(max_length=60, null=True, blank=True)
    imagem_perfil = models.ImageField(default='usuario.png', upload_to='users/', null=True, blank=True)
    data_cadastro = models.DateField(null=True, blank=True, auto_created=True, auto_now=True)

    def __str__(self) :
        return self.user.username # RETORNA NO ADMIN DO DJANGO

# O CODIGO ABAIXO VERIFICA O USUARIO E CRIA UM GRUPO PARA ELE SER ADCIONADO
# O ADMIN FICA NO GRUPO admin E QUEM NO FOR É CRIADO UM GRUPO client E O USUARIO VAI SER DIRECIONADO PARA ELE
# O USUARIO PODE TER OUTRAS PERMISSOES, É SÓ IR NO ADMIN DO DJANGO E ALTERAR
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if instance.is_staff:
        try:
            group = Group.objects.get(name='admin')
        except:
            group = Group.objects.create(name='admin')
    else:
        try:
            group = Group.objects.get(name='client')
        except:
            group = Group.objects.create(name='client')

    instance.groups.add(group)
    if created:
        Profile.objects.create(user=instance)

#AQUI SALVA TODAS AS INFORMACOES DO PERFIL INFORMADO ACIMA
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()