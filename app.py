from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <h3>Student Grade Calculator</h3>
    <form action="/result">
        <input name="m1" placeholder="Subject 1 marks" required>
        <input name="m2" placeholder="Subject 2 marks" required>
        <input name="m3" placeholder="Subject 3 marks" required>
        <button>Calculate</button>
    </form>
    '''
@app.route("/result")
def result():
    m1 = float(request.args.get("m1"))
    m2 = float(request.args.get("m2"))
    m3 = float(request.args.get("m3"))

    total = m1 + m2 + m3
    avg = total / 3

    grade = "A" if avg >= 80 else "B" if avg >= 60 else "C"

    return f"Total: {total}, Average: {avg}, Grade: {grade}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
