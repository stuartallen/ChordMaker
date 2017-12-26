from flask import Flask, render_template, request
from Chord import chord, findkey

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def hello():
    note_name = request.args.get('note_name', 'C')
    scale_name = request.args.get('scale_name', 'major')
    chord_name = request.args.get('chord_name', 'triad')
    result = chord(findkey(note_name, scale_name), chord_name)
    return render_template("index.html", 
                           note_name=note_name, 
                           scale_name=scale_name, 
                           chord_name=chord_name,
                           result=result)

if __name__ == "__main__":
    # running locally only
    #app.run(host='127.0.0.1',port=8000,debug=True)
    # running locally with LAN access
    app.run(host='0.0.0.0',port=8000,debug=True)