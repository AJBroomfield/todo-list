from application import app, db
from application.models import Tasks

@app.route('/')
@app.route('/home')
def home():
    all_tasks = Tasks.query.all()
    return str(all_tasks)

@app.route('/create')
def create():
    new_todo = Task(description='New Task')
    db.session.add(new_todo)
    db.session.commit()
    return "New Task Added"

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

@app.route('/update/<new_description>')
def update(new_description):
    task = Tasks.questy.order_by(Tasks.id.desc()).first()
    task.desc = new_description
    db.session.commit()
    return f'Most recent task description has been updated to: {new_description}'