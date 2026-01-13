from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import News


def news_list(request):
    game_filter = request.GET.get('game', None)
    
    if game_filter:
        news_list = News.objects.filter(game=game_filter)
    else:
        news_list = News.objects.all()
    
    games = News.GAMES
    
    context = {
        'news_list': news_list,
        'games': games,
        'current_game': game_filter,
    }
    return render(request, 'news/news_list.html', context)


def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'news/news_detail.html', {'news': news})
