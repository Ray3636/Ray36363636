from flask import Flask #flask是工具箱(module模組),Flask是工具(class類別)
from flask import abort, redirect, url_for,render_template

app = Flask(__name__) #製作出一個由Flask類別生成的物件(object)

@app.route("/") #裝飾器 :根目錄要做啥事
@app.route("/<string:username>") 
def say_hello_world(username=""):
    return render_template("hello.html", name=username)

@app.route("/tell_me_a_joke") 
def tell_me_a_joke():
    return "<p>Ha ha ha ha!!</p>"


@app.route("/eat/<string:what_fruit>")
def eat_fruit(what_fruit):
    return redirect(url_for('say_apple_is_gone', fruit=what_fruit)) #url_for(route_function_name)

@app.route("/eat_<string:fruit>")
def say_apple_is_gone(fruit):
    return "<p>"+ fruit + " is gone.</p>" 




#@app.route('/')
#def index():
    return redirect(url_for('login'))

#@app.route('/login')
#def login():
    abort(401)
    this_is_never_executed()

#在command_line 下:flask --app flask_linebot.py run ---盡量不要取同名
#在command_line 下:flask --app (你的檔名).py run
#if __name__=='__main__':  #如果我直接執行這個檔案,那__name__就等於__main__
    app.run(debug=True)             #或在command_line 下:flask --app flask_linebot.py --debug run
 