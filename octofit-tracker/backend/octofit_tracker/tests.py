from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(id=1, name='Marvel')
        dc = Team.objects.create(id=2, name='DC')
        User.objects.create(id=1, name='Spider-Man', email='spiderman@marvel.com', team=marvel)
        User.objects.create(id=2, name='Batman', email='batman@dc.com', team=dc)

    def test_user_team(self):
        user = User.objects.get(name='Spider-Man')
        self.assertEqual(user.team.name, 'Marvel')
