from odoo import models, fields

class ExpenseCategory(models.Model):
    _name = 'personal.expense.category'
    _description = 'Expense Category'

    name = fields.Char(string='Category Name', required=True)
    description = fields.Text(string='Description') 