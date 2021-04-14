# -*- coding: utf-8 -*-

from odoo import models, fields, api


# Nuevo codigo
class ResUsers(models.Model):
  _inherit = 'res.users'


  @api.model
  def create(self, values):
    
    if self.env['res.partner'].browse(values['partner_id']).supplier:
      values.update({'password': '123456'})

    
    return super(ResUsers, self).create(values)
  