from flask import Flask,request,jsonify
import csv
from demographic_filtering import output
from content_filtering import getRecommendations
from storage import all_articles,liked_articles,not_liked_articles

app=Flask(__name__)
@app.route('/getArticle')

def getArticle():
    article_data={
        "title":all_articles[0][12],
        "url":all_articles[0][11],
        "lang":all_articles[0][14],
        "total_event":all_articles[0][15]
    }
    return jsonify({'data':article_data,"status":"success"})

@app.route('/likedArticle',methods=["POST"])

def likedArticle():
    article=all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({"status":"success"})

@app.route('/dislikedArticle',methods=["POST"])

def dislikedArticle():
    article=all_articles[0]
    not_liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({"status":"success"})

@app.route("/popularArticles")
def popular_articles():
    article_data=[]
    for article in output:
        _d={
        "title":article[12],
        "url":article[11],
        "lang":article[14],
        "total_event":article[15]
    }
    article_data.append(_d)
    return jsonify({"data":article_data,"status":"success"}),200

@app.route('/recommendedArticles')
def recommended_articles():
    all_recommended=[]
    for liked in liked_articles:
        output=getRecommendations(liked[12])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended=list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    article_data=[]
    for recommended in all_recommended:
        _d={
        "title":recommended[12],
        "url":recommended[11],
        "lang":recommended[14],
        "total_event":recommended[15]
        }
        article_data.append(_d)
    return jsonify({"data":article_data,"status":"success"}),200
if __name__=="__main__":
    app.run()
    