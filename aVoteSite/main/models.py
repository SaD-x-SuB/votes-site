from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Votes(models.Model):

    title = models.CharField('Название', max_length=250)
    text = models.TextField('Текст')
    ansvers = models.CharField('Варианты ответов', max_length=500)
    date = models.DateField('Дата')


    # title = models.CharField('Title', max_length = 50)
    # anons = models.CharField('Anons', max_length = 250)

    def __str__(self):
        return str(self.id)



    class Meta:
        verbose_name = "Vote"
        verbose_name_plural = "Votes"

class Profile(models.Model):
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    createdVotes = models.CharField('Созданные голосования',max_length=5000,blank=True,default = 'none')
    createdReports = models.CharField('Созданные жалобы',max_length=5000,blank=True,default = 'none')
    usedVotes = models.CharField('Участие в голосованиях',max_length=5000,blank=True,default = 'none')

    def __str__(self):
        return str(self.user)

    def get_queryset(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()