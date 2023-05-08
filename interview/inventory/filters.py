import django_filters
from django.db import models as django_models
from django_filters import rest_framework as filters
from rest_framework import viewsets
from .models import Inventory

class InventoryFilter(filters.FilterSet):
    class Meta:
        model = Inventory
        fields = {
            'created_at': ('gte',)
        }

    filter_overrides = {
        django_models.DateTimeField: {
            'filter_class': django_filters.IsoDateTimeFilter
        },
    }
