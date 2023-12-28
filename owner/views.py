from django.shortcuts import render
from django.db.models import F, Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.core import serializers as ssr
from django.http import HttpResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import status

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from owner.models import Owner
from owner.forms import OwnerForm
from owner.serializers import OwnerSerializer

# Create your views here.

def owner_list(request):

    data_context = [
        {
            'nombre': 'Katty Paredes',
            'edad': 26,
            'dni': "543214567",
            'pais': "Perú",
            'vigente': False,
            'pokemons': [
                {
                    'nombre_pokemon': 'Charizard',
                    'ataques': ['Ataque 1 -Charizard', 'Ataque 2 -Charizard', 'Ataque 3 -Charizard']
                }
            ]
        },
        {
            'nombre': 'Mario Mejia',
            'edad': 22,
            'dni': "55555555",
            'pais': "Brasil",
            'vigente': False,
            'pokemons': []
        },
        {
            'nombre': 'Benito Montes',
            'edad': 27,
            'dni': "77777777",
            'pais': "Perú",
            'vigente': True,
            'pokemons': []
        }
    ]

    return render(request, 'owner_list.html', context={'data': data_context})

def owner_orm(request):


    """Crear un objeto en la tabla  Owner en la BD"""
    #owner = Owner(nombre="George Espinoza", edad=26, dni="12348765", pais="Brasil", vigente=True)
    #owner.nombre = "Margarita Tello"
    #owner.save()

    """Obtener todos los registros de la tabla Owner"""

    #data_context = Owner.objects.all()
    #print(data_context)

    """Filtración de datos: .filter()"""

    # data_context = Owner.objects.filter(nombre="María Paredes")

    """Filtración de datos con AND en SQL: .filter(     ,     )"""

    #data_context = Owner.objects.filter(nombre="María Paredes", edad=20)
    #data_context = Owner.objects.filter(pais="Perú")
    #data_context = Owner.objects.filter(pais='España', vigente=True)
    #data_context = Owner.objects.filter(nombre__startswith='Ma')
    """Filtración de datos más precisos: __contains"""

    #data_context = Owner.objects.filter(nombre__contains="evelin")

    """Filtración de datos más precisos: __endswith"""

    #data_context = Owner.objects.filter(nombre__endswith="na")

    """Obtener un solo objeto de la tabla en la BD"""

    #data_context = Owner.objects.get(dni="22222222")

    """Ordenar por cualquier atributo o campo de la tabla"""

    #data_context = Owner.objects.order_by("nombre")
    #data_context = Owner.objects.order_by("-edad")

    """Ordenar concatenando diferentes métodos ORM's"""

    #data_context = Owner.objects.filter(nombre="Camila").order_by("edad")

    """Acortar datos: Obtener un rango de registros de una tabla en la BD"""

    #data_context = Owner.objects.all()[0:5]
    #data_context = Owner.objects.all()

    """Elimnando un dato fácilmente"""

   #data_context = Owner.objects.get(id=7)
   #data_context.delete()

    """Actualización de datos en ela BD a un cierto de datos o un solo registro"""

    #Owner.objects.filter(edad=26).update(pais="España")

    """Utilizando F expressions: actualización sobre un campo"""

    #Owner.objects.filter(edad__lte=26).update(edad=F('edad') + 10)
    #data_context = Owner.objects.all()
    #data_context = Owner.objects.filter(edad__lte=33)

    """Consultas complejas"""

    #query = Q(pais__startswith='Pe') | ~Q(edad=36)
    #data_context = Owner.objects.filter(query)

    query = Q(pais__startswith='Pe') | Q(pais__startswith='Es')
    data_context = Owner.objects.filter(query, edad__lte=30)

    """Error de consulta con Q: cuando no es válido"""
    #query = Q(pais__startswith='Pe') | Q(pais__startswith='Es')
    #data_context = Owner.objects.filter(edad__lte=30, query)

    return render(request, 'owner_orm.html', context={'data': data_context})


def owner_search(request):
    query = request.GET.get('q', '')
    print("QUERY: {}".format(query))

    query_c = Q(nombre__icontains=query)
    data_context = Owner.objects.filter(query_c)

    return render(request, 'owner_search.html', context={'data': data_context, 'query': query})


def owner_details(request):
    """Obtiene todos los owner de tabla correspendiente en la BD"""

    data_context = Owner.objects.all()

    return render(request, 'owner_details.html', context={'data': data_context})


def owner_delete(request, id_owner):

    print("ID de owner: {}".format(id_owner))
    owner = Owner.objects.get(id=id_owner)
    owner.delete()

    return redirect('owner_details')


def owner_edit(request, id_owner):
    print("ID de owner: {}".format(id_owner))

    owner = Owner.objects.get(id=id_owner)
    print("Datos del owner a editar: {}".format(owner))

    form = OwnerForm(initial={'nombre': owner.nombre, 'edad': owner.edad, 'pais': owner.pais, 'dni': owner.dni})

    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)

        if form.is_valid():
            form.save()
            return redirect('owner_details')
    return render(request, 'owner_update.html', context={'data': form})


def owner_create(request):
    form = OwnerForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('owner_details')
    else:
        form = OwnerForm()

    return render(request, 'owner_create.html', context={'data': form})


class OwnerList(ListView):
    model = Owner
    template_name = 'owner_list_vc.html'


class OwnerCreate(CreateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'owner_create.html'
    success_url = reverse_lazy('owner_list_vc')


class OwnerUpdate(UpdateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'owner_update_vc.html'
    success_url = reverse_lazy('owner_list_vc')


class OwnerDelete(DeleteView):
    model = Owner
    success_url = reverse_lazy('owner_list_vc')
    template_name = "owner_confirm_delete.html"


def ListOwnerSerializer(request):
    lista_owner = ssr.serialize('json', Owner.objects.all(), fields=['nombre', 'pais', 'edad', 'dni'])

    return HttpResponse(lista_owner, content_type="application/json")

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def owner_api_view(request):

    if request.method == 'POST':
        print("Data OWNER: {}".format(request.data))
        serializers_class = OwnerSerializer(data=request.data)
        if serializers_class.is_valid():
            serializers_class.save()
            return Response(serializers_class.data, status=status.HTTP_201_CREATED)
        return Response(serializers_class.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        print("Ingresó a GET")
        queryset = Owner.objects.all()
        serializers_class = OwnerSerializer(queryset, many=True)

        return Response(serializers_class.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def owner_details_view(request, pk):
    owner = Owner.objects.filter(id=pk).first()

    if owner:
        if request.method == 'GET':
            serializers_class = OwnerSerializer(owner)
            return Response(serializers_class.data)

        elif request.method == 'DELETE':
            print("Ingresó a DELETE")
            owner.delete()
            return Response("Owner ha sido eliminado correctamente de la BD", status=status.HTTP_200_OK)

        elif request.method == "PUT":
            serializers_class = OwnerSerializer(owner, data=request.data)
            if serializers_class.is_valid():
                serializers_class.save()
                return Response(serializers_class.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializers_class.errors, status=status.HTTP_400_BAD_REQUEST)