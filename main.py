from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from Calculator import Calculator
from Temperature import Temperature



app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class CaloriesFormPage(MethodView):

    def get(self):
        calories_form = CaloriesForm()
        return render_template('calories_form_page.html',
                               caloriesform=calories_form)

    def post(self):
        calories_form = CaloriesForm(request.form)

        temperature = Temperature(state=calories_form.state.data,
                                  city=calories_form.city.data).scrape()

        calorie = Calculator(weight=float(calories_form.weight.data),
                          height=float(calories_form.height.data),
                          age=float(calories_form.age.data),
                          temperature=float(temperature))

        calories = str(calorie.calculate())

        return render_template('calories_form_page.html',
                               caloriesform=calories_form,
                               calories=calories,
                               result=True)


class CaloriesForm(Form):
    weight = StringField("Weight: ", default=75)
    height = StringField("Height: ", default=180)
    age = StringField("Age: ", default=35)
    state = StringField("State: ", default="czech republic")
    city = StringField("City: ", default="brno")
    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calories_form', view_func=CaloriesFormPage.as_view('calories_form_page'))

app.run(debug=True)