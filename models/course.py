#-*- coding: utf-8 -*-

from odoo import models, fields, api


class course(models.Model):
    _name = 'open_academy.course'
    _description = 'Course'

    name = fields.Char(string="Course")
    title = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible", index=True)

