from flask import Flask,jsonify,request
import csv

allArticles = []
likedArticles = []
notLikedArticles = []
DidNotWatchArticles = []
with open('articles.csv',encoding = 'utf8') as f:
    reader = csv.reader(f)
    data = list(reader)
    allArticles = data[1:]

app = Flask(__name__)
@app.route('/getArticles')
def getArticles():
    return jsonify({
        'data' : allArticles[0],
        'message' : 'success'
    })

@app.route('/likedArticles',methods = ['POST'])    
def likedArticles():
    article = allArticles[0],
    allArticles = allArticles[1:],
    likedArticles.append(article)
    return jsonify ({
        'status' : 'success'
    })

@app.route('/notlikedArticles',methods = ['POST'])    
def notLikedArticles():
    article = allArticles[0],
    allArticles = allArticles[1:],
    notLikedArticles.append(article)
    return jsonify ({
        'status' : 'success'
    })

@app.route('/didNotWatchedArticles',methods = ['POST'])    
def didNotReadArticles():
    article = allArticles[0],
    allArticles = allArticles[1:],
    didNotReadArticles.append(article)
    return jsonify ({
        'status' : 'success'
    })

if __name__ == '__main__':
    app.run() 