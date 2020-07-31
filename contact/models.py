from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.

STATUS = (
    ('new', 'New'),
    ('read', 'Read'),
    ('closed', 'Closed'),
)


class Contact(models.Model):

    class TALEBLER(models.TextChoices):
        SAT = 'Satmak', _('Satmak')
        SATINAL = 'Satın Almak', _('Satın Almak')
        KİRAVER = 'Kiraya Vermek', _('Kiraya Vermek')
        KİRAAL = 'Kiralamak', _('Kiralamak')
        GAYRİMENKUL = 'Gayrimenkul Değerlemesi', _('Gayrimenkul Değerlemesi')
        ARSA = 'Arsa Yatırımı', _('Arsa Yatırımı')
        DİĞER = 'Diğer', _('Diğer')
        TALEBİNİZ = 'Talebiniz', _('Talebiniz')


    subject = models.CharField(max_length=25,choices=TALEBLER.choices,default=TALEBLER.TALEBİNİZ,)

    status = models.CharField(max_length=6, choices=STATUS, default='new')
    name = models.CharField(max_length=30)
    #subject = models.CharField(blank=True, max_length=50, choices=TALEBLER, default='Diğer')
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
