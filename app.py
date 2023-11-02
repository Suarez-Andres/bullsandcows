import random
from cs50 import SQL
from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key='final_proyect'

db = SQL("sqlite:///numbers.db")

def numero():
    l=[]
    while len(l)<4:
        n=str(random.randrange(0,10))
        if n not in l:
            l.append(n)
        else:
            continue
    return tuple(l)

@app.route("/", methods=["GET", "POST"])
def index():
    global pc_num
    pc_num=numero()
    db.execute("DELETE FROM tries")
    db.execute("DELETE FROM SQLITE_SEQUENCE WHERE name='tries'")
    if request.method == "post":
        return redirect("/play")
    return render_template("index.html")

@app.route("/play", methods=["GET", "POST"])
def play():
    b=0 #fija
    c=0 #pica
    if request.method == "POST":
        user_num=request.form.get("num","1234")
        if not user_num or not user_num.isdigit() or len(user_num) != 4 or len(set(user_num)) < 4:
            flash(f"You are not following the rules! the number is wrong!")
            return redirect("/play")
        else:
            if len(set(pc_num)&set(user_num))>0:
                c=len(set(pc_num)&set(user_num))
                for i in range(len(pc_num)):
                    if pc_num[i]==user_num[i]:
                        b+=1
                        c-=1
                db.execute("INSERT INTO tries(number, bulls, cows) VALUES(?, ?, ?)", user_num, b, c)
                tries=db.execute("SELECT * FROM tries WHERE try > 1 ORDER BY try DESC")
                if b==4:
                    db.execute("DELETE FROM tries")
                    db.execute("DELETE FROM SQLITE_SEQUENCE WHERE name='tries'")
                    flash(f"You won!")
                    return redirect("/play")
            return render_template("game.html",tries=tries, bulls=b, cows=c, pn=pc_num)

    else:
        tries=db.execute("SELECT * FROM tries WHERE try > 1 ORDER BY try DESC")
        return render_template("game.html",tries=tries, bulls=b, cows=c, pn=pc_num)
