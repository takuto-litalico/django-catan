from django.db import models
from django.db.models import Q
import math

# Create your models here.
class Player(models.Model):
        name = models.CharField(max_length=30, unique=True, blank=True)
        
        def __str__(self):
                return self.name
        @property
        def entry_num(self):
                return self.games.count()
        
        @property
        def points_gained(self):
                #２ポイント獲得&１ポイント獲得の回数
                plus = self.total_wins * 2
                plus += Score.objects.filter(player=self, rank=2, game__players__gte=5).count()
                #マイナス１ポイント&マイナス２ポイント
                minus = Score.objects.filter(Q(player=self), Q(score=5) | Q(score=6)).count()
                minus += Score.objects.filter(Q(player=self), Q(score__gte=2), Q(score__lte=4)).count()*2
                return plus - minus
        
        @property
        def total_wins(self):
                namae = Player.objects.filter(name=self.name)[0]
                return Score.objects.filter(player=namae, rank=1).count()
        
        @property
        def win_rate(self):
                win_num = self.total_wins
                entry = self.entry_num
                a = math.floor(win_num / entry * 100 * 100) / 100
                return a
        
        @property
        def total_score(self):
                namae = Player.objects.filter(name=self.name)[0]
                score_list = []
                for score_obj in Score.objects.filter(player=namae):
                        score = score_obj.score
                        score_list.append(score)
                return sum(score_list)
        
        @property
        def average_score(self):
                goukei = self.total_score
                shutsujo = self.entry_num
                b = math.floor(goukei / shutsujo * 100) / 100
                return b
        
        @property
        def player_info(self):
                return tuple(self.entry_num, self.points_gained, self.total_wins, self.win_rate, self.total_score, self.average_score)
                
class Game(models.Model):
        players = models.ManyToManyField(Player, related_name="games")
        datetime = models.DateTimeField(auto_now_add=True)
        place = models.CharField(max_length=30, blank=False, default="塩光宅")
        
        def __str__(self):
                return f'{self.datetime}, {self.place}'

class Score(models.Model):
        player = models.ForeignKey(Player, related_name="scores", on_delete=models.CASCADE)
        game = models.ForeignKey(Game, related_name="scores", on_delete=models.CASCADE)
        score = models.IntegerField(default=0, blank=True)
        rank = models.IntegerField(default=0, blank=True)
