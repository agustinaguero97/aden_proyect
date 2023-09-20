# aden_proyect

code challengue: Proyecto en Odoo 15

## especificaciones del challengue

Crear un modulo de Odoo versión 15 que cumpla con lo siguiente:
1. Modelo Alumno que contenga los siguientes datos:
    1. Nombre
    2. Apellido
    3. Fecha de nacimiento
    4. Nro de legajo
    5. Email
    6. Teléfono
    7. Dirección
    8.  País

2. Modelo Programa que contenga 
    1. nombre
    2. descripción

3. Modelo Inscripción que permita registrar que un alumno está inscripto a un programa

4. Función dentro del modelo programa que reciba como parámetro un programa y que retorne una lista de todos los alumnos que están inscriptos en el programa.
Ejemplo de respuesta:

```json
    [
        {
            'nombre': 'Cristian',
            'apellido': 'Ruppert',
            'legajo': 12548,
            'fecha_nacimiento': '1993-10-29'
            'email': 'cristian.ruppert@aden.org',
            'telefono': '+5492616861427',
            'pais': {
                'id': 587,
                'nombre': 'Argentina'
            }
        },
        {
            'nombre': 'Philipp',
            'apellido': 'Anderson',
            'legajo': 12549,
            'fecha_nacimiento': '1989-04-30'
            'email': 'philipp.anderson@test.com',
            'telefono': '+54912311111',
            'pais': {
                'id': 587,
                'nombre': 'Argentina'
            }
        }
    ]
```