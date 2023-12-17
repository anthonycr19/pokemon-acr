from django.shortcuts import render
from django.db.models import F, Q
from owner.models import Owner

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