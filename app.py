from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
<title>Smart AI Farm</title>
<style>
body{
font-family: Arial;
background:#f5f5f5;
text-align:center;
padding:40px;
}

.card{
background:white;
padding:30px;
border-radius:12px;
box-shadow:0 0 10px rgba(0,0,0,0.1);
display:inline-block;
}

button{
background:#2e7d32;
color:white;
border:none;
padding:12px 20px;
border-radius:8px;
font-size:16px;
cursor:pointer;
}

button:hover{
background:#1b5e20;
}
</style>
</head>

<body>

<div class="card">

<h1>🌱 Smart AI Farm</h1>

<p>AI based agriculture assistant</p>

<button onclick="checkAPI()">Check API</button>

<p id="result"></p>

</div>

<script>

function checkAPI(){

fetch('/api')

.then(res=>res.json())

.then(data=>{

document.getElementById("result").innerHTML =
data.message;

})

}

</script>

</body>

</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML_PAGE)


@app.route("/api")
def api():
    return jsonify({
        "status": "running",
        "message": "AI Farm API working 🚀"
    })


if __name__ == "__main__":
    app.run()
