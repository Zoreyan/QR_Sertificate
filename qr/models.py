from django.db import models

class Settings(models.Model):
    title = models.CharField(max_length=40, null=True)
    template = models.FileField(upload_to='templates/', null=True)
    x = models.IntegerField(null=True, default=0)
    y = models.IntegerField(null=True, default=0)
    font_size = models.CharField(max_length=2, null=True, default=16)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Настройки'
        verbose_name_plural = 'Настройки'


class Sertificate(models.Model):
    image = models.FileField(upload_to='sertificates/', null=True, blank=True)
    name = models.CharField(max_length=150, null=True)
    created = models.DateField(auto_now_add=True)
    settings = models.ForeignKey(Settings, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'
    

