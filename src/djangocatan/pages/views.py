from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from info.models import Player, Game, Score

from .models import Person, Example
from .forms import PersonForm, addgameForm, ExampleForm


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

#プレイヤー情報をPOSTから抽出
def get_player_data(post_dict, player_num=6):
    result = []
    for i in range(1, player_num+1):
        name = post_dict[f'name_{i}'][0]
        score = post_dict[f'score_{i}'][0]
        if name != "" and score != "":
            result.append((name, score))
    return result

#各部のランキングを作成
def create_rank():
    players = Player.objects.all()
    en_dict = {}
    pg_dict = {}
    tw_dict = {}
    wr_dict = {}
    ts_dict = {}
    as_dict = {}
    dict_list = [en_dict, pg_dict, tw_dict, wr_dict, ts_dict, as_dict]
    for pl in players:
        name = pl.name
        info = pl.player_info
        i = 0
        while i < 7:
            dict_list[i][f'{name}'] = info[i]
            i += 1
    result = []
    for dic in dict_list:
        result.append(sorted(dic, key=lambda x:x[1]))
    return result

#ゲームデータを追加するページ
def addgame_view(request, *args, **kwargs):
    context = {"range": [1, 2, 3, 4, 5, 6]}
    if request.method == "GET":
        return render(request, "addgame.html", context)
    if request.method == "POST":
        #ここにデータ処理の内容を書く。
        playerdata = get_player_data(dict(request.POST))
        game = Game.objects.create()
        for player in playerdata:
            score = player[1]
            pl, _ = Player.objects.get_or_create(name=player[0])
            game.players.add(pl)
            #注目するべき順位は１位、２位のみ
            if playerdata.index(player) == 0:
                rank = 1
                Score.objects.create(player=pl, game=game, score=score, rank=rank)
            elif player[1] == playerdata[1][1]:
                rank = 2
                Score.objects.create(player=pl, game=game, score=score, rank=rank)
            else:
                Score.objects.create(player=pl, game=game, score=score)
        return render(request, "addgame.html", context)

#ランキングを表示するページ
def rank_view(request, *args, **kwargs):
    if request.method == "GET":
        players = Player.objects.all()
        context = {"players": players}
        context["order_by_points_gained"] = sorted(players, key=lambda p: p.points_gained, reverse=True)
        return render(request, "rank.html", context)
    




#########################################

class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = "eg.html"
    success_url = "/create"

def ExampleView(request):
    form = ExampleForm()
    return render(request, "example.html", {"form": form})

'''
class ExampleCreateView(CreateView):
    mdoel = Example
    form_class = ExampleForm
    template = "example.html"
    success_url = "/index"
'''