from application import app, db
from application.models import Tasks
from flask import render_template, request, redirect, url_for
from application.forms import TaskForm

@app.route('/')
@app.route('/home')
def home():
    all_tasks = Tasks.query.all()
    output = ""
    return render_template("index.html", title="Home", all_tasks=all_tasks)    

@app.route('/create', methods=["GET","POST"])
def create():
    form = TaskForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_task = Tasks(desc=form.desc.data)
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template("add.html", title='Create a task', form=form)

@app.route('/update/<int:id>', methods=["GET","POST"])
def update(id):
    task = Tasks.query.filter_by(id=id).first()
    form = TaskForm()
    if request.method == "POST":
        task.desc = form.desc.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=form, title="Update Task", task=task)

@app.route('/delete/<int:id>', methods=["GET","POST"])
def delete(id):
    task = Tasks.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('home'))
    


@app.route('/complete/<int:id>')
def complete(id):
    task = Tasks.query.filter_by(id=id).first()
    task.status = True
    db.session.commit()
    return f'Tast {id} is now complete'

@app.route('/incomplete/<int:id>')
def incomplete(id):
    task = Tasks.query.filter_by(id=id).first()
    task.status = False
    db.session.commit()
    return f'Tast {id} is now incomplete'

