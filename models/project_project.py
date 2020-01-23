# -*- coding: utf-8 -*-
from odoo import api, fields, models

class ProjectProject(models.Model):
    _inherit = 'project.project'
    repo_url = fields.Char(
        string='Repository URL',
    )
    odoo_version = fields.Char(
    )
    proj_domain = fields.Char(
        string='Project Domain',
    )
    ip_domain = fields.Char(
        string='IP/Domain',
    )
    user = fields.Char(
    )
    password = fields.Char(
    )
    masterpass = fields.Char(
        string='Master Password',
    )
    addons = fields.Char(
    )
    config = fields.Char(
        string='Configurations',
    )
    daemon = fields.Char(
    )
    log = fields.Char(
    )
    
    
    
    