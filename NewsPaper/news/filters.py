from django_filters import FilterSet, CharFilter, BooleanFilter
from .models import Post


class PostFilter(FilterSet):
    class Meta:
       model = Post
       fields = {
            'name': ['icontains'],
            'author': ['icontains'],
            'time_of': ['date'],
            }
