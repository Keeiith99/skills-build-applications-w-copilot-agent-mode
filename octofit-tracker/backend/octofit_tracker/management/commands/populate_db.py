from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)

        # Create Activities
        Activity.objects.create(user=tony, type='Running', duration=30, date=date(2025, 12, 1))
        Activity.objects.create(user=steve, type='Cycling', duration=45, date=date(2025, 12, 2))
        Activity.objects.create(user=bruce, type='Swimming', duration=60, date=date(2025, 12, 3))
        Activity.objects.create(user=clark, type='Yoga', duration=20, date=date(2025, 12, 4))

        # Create Workouts
        Workout.objects.create(name='Super Strength', description='Strength workout for heroes', suggested_for='Marvel')
        Workout.objects.create(name='Flight Training', description='Flight skills for Kryptonians', suggested_for='DC')

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
