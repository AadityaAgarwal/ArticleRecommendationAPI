from flask import Flask,request,jsonify
import csv
all_articles=[]
liked_articles=[]
disliked_articles=[]


with open ("articles.csv",encoding="utf-8") as f:
    reader=csv.reader(f)
    data=list(reader)
    all_articles=data[1:]

app=Flask(__name__)
@app.route('/getArticle')

def getArticle():
    return jsonify({'data':all_articles[0],"status":"success"})

@app.route('/likedArticle',methods=["POST"])

def likedArticle():
    movie=all_articles[0]
    All_articles=all_articles[1:]
    liked_articles.append(movie)
    all_articles.append(All_articles)
    return jsonify({"status":"success"})

@app.route('/dislikedArticle',methods=["POST"])

def dislikedArticle():
    movie=all_articles[0]
    AllArticlesDisliked=all_articles[1:]
    disliked_articles.append(movie)
    all_articles.append(AllArticlesDisliked)
    return jsonify({"status":"success"})

if __name__=="__main__":
    app.run()
    
