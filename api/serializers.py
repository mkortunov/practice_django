from rest_framework import serializers
from .models import *

class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('actor_id', 'first_name', 'last_name', 'last_update', )
        model = Actor