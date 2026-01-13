from django.db import models


class News(models.Model):
    GAMES = [
        ('CS2', 'Counter-Strike 2'),
        ('Dota2', 'Dota 2'),
        ('Valorant', 'Valorant'),
        ('LoL', 'League of Legends'),
        ('Overwatch2', 'Overwatch 2'),
        ('Apex', 'Apex Legends'),
        ('Fortnite', 'Fortnite'),
        ('Other', 'Другое'),
    ]
    
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    game = models.CharField(max_length=20, choices=GAMES, verbose_name='Игра')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
