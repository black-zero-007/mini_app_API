# Author:JZW
from rest_framework.filters import BaseFilterBackend
from api import models

class MinFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        min_id = request.query_params.get('min_id')
        topic_id = request.query_params.get('topic_id')
        token = request.query_params.get('token')
        if min_id:
            if topic_id:
                return models.News.objects.filter(id__lt=min_id,topic_id=topic_id).order_by('-id')
            elif token:
                user = models.UserInfo.objects.filter(token=token).first()
                return models.News.objects.filter(id__lt=min_id,user=user).order_by('-id')
            else:
                return models.News.objects.filter(id__lt=min_id).order_by('-id')
        return queryset

class MaxFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        max_id = request.query_params.get('max_id')
        topic_id = request.query_params.get('topic_id')
        token = request.query_params.get('token')
        if max_id:
            if topic_id:
                return models.News.objects.filter(id__gt=max_id,topic_id=topic_id).order_by('id')
            elif token:
                user = models.UserInfo.objects.filter(token=token).first()
                return models.News.objects.filter(id__gt=max_id,user=user).order_by('id')
            else:
                return models.News.objects.filter(id__gt=max_id).order_by('id')
        return queryset

class CollectMaxFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        max_id = request.query_params.get('max_id')
        return queryset.filter(id__gt=max_id).order_by('id')

class CollectMinFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        min_id = request.query_params.get('min_id')
        return queryset.filter(id__lt=min_id).order_by('-id')