from flask import Flask, request

app= Flask(__name__)
# no methods is spectified, by default it takes get
@app.route("/testfun")

def test():
    get_name = request.args.get("get_name")
    mobile_no= request.args.get("mobile_no")
    mail_id  =request.args.get("mail_id")
    return "this is my first function for get {}{}{}".format(get_name,mobile_no, mail_id)

if __name__=="__main__":
    app.run(port=5001)