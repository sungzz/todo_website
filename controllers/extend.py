# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.todo_website.controllers.main import Todo

class TodoExtended(Todo):
    @http.route(['/hello', '/hello/<name>'])
    def hello(self, name=None, ** kwargs):
        response = super(TodoExtended, self).hello()
        response.qcontext['name'] = name
        return response

    @http.route('/hellocms/<page>', auth='public')
    def hello(self, page, ** kwargs):
        return http.request.render(page)


class Main(http.Controller):
    # link with /todo in main.py file
    @http.route('/todo', auth="user", website="True")
    def index(self, **kwargs):
        TodoTask = request.env['todo.task']
        tasks = TodoTask.search([])
        return request.render(
            'todo_website.index', {'tasks': tasks})