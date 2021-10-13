from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='тэг', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class WHEvent(models.Model):
    SYSTEMS = [
        ('40k', '40k'),
        ('AOS', 'AOS'),
        #  ('AERO', 'Warhammer Aeronautica'),
        ('KT', 'Kill Team'),
        ('WC', 'WarCry'),
    ]
    """
    событие - турик или еще что-то
    """
    name = models.CharField(max_length=100, verbose_name='Название ивента')
    source_link = models.CharField(max_length=200, verbose_name='Ссылка на ивент')
    date_of_event = models.DateField(verbose_name='Дата проведения')
    system = models.CharField(choices=SYSTEMS, verbose_name='Система по которой проходит турнир', max_length=100)
    tags = models.ManyToManyField(Tag, verbose_name='Тэги ивента')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ивент'
        verbose_name_plural = 'Ивенты'

