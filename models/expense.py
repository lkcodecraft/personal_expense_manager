from odoo import models, fields, api

class Expense(models.Model):
    _name = 'personal.expense'
    _description = 'Expense Record'
    _inherit = ['mail.thread']

    date = fields.Date(
        string='Date',
        default=fields.Date.context_today,
        required=True
    )
    category_id = fields.Many2one(
        'personal.expense.category',
        string='Category',
        required=True
    )
    amount = fields.Float(string='Amount', required=True)
    description = fields.Text(string='Notes')
    paid = fields.Boolean(string='Paid', default=False)

    @api.multi
    def mark_as_paid(self):
        for rec in self:
            rec.paid = rec and True or False 