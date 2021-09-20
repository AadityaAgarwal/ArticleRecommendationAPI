import pandas as pd
import numpy as np

df=pd.read_csv("articles.csv")
df=df.sort_values("total_event",ascending=True)
output=df[["index","timestamp","eventType","contentId","authorPersonId","authorSessionId","authorUserAgent","authorRegion","authorCountry","contentType","url"	,"title","text","lang","total_event"]].head(20).values.tolist()