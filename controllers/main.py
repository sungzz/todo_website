# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class Todo(http.Controller):

    @http.route('/helloworld', auth='public')
    def hello_world(self):
        return('<h1>Hello World!</h1>')

    @http.route('/hello', auth='public', website=True)
    def hello(self, **kwargs):
        return request.render('todo_website.hello')

        

class Main(http.Controller):
    # link with /todo in extend.py file
    @http.route('/todo/<model("todo.task"):task>', website=True)
    def index(self, task, **kwargs):
        return http.request.render(
            'todo_website.detail', {'task': task})


    @http.route('/todo/add', website=True)
    def add(self, **kwargs):
        users = request.env['res.users'].search([])
        return request.render(
            'todo_website.add', {'users': users})