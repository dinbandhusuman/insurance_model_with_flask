from flask import Flask,request,render_template
import pickle

pickle_in = open('insurancemodel.pkl','rb')
pred = pickle.load(pickle_in)


app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('home.html')

@app.route('/result',methods=['POST','GET'])
def insurance_prediction():
    northeast=0
    northwest=0
    southeast=0
    southwest=0
    if request.method =='POST':
        age = int(request.form.get('age'))
        sex=request.form.get('sex')
        if sex=='male':
            sex = 1
        else:
            sex=0
        bmi=float(request.form.get('bmi'))
        children=int(request.form.get('children'))
        smoker=request.form.get('smoker')
        if smoker=='yes':
            smoker=1
        else:
            smoker=0
        region=request.form.get('region')
        if region=='northeast':
            northeast = 1
            northwest = 0
            southeast = 0
            southwest = 0
        elif region=='northwest':
            northeast = 0
            northwest = 1
            southeast = 0
            southwest = 0
        elif region=='southeast':
            northeast = 0
            northwest = 0
            southeast = 1
            southwest = 0
        else:
            northeast = 0
            northwest = 0
            southeast = 0
            southwest = 1

        value = [age,sex,bmi,children,smoker,northeast,northwest,southeast,southwest]

        prediction = pred.predict([[age,sex,bmi,children,smoker,northeast,northwest,southeast,southwest]])

        return render_template('result.html',feature=value,output=prediction,)
if __name__=='__main__':
    app.run(debug=True)