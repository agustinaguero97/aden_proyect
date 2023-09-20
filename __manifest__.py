# -*- coding: utf-8 -*-
{
    'name': "alumno",

    'summary': """
        modulo donde alumnos se inscriben a programas
    """,

    'description': """
        Crear un modulo de Odoo versión 15 que cumpla con lo siguiente:
            - Modelo Alumno que contenga los siguientes datos:
                - Nombre
                - Apellido
                - Fecha de nacimiento
                - Nro de legajo
                - Email
                - Teléfono
                - Dirección
                - País
            - Modelo Programa que contenga nombre y descripción
            - Modelo Inscripción que permita registrar que un alumno está inscripto a un programa
            - Función dentro del modelo programa que reciba como parámetro un programa
                y que retorne una lista de todos los alumnos que están inscriptos en el programa.
            Ejemplo de respuesta:
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
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'application': True,

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
