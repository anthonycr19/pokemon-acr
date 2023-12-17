from django.shortcuts import render

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

    data_context = Owner.objects.all()
    print(data_context)

    return render(request, 'owner_orm.html', context={'data': data_context})

