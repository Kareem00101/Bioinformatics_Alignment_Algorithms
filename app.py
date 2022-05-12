from flask import Flask, render_template, redirect, request
from flask_cors import CORS
# import bio algorithms here


app = Flask(__name__)
CORS(app)

@app.route("/")
def setup_get():
    
    return render_template('home.html')

@app.route("/", methods=['Post'])
def setup_post():

    global s1
    s1=request.form.get('s1')
    global s2
    s2=request.form.get('s2')
    global match
    match=request.form.get('match')
    global mismatch
    mismatch=request.form.get('mismatch')
    global gap
    gap=request.form.get('gap')
    global algoType
    algoType=request.form.get('algoType')

    # check algo then call algo func here 
    global l1
    l1=[[0,0,0,0,0,0,0,0,0],
        [0,5,0,0,5,0,0,5,0],
        [0,5,3,0,5,3,0,5,3],
        [0,0,3,8,2,10,4,0,3],
        [0,0,0,2,6,4,8,2,5],
        [0,5,0,0,7,4,2,13,7],
        [0,0,3,0,1,5,2,7,18]]

    print(algoType,gap,mismatch,match,s2,s1)

    return redirect('/algo')

@app.route("/algo" )
def algo_get():

    return render_template('home.html',s1=s1, s2=s2, match=match, mismatch=mismatch, gap=gap, algoType=algoType,l1=l1)

     

    
if __name__=='__main__':
    app.run(debug=True,port=5000)