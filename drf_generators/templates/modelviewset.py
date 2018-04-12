
__all__ = ['MODEL_URL', 'MODEL_VIEW']


MODEL_URL = """from rest_framework.routers import SimpleRouter
from {{ app }} import views


router = SimpleRouter()
{% for model in models %}
router.register(r'{{ model | lower }}', views.{{ model }}ViewSet){% endfor %}

urlpatterns = router.urls
"""


MODEL_VIEW = """from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from {{ app }}.serializers import {{ serializers|join:', ' }}
from {{ app }}.models import {{ models|join:', ' }}
{% for model in models %}

class {{ model }}ViewSet(ModelViewSet):
    __doc__ = ModelViewSet.__doc__
    
    queryset = {{ model }}.objects.all()
    serializer_class = {{ model }}Serializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'
{% endfor %}"""
