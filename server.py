from flask import Flask, request, render_template
from Maths.mathematics import summation, subtraction, multiplication

app = Flask(__name__)

# Ana sayfa (index.html render edilir)
@app.route("/")
def render_index_page():
    return render_template('index.html')


# Toplama işlemi
@app.route("/sum", methods=["GET"])
def sum_numbers():
    num1 = float(request.args.get("num1", 0))
    num2 = float(request.args.get("num2", 0))
    result = summation(num1, num2)
    if result.is_integer():
        result = int(result)
    return str(result)


# Çıkarma işlemi
@app.route("/sub", methods=["GET"])
def sub_numbers():
    num1 = float(request.args.get("num1", 0))
    num2 = float(request.args.get("num2", 0))
    result = subtraction(num1, num2)
    if result.is_integer():
        result = int(result)
    return str(result)


# Çarpma işlemi
@app.route("/mul", methods=["GET"])
def mul_numbers():
    num1 = float(request.args.get("num1", 0))
    num2 = float(request.args.get("num2", 0))
    result = multiplication(num1, num2)
    if result.is_integer():
        result = int(result)
    return str(result)


if __name__ == "__main__":
    app.run(debug=True)
