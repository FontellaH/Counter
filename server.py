from flask import Flask , render_template, request, redirect, session

app=Flask(__name__)
app.secret_key='Practice'

@app.route('/')
def count1():
    if 'count' in session:
        session['count'] +=1
    else:
        session['count'] =1
    if 'the_count' not in session:
        session['the_count'] =1
    return render_template("index.html", amount_of_time=session['count'], amount_of_the_count=session['the_count'])


@app.route('/', methods=['POST'])
def count2():
    amount_to_add = request.form['add_num']
    if amount_to_add == "1":
        return redirect('/destroy_session')
    
    elif amount_to_add == "2":
        session['count'] +=2
        session['the_count'] +=1
        return render_template("index.html", amount_of_time=session['count'], amount_of_the_count=session['the_count'])
    
    elif amount_to_add == "3":
        session['count'] +=3
        session['the_count'] +=1
        return render_template("index.html", amount_of_time=session['count'], amount_of_the_count=session['the_count'])
    else:
        session['count'] += int(amount_to_add)
        session['the_count'] +=1
        return render_template("index.html", amount_of_time=session['count'], amount_of_the_count=session['the_count'])
    


if __name__ == '__main__':
   app.run(debug = True)