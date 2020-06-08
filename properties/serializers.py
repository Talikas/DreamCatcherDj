from rest_framework import serializers
from .models import User, Dream, Sleep, People, QuestionnaireEntry


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'level')


class SleepSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sleep
        fields = ['post', 'user_no', 'time', 'physical_activity', 'food_consumption', 'dream_remembered',
                  'day', 'month', 'year']


class DreamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dream
        fields = ('user_no','post', 'people_exist', 'sound', 'musical', 'grayscale', 'experience',
                  'lucidity', 'title', 'content', 'interpretation', 'day', 'month', 'year')


class PeopleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = People
        fields = ('user_no', 'post', 'first_name', 'second_name', 'third_name', 'fourth_name', 'fifth_name',
                  'sixth_name', 'seventh_name', 'eighth_name', 'ninth_name', 'tenth_name', 'first_impression',
                  'second_impression', 'third_impression', 'fourth_impression', 'fifth_impression', 'sixth_impression',
                  'seventh_impression', 'eighth_impression', 'ninth_impression', 'tenth_impression')


class QuestionnaireEntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestionnaireEntry
        fields = (
            'user_no', 'post', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13',
            'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'result')
