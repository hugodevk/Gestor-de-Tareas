from flask import Flask, request, render_template

app = Flask(__name__)

tareas = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        tarea = request.form['tarea']
        tareas.append(tarea)
    return render_template("index.html", tereas=tareas)


if __name__ == "__main__":
    app.run(debug=True)

