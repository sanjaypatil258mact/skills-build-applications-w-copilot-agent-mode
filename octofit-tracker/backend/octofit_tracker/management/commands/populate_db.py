from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as octo_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        self.stdout.write(self.style.WARNING('Deleting old data...'))
        octo_models.Team.objects.all().delete()
        octo_models.Activity.objects.all().delete()
        octo_models.Leaderboard.objects.all().delete()
        octo_models.Workout.objects.all().delete()
        get_user_model().objects.all().delete()

        # Create Teams
        marvel = octo_models.Team.objects.create(name='Marvel')
        dc = octo_models.Team.objects.create(name='DC')

        # Create Users
        ironman = get_user_model().objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel)
        captain = get_user_model().objects.create_user(username='captain', email='captain@marvel.com', password='password', team=marvel)
        batman = get_user_model().objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc)
        superman = get_user_model().objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc)

        # Create Activities
        octo_models.Activity.objects.create(user=ironman, type='run', duration=30, distance=5)
        octo_models.Activity.objects.create(user=batman, type='cycle', duration=60, distance=20)
        octo_models.Activity.objects.create(user=superman, type='swim', duration=45, distance=2)
        octo_models.Activity.objects.create(user=captain, type='run', duration=25, distance=4)

        # Create Workouts
        octo_models.Workout.objects.create(user=ironman, name='Chest Day', description='Bench press and pushups')
        octo_models.Workout.objects.create(user=batman, name='Leg Day', description='Squats and lunges')
        octo_models.Workout.objects.create(user=superman, name='Cardio', description='Running and swimming')
        octo_models.Workout.objects.create(user=captain, name='Arms', description='Curls and triceps')

        # Create Leaderboard
        octo_models.Leaderboard.objects.create(team=marvel, points=100)
        octo_models.Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
