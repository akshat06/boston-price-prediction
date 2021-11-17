from flask import Flask, request,render_template
from flask_cors import cross_origin
import pickle


app = Flask(__name__)
model = pickle.load(open('boston_model.pkl','rb'))

@app.route("/", methods = ["GET"])
@cross_origin()
def home():
    return render_template("home.html")

@app.route("/predict", methods = ["POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        crim = float(request.form['crim'])
        zn = float(request.form['zn'])
        indus = float(request.form['indus'])
        chas = float(request.form['chas'])
        nox = float(request.form['nox'])
        rm = float(request.form['rm'])
        age = float(request.form['age'])
        dis = float(request.form['dis'])
        rad = float(request.form['rad'])
        tax = float(request.form['tax'])
        ptratio = float(request.form['ptratio'])
        b = float(request.form['b'])
        lstat = float(request.form['lstat'])
        prediction = model.predict([[crim,zn,indus,chas,nox,rm,age,dis,rad,tax,ptratio,b,lstat]])
        print("prediction-->> {}, type-->> {}".format(prediction[0][0], type(prediction[0][0])))
        print(zn, type(zn))
        return render_template("home.html", prediction_text="House Price is: ${:.2f}".format(prediction[0][0]))
        # return render_template("home.html", prediction_text="House Price is: ${:.2f}".format(100.45))


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False,port=8080)