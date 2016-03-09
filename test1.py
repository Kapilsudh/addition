from flask import Flask, render_template, request
from wtforms import Form, FloatField, validators
#from compute import compute

app = Flask(__name__)

# Model
class InputForm(Form):
    n1 = FloatField(validators=[validators.InputRequired()])
    n2 = FloatField(validators=[validators.InputRequired()])

# View
@app.route('/hw1', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        n1 = form.n1.data
        n2=form.n2.data
        s = n1+n2
        return render_template("adding.html", form=form, s=s)
    else:
        return render_template("adding.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
    