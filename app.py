from ctypes import alignment
from sys import flags
from flask import Flask, render_template, redirect, request
from flask_cors import CORS
from main import needleman_wunsch, needleman_wunsch_list_of_trace_back_strings, smith_waterman, smith_waterman_list_of_trace_back_strings
from AGP import global_alignment_with_affine_gap, affine_gap_list_of_trace_back_strings


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
    global open
    open = request.form.get('open')
    global extention
    extention = request.form.get('extention')

    # check algo then call algo func here 
    # global l1
    # l1=[[0,0,0,0,0,0,0,0,0],
    #     [0,5,0,0,5,0,0,5,0],
    #     [0,5,3,0,5,3,0,5,3],
    #     [0,0,3,8,2,10,4,0,3],
    #     [0,0,0,2,6,4,8,2,5],
    #     [0,5,0,0,7,4,2,13,7]]

    global outputMatrix,outputIndices
    outputMatrix=outputIndices=[]
    global xx
    xx=[]
    tracebackString=''
    global flag
    flag = bool
    

    if algoType == "NW":
        outputMatrix, outputIndices=needleman_wunsch(s2,s1,match,mismatch,gap)
        tracebackString=needleman_wunsch_list_of_trace_back_strings
        outputMatrix=outputMatrix.tolist()
        outputIndices=outputIndices.tolist()
        print(type(outputIndices),type(outputMatrix))
        print(outputMatrix,outputIndices)
        flag= False

    elif algoType== "SW":
        outputMatrix, outputIndices=smith_waterman(s2,s1,match,mismatch,gap)
        outputMatrix=outputMatrix.tolist()
        outputIndices=outputIndices.tolist()
        tracebackString=smith_waterman_list_of_trace_back_strings
        print(type(outputIndices),type(outputMatrix))
        print(outputMatrix,outputIndices,tracebackString)
        flag= False
    
    elif algoType== "AGP":
        global outputMatrixM,outputMatrixX,outputMatrixY
        outputMatrixM,outputMatrixX,outputMatrixY,outputIndices= global_alignment_with_affine_gap(s2,s1,int(match),int(mismatch),int(open),int(extention))
        tracebackString=affine_gap_list_of_trace_back_strings

        global mainM
        mainM=[]
        flag=True

        # print(len(outputMatrixM),len(outputMatrixM[0]))

        for i in range(0,int(len(outputMatrixM))):

            for a in range(0,int(len(outputMatrixM[0]))):
                ltest=[]

                ltest.append(outputMatrixM[i][a] if outputMatrixM[i][a] > -999 else '-∞')
                ltest.append(outputMatrixX[i][a] if outputMatrixX[i][a] > -999 else '-∞')
                ltest.append(outputMatrixY[i][a] if outputMatrixY[i][a] > -999 else '-∞')
                mainM.append(ltest)

            outputMatrix.append(mainM)
            mainM=[]

    # print('this is test: ', outputMatrixM,outputMatrixX,outputMatrixY,outputMatrix,outputMatrix)


    for i in range(0,int(len(tracebackString)),2):
        ltest=[]
        for a in range(0,2):
            ltest.append(tracebackString[a+i])
            if a%2 !=0:
                break

        xx.append(ltest)

    
    print(outputMatrix,outputIndices,tracebackString )
    # print(algoType,gap,mismatch,match,s2,s1,outputMatrix,xx )

    return redirect('/algo')

@app.route("/algo" )
def algo_get():

    # row and coloumn which is larger

    return render_template('home.html',s1=s1, s2=s2, match=match, mismatch=mismatch, gap=gap, algoType=algoType,\
                            l1=outputMatrix, i1=outputIndices,alignment=xx,flag=flag)

    
if __name__=='__main__':
    app.run(debug=True,port=5000)