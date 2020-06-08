from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, SleepSerializer, DreamSerializer, PeopleSerializer, \
    QuestionnaireEntrySerializer
from .models import User, Sleep, Dream, People, QuestionnaireEntry


@api_view(['GET', 'POST'])
def dream_list(request):
    if request.method == 'GET':
        dreams = Dream.objects.all()
        serializer = DreamSerializer(dreams, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DreamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def sleep_list(request):
    if request.method == 'GET':
        sleeps = Sleep.objects.all()
        serializer = SleepSerializer(sleeps, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SleepSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
def dream_by_post_id(request, post):
    try:
        dream = Dream.objects.get(post=post)
    except Dream.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DreamSerializer(dream)
        return Response(serializer.data)


@api_view(['GET', ])
def sleep_by_post_id(request, post):
    try:
        sleep = Sleep.objects.get(post=post)
    except Sleep.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SleepSerializer(sleep)
        return Response(serializer.data)


@api_view(['GET', ])
def q_result_by_post_id(request, post):
    try:
        result = QuestionnaireEntry.objects.get(post=post)
    except QuestionnaireEntry.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = QuestionnaireEntrySerializer(result)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = QuestionnaireEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def people_by_post_id(request, post):
    try:
        people = People.objects.get(post=post)
    except People.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PeopleSerializer(people)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PeopleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', ])
def update_dream(request, post):
    try:
        dream = Dream.objects.get(post=post)
    except Dream.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = DreamSerializer(dream, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["succeeded"] = True
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', ])
def update_sleep(request, post):
    try:
        sleep = Sleep.objects.get(post=post)
    except Sleep.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = SleepSerializer(sleep, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["succeeded"] = True
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', ])
def update_people(request, post):
    try:
        people = People.objects.get(post=post)
    except People.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = PeopleSerializer(people, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["succeeded"] = True
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', ])
def update_add_lucidity_to_dream(request, post, q_result):
    try:
        dream = Dream.objects.get(post=post)
        dream.lucidity = q_result
        dream.save()
    except Dream.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = DreamSerializer(dream, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["succeeded"] = True
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
