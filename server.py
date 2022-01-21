from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    data = { 
        "frutas" : {
            "Strawberry" : request.form["strawberry"],
            "Raspberry" : request.form["raspberry"],
            "Apple" : request.form["apple"]
        },
        "info_user" : {
            "first_name" : request.form["first_name"],
            "last_name" : request.form["last_name"],
            "student_id" : request.form["student_id"]
        }
    }
    print(len(data["frutas"]))
    return render_template("checkout.html",data=data)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    