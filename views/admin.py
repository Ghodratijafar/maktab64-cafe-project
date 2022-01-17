from models import *
from flask import Flask
from flask import redirect, url_for, request, render_template, escape, render_template_string, Response, jsonify
from models import cashier, category, menu_items, order_item, orders, table, reciepts
import json


def login():
    print("login")
    if request.method == "POST":
        cashier_dict = cashier.CashierModels.read_all()
        for c in cashier_dict:
            if escape(request.form.get('phone')) == cashier_dict[c]['phone'] and \
                    escape(request.form.get('password')) == cashier_dict[c]['password']:
                return render_template('cashier/adminpage2.html', data=c)
    elif request.method == 'GET':
        return render_template('cashier/login.html')


def register():
    if request.method == 'GET':
        return render_template('cashier/login.html')
    elif request.method == 'POST':
        cashier.CashierModels(escape(request.form.get('firstname')), escape(request.form.get('lastname')),
                              escape(request.form.get('phone')),
                              escape(request.form.get('password')), escape(request.form.get('email')))
        return render_template('cashier/login.html')
    return None


def admin_page():
    if request.method == 'GET':
        category_dict = category.CategoryModels.read_all()
        menu_dict = menu_items.MenuItems.read_all()
        order_dict = orders.Order.read_all()
        order_item_dict = order_item.OrderItem.read_all()
        table_dict = table.TableModels.read_all()
        receipts_dict = reciepts.Receipt.read_all()
        return render_template('cashier/adminpage2.html', category_dict=category_dict, menu_dict=menu_dict,
                               order_dict=order_dict,
                               order_item_dict=order_item_dict, table_dict=table_dict, receipts_dict=receipts_dict)
    return None


def order():
    if request.method == "GET":
        menu_dict = menu_items.MenuItems.read_all()
        order_dict = orders.Order.read_all()
        order_item_dict = order_item.OrderItem.read_all()
        return jsonify({'data': render_template('cashier/orders.html', menu_dict=menu_dict, order_dict=order_dict,
                                                order_item_dict=order_item_dict)})
    return None


def receipt():
    if request.method == 'GET':
        receipts_dict = reciepts.Receipt.read_all()
        return jsonify({'data': render_template('cashier/recipts.html', receipts_dict=receipts_dict)})
    return None


def menu_item():
    if request.method == 'GET':
        menu_dict = menu_items.MenuItems.read_all()
        return jsonify({'data': render_template('cashier/menuitems.html', menu_dict=menu_dict)})
    elif request.method == 'POST':
        if request.form.get('Name') and request.form.get('Price') and request.form.get('Image') \
                and request.form.get('Description') and request.form.get('Category')and request.form.get('Discount') and request.form.get('Serv_time')\
                and request.form.get('St_cooking_time'):

            name = request.form['Name']
            price = request.form['Price']
            image = request.form['Image']
            description = request.form['Description']
            category = request.form['Category']
            discount = request.form['Discount']
            serv_time = request.form['Serv_time']
            st_cooking_time = request.form['St_cooking_time']
            menu_items.MenuItems(name, price, image, description, category, discount,serv_time,st_cooking_time)
            return jsonify({'data': render_template('cashier/menuitems.html')})
        elif request.form.get('id_Delete'):
            id_delete = request.form["id_Delete"]
            menu_items.MenuItems.delete(id_delete)
            return jsonify({'data': render_template('cashier/menuitems.html.html')})


def categories():
    if request.method == 'GET':
        return jsonify({'data': render_template('cashier/category.html')})
    elif request.method == 'POST':
        req = request.form.get
        category.CategoryModels(req('title'), req('root'))
        return render_template('cashier/category.html')


def about():
    if request.method == 'GET':
        return render_template('Customer/about.html')


def team():
    if request.method == "GET":
        return render_template('Customer/team.html')


def tables():
    if request.method == 'GET':
        table_dict = table.TableModels.read_all()
        return jsonify({'data': render_template('cashier/table.html', table_dict=table_dict)})
