from django.core.management.base import BaseCommand
from tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(_id=ObjectId(), email='thundergod@mhigh.edu', name='Thor', age=30, team='Blue Team'),
            User(_id=ObjectId(), email='metalgeek@mhigh.edu', name='Tony Stark', age=35, team='Gold Team'),
            User(_id=ObjectId(), email='zerocool@mhigh.edu', name='Steve Rogers', age=32, team='Blue Team'),
            User(_id=ObjectId(), email='crashoverride@hmhigh.edu', name='Natasha Romanoff', age=28, team='Gold Team'),
            User(_id=ObjectId(), email='sleeptoken@mhigh.edu', name='Bruce Banner', age=40, team='Blue Team'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        teams = [
            Team(name='Blue Team', description='Team focused on endurance training'),
            Team(name='Gold Team', description='Team focused on strength training'),
        ]
        Team.objects.bulk_create(teams)

        # Create activities
        activities = [
            Activity(user=users[0], activity_type='Cycling', duration=60, date='2025-04-15'),
            Activity(user=users[1], activity_type='Crossfit', duration=120, date='2025-04-14'),
            Activity(user=users[2], activity_type='Running', duration=90, date='2025-04-13'),
            Activity(user=users[3], activity_type='Strength', duration=30, date='2025-04-12'),
            Activity(user=users[4], activity_type='Swimming', duration=75, date='2025-04-11'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(user=users[0], score=100),
            Leaderboard(user=users[1], score=90),
            Leaderboard(user=users[2], score=95),
            Leaderboard(user=users[3], score=85),
            Leaderboard(user=users[4], score=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event', duration=60),
            Workout(name='Crossfit', description='Training for a crossfit competition', duration=120),
            Workout(name='Running Training', description='Training for a marathon', duration=90),
            Workout(name='Strength Training', description='Training for strength', duration=30),
            Workout(name='Swimming Training', description='Training for a swimming competition', duration=75),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))