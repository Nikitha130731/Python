from flask import Flask , request ,jsonify
#get--> posting a data through URL
#post--> posting a data through body
app = Flask(__name__)
@app.route('/abc/test1', methods=['GET','POST']) 
def test1():
    if(request.method=='POST'):
        a=request.json['num1']
        b=request.json['num2']
        result = a+b
        return jsonify(str(result))
    

@app.route('/abc1/test2',methods=['GET','POST'])
def test2():
    if(request.method=='POST'):
        a=request.json['num1']
        b=request.json['num2']
        result = a*b
        return jsonify(str(result))

@app.route('/abc1/test3',methods=['GET','POST'])
def test3():
    if(request.method=='POST'):
        a=request.json['num1']
        b=request.json['num2']
        result = a-b
        return jsonify(str(result))
    
@app.route('/abc1/test4',methods=['GET','POST'])
def test4():
    if(request.method=='POST'):
        a=request.json['num1']
        b=request.json['num2']
        result = a**b
        return jsonify(str(result))
    
@app.route('/abc1/test5',methods=['GET','POST'])
def test5():
    if(request.method=='POST'):
        a=request.json['num1']
        b=request.json['num2']
        result = a/b
        return jsonify(str(result))
    
if  __name__=='__main__':
    app.run()

# def test(a,b):
#     return a+b


# print(test(4,5))