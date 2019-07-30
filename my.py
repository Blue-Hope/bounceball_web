from flask import Flask, render_template, request
score=dict()
app = Flask(__name__)
@app.route("/", methods=['POST','GET'])
def hello():
  if request.method=='POST':
    score_tmp = request.form['score']
    user_tmp = request.form['user']
    score[user_tmp] = score_tmp
    return ""
  else:
    return render_template('my.html', scores=sorted(score.items(), reverse = True)) 

if __name__=="__main__":
  app.run(host='0.0.0.0')
