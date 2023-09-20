# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Alumno(models.Model):
    _name = 'alumno.alumno'
    _description = 'Modelo para Alumnos que se registran a programas'

    nombre = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellido', required=True)
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')
    nro_legajo = fields.Char(string='Nro de Legajo')
    email = fields.Char(string='Email')
    telefono = fields.Char(string='Teléfono')
    direccion = fields.Text(string='Dirección')
    pais = fields.Char(string='País')


class Programa(models.Model):
    _name = 'alumno.programa'
    _description = 'Modelo para Programas donde se registran alumnos'

    nombre = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
    alumnos_inscriptos = fields.Char(compute="get_alumnos_inscriptos", store=False)

    # @api.depends('alumno.inscripcion.programa_id')
    @api.model
    def get_alumnos_inscriptos(self, testing_call=None):
        alumnos_inscriptos = []
        for programa in self:
            print(programa)
            inscripciones = self.env['alumno.inscripcion'].search([
                ('programa_id', '=', programa.id)
            ])
            for inscripto in inscripciones:
                alumno = inscripto.alumno_id
                alumnos_inscriptos.append({
                    'nombre': alumno.nombre,
                    'apellido': alumno.apellido,
                    'legajo': alumno.nro_legajo,
                    'fecha_nacimiento': alumno.fecha_nacimiento,
                    'email': alumno.email,
                    'telefono': alumno.telefono,
                    'pais': alumno.pais
                })
        print(alumnos_inscriptos)
        return str(alumnos_inscriptos)


class Inscripcion(models.Model):
    _name = 'alumno.inscripcion'
    _description = 'Modelo para Inscripciones, Alumnos se registran a Programas'

    alumno_id = fields.Many2one('alumno.alumno', string='Alumno', required=True)
    programa_id = fields.Many2one('alumno.programa', string='Programa', required=True)
