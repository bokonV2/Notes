from flask import Blueprint, render_template, url_for, redirect, request
from notes.objekt import *

notes = Blueprint('notes', __name__, template_folder='templates', static_folder='static')

@notes.route('/')
def index():
    obj = Notes.select().order_by(Notes.pin.desc())
    try:
        return render_template('notes/index.html', obj=obj, style=Config.select()[0].style)
    except:
        return render_template('notes/index.html', style=Config.select()[0].style)

@notes.route('/style/<st>')
def style(st):
    cnf = Config.select()[0]
    cnf.style = st
    cnf.save()
    return redirect('/notes/')

@notes.route('/delNote', methods=['POST'])
def delNote():
    id = request.form.get('id')
    obj = Notes.get(Notes.id == id)
    obj.delete_instance()
    return "data"

@notes.route('/pinNote', methods=['POST'])
def pinNote():
    id = request.form.get('id')
    obj = Notes.get(Notes.id == id)
    obj.pin = 1 if obj.pin == 0 else 0
    obj.save()
    return "data"

@notes.route('/setColor', methods=['POST'])
def setColor():
    print(request.form)
    id = request.form.get('id')
    color = request.form.get('color')
    obj = Notes.get(Notes.id == id)
    obj.color = color
    obj.save()
    return "data"

@notes.route('/search', methods=['POST'])
def search():
    print(request.form)
    field = request.form.get('field')
    obj = Notes.select().where(
        Notes.title.contains(field) | Notes.message.contains(field)
        ).execute()
    return render_template('notes/index.html', obj=obj, style=Config.select()[0].style)

@notes.route('/sort/<int:id>')
def sort(id):
    if id == 1:
        obj = Notes.select().order_by(Notes.date)
    elif id == 2:
        obj = Notes.select().order_by(Notes.date.desc())
    return render_template('notes/index.html', obj=obj, style=Config.select()[0].style)

@notes.route('/addNote', methods=['POST', 'GET'])
def addNote():
    if request.method == 'POST':
        title = request.form.get('title')
        message = request.form.get('message')
        Notes.create(
            title=title,
            message=message,
            color="blue"
        )
        return "data"
    return render_template('notes/addNotes.html', style=Config.select()[0].style)

@notes.route('/editNote', methods=['POST'])
def editNote():
    title = request.form.get('title')
    message = request.form.get('message')
    id = request.form.get('id')
    obj = Notes.get(Notes.id == id)
    obj.title = title
    obj.message = message
    obj.save()
    return "data"

@notes.route('/notes/<int:id>')
def getNote(id):
    obj = Notes.get(Notes.id == id)
    return render_template('notes/editNotes.html', obj=obj, style=Config.select()[0].style)
