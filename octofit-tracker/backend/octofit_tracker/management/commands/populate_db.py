from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data in correct order (children before parents)
        Activity.objects.all().delete()
        User.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        Team.objects.all().delete()

        # Create teams with integer IDs
        marvel = Team.objects.create(id=1, name='Marvel')
        dc = Team.objects.create(id=2, name='DC')

        # Create users with integer IDs
        users = [
            User.objects.create(id=1, name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(id=2, name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(id=3, name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(id=4, name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create activities with integer IDs
        activity_id = 1
        for user in users:
            Activity.objects.create(id=activity_id, user=user, type='Running', duration=30, date='2026-03-04')
            activity_id += 1
            Activity.objects.create(id=activity_id, user=user, type='Cycling', duration=45, date='2026-03-04')
            activity_id += 1

        # Create workouts with integer IDs
        Workout.objects.create(id=1, name='Full Body', description='A full body workout')
        Workout.objects.create(id=2, name='Cardio Blast', description='Intense cardio session')

        # Create leaderboard with integer IDs
        Leaderboard.objects.create(id=1, team=marvel, total_minutes=100)
        Leaderboard.objects.create(id=2, team=dc, total_minutes=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
