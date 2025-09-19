from django.shortcuts import get_object_or_404, render
from ACMEAPI.models import Tarefa
from ACMEAPI.serializers import TarefaSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def visao_geral(request):
    api_urls = {
        'todas_as_tarefas': '/all',
        'Buscar por titulo': '/?titulo=nome_titulo',
        'Buscar por id': '/?id=numero_id',
        'Adicionar': '/create',
        'Atualizar': '/update/pk',
        'Deletar': '/tarefa/pk/delete',
    }
    
    return Response(api_urls)

@api_view(['POST'])
def tarefa_adicionar(request):
    tarefa = TarefaSerializer(data=request.data)
    
    if tarefa.is_valid():
        tarefa.save()
        return Response(tarefa.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def tarefa_consultar(request):
    if request.query_params:
        tarefas = Tarefa.objects.filter(**request.query_params.dict())
    else:
        tarefas = Tarefa.objects.all()
        
    if tarefas:
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def tarefa_atualizar(request, pk):
    tarefa = Tarefa.objects.get(pk=pk)
    data = TarefaSerializer(instance=tarefa, data=request.data)
    
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def tarefa_deletar(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    tarefa.delete()
    return Response(status=status.HTTP_202_ACCEPTED)