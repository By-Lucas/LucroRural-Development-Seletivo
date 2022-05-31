from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver


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
        return self.user.username 

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

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()