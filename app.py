from typing import Union
from fastapi import FastAPI, Query
import json

app = FastAPI()

sections = [
    'supplier',
    'general',
    'customer',
    'instruction'
]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/sections/")
def getSections():
    return sections

@app.get("/GetQuestionList/")
def GetQuestionList(sectionType: str = Query(default="supplier"), count: Union[int, None] = None):
    if sectionType not in sections:
        return False

    path = './data/%s/questionList.json' % sectionType

    with open(path, 'r') as f:
        data = json.load(f)
    
    if count is None: count = len(data)
    return data[:min(len(data), count)]

@app.get("/GetServicesListSectionType/")
def GetServicesListSectionType(sectionType: str = Query(default="supplier"), count: Union[int, None] = None):
    if sectionType not in sections:
        return False

    path = './data/%s/serviceList.json' % sectionType

    with open(path, 'r') as f:
        data = json.load(f)
    
    if count is None: count = len(data)
    return data[:min(len(data), count)]

@app.get("/GetArticleById/")
def GetArticleById(id: int):
    articles = getArticles()

    for article in articles:
        if article['articleId'] == id:
            return article

    return False

# helpers

def getArticles():
    articleList = []

    for section in sections:
        qPath = './data/%s/questionList.json' % section
        sPath = './data/%s/serviceList.json' % section

        with open(qPath, 'r') as f:
            articleList += json.load(f)

        with open(sPath, 'r') as f:
            data = json.load(f)

            for d in data:
                articleList += d['articleList']

    return articleList