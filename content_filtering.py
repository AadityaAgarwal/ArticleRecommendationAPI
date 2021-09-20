from sklearn.feature_extraction.text import CountVectorizer as cvt
from sklearn.metrics.pairwise import cosine_similarity as cs
import pandas as pd
import numpy as np

df=pd.read_csv('articles.csv')
df=df[df["title"].notna()]

count=cvt(stop_words='english')
count_matrix=count.fit_transform(df["title"])
cosine_sim2=cs(count_matrix,count_matrix)

df1=df.reset_index()
indices=pd.Series(df1.index,index=df["contentId"])

def getRecommendations(title,cosine_sim):
  idx=indices[title]
  sim_scores=list(enumerate(cosine_sim[idx]))
  sim_scores=sorted(sim_scores,key=lambda x:x[1],reverse=True)
  sim_scores=sim_scores[1:11]
  article_indices=[i[0]for i in sim_scores]
  return df["title"].iloc[article_indices]
