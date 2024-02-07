import json
from flask import Flask,redirect, render_template, request, url_for
import emcalc 
import deciMake
import socialIncli
import socialWell
import curiosityQ

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/aboutUs')
def aboutUs():
    return render_template('aboutUs.html')

@app.route('/instructions')
def instructions():
    return render_template('instructions.html')

@app.route('/takeTest')
def takeTest():
    name = request.args.get('name')
    age = request.args.get('age') 
    return render_template('takeTest.html',name=name,age=age)

@app.route('/submit_colors', methods=['POST'])
def submit_colors():
    if request.method == 'POST':
        name = request.form.get('name') 
        age = request.form.get('age')
        colors_str = request.form.get('colors')
        print('Received colors:', colors_str)
        colors1 = [int(value) for value in colors_str.split(',')[:3]]  
        colors2=[int(value)for value in colors_str.split(',')[3:6]]
        colors3=[int(value) for value in colors_str.split(',')[6:9]]
        colors4=[int(value)for value in colors_str.split(',')[9:12]]
        colors5=[int(value)for value in colors_str.split(',')[12:]]
        print(colors1,colors2,colors3,colors4,colors5)
        emp_per = emcalc.weights_cal(*colors1)
        deci_per=deciMake.weights_cal(*colors2)
        social_incli=socialIncli.weights_cal(*colors3)
        social_well_per=socialWell.weights_cal(*colors4)
        curiosity_per=curiosityQ.weights_cal(*colors5)
        return redirect(url_for('show_result', emp_per=emp_per,deci_per=deci_per,social_incli=social_incli,social_well_per=social_well_per,curiosity_per=curiosity_per,name=name,age=age))
    else:
        return redirect(url_for('home'))
@app.route('/result')
def show_result():
    deci_per=request.args.get('deci_per','')
    emp_per = request.args.get('emp_per', '')
    social_incli=request.args.get('social_incli', '')
    social_well_per=request.args.get('social_well_per', '')
    curiosity_per=request.args.get('curiosity_per', '')
    name = request.args.get('name', '')  
    age = request.args.get('age', '')  
    return render_template('result.html', emp_per=emp_per,deci_per=deci_per,social_incli=social_incli,social_well_per=social_well_per,curiosity_per=curiosity_per,name=name,age=age)



if __name__ == '__main__':
    app.run(debug=True)

