from flask import Flask, render_template, request, Response   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/webhook', methods=['POST'])
def respond():
    print(request.json);
    return Response(status=200)
    

    
if __name__ == "__main__":
    app.run(debug=True)
