from django.db import models

class Project(models.Model):
    name = models.CharField('Название проекта', max_length=200)
    description = models.TextField('Описание', blank=True)
    city = models.CharField('Город', max_length=100)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Building(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,  # при удалении проекта — удаляются и корпуса
        related_name='buildings',   # project.buildings.all()
        verbose_name='Проект'
    )
    name = models.CharField('Название корпуса/дома', max_length=100)
    floors = models.PositiveSmallIntegerField('Этажей')
    apartments_count = models.PositiveIntegerField('Кол-во квартир')
    status = models.CharField(
        'Статус',
        max_length=20,
        choices=[
            ('planned', 'Планируется'),
            ('building', 'Строится'),
            ('completed', 'Сдан'),
        ],
        default='planned'
    )

    def __str__(self):
        return f"{self.name} ({self.project.name})"

    class Meta:
        verbose_name = 'Корпус / Дом'
        verbose_name_plural = 'Корпуса / Дома'
