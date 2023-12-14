# -*- coding: utf-8 -*-

from odoo import models, fields, api

class empresas_contratadoras(models.Model):
    _name = 'empresas_contratadoras'
    _description = 'Empresas Contratadoras'

    name = fields.Char(string="Nombre")
    proyectos_contratados = fields.Many2many("project.project", string="Proyectos Contratados")
    cantidad_tareas = fields.Integer(string="Cantidad de tareas", compute="_compute_cantidad_tareas", store=True)

    @api.depends('proyectos_contratados.tareas')
    def _compute_cantidad_tareas(self):
        for empresa in self:
            cantidad_tareas = 0
            for proyecto in empresa.proyectos_contratados:
                cantidad_tareas += len(proyecto.tareas)
            empresa.cantidad_tareas = cantidad_tareas

class proyectos(models.Model):
    _name = 'project.project'
    _inherit = 'project.project'

    empresa_contratadora = fields.Many2one("empresas_contratadoras", string="Empresa Contratadora", inverse_name='proyectos_contratados')
    tareas = fields.One2many("project.task", "project_id", string="Tareas")
