from ACMEAPI.models import Tarefa
from rest_framework import serializers

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'