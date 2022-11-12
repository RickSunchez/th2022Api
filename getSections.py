import requests
import os
import json
from jsonmerge import merge
from jsoncomparison import Compare, NO_DIFF

sectionTypes = [
    'supplier',
    'general',
    'customer',
    'instruction'
]

# api methods
def questionList(sectionType):
    # &count=0
    return 'https://old.zakupki.mos.ru/api/Cssp/KnowledgeBase/GetQuestionList?sectionType=%s&count=10' % sectionType

def serviceList(sectionType):
    # &count=6
    return 'https://old.zakupki.mos.ru/api/Cssp/KnowledgeBase/GetServicesListSectionType?sectionType=%s&count=10' % sectionType

def getArticleById(id):
    return 'https://old.zakupki.mos.ru/api/Cssp/KnowledgeBase/GetArticleById?id=%d' % id

# helpers
def getSections():
    sections = {}

    for sectionType in sectionTypes:
        path = './data/%s' % sectionType
        sections[sectionType] = {}

        if not os.path.isdir(path):
            os.mkdir(path)

        questionListPath = path + '/questionList.json'
        questionListJson = {}
        if os.path.isfile(questionListPath):
            with open(questionListPath, 'r') as f:
                questionListJson = json.load(f)
        else:
            response = requests.get(questionList(sectionType))
            questionListJson = response.json()

            with open(questionListPath, 'w') as f:
                json.dump(questionListJson, f, ensure_ascii=False)

        serviceListPath = path + '/serviceList.json'
        serviceListJson = {}
        if os.path.isfile(serviceListPath):
            with open(serviceListPath, 'r') as f:
                serviceListJson = json.load(f)
        else:
            response = requests.get(serviceList(sectionType))
            serviceListJson = response.json()

            with open(serviceListPath, 'w') as f:
                json.dump(serviceListJson, f, ensure_ascii=False)

        sections[sectionType]['services'] = serviceListJson
        sections[sectionType]['questions'] = questionListJson
    
    return sections

# def getArticles(sections):
#     for sectionType in sections:
#         print('Section:', sectionType)

#         path = './data/%s' % sectionType
#         articles = {}

#         for type in sections[sectionType]:
#             print('Type:', type)
#             articles[type] = {}

#             if type == 'services':
#                 for article in sections[sectionType][type]:
#                     key = article['key']
#                     articles[type][key] = 

#             l = len(sections[sectionType][type])
#             c = 0

#             for article in sections[sectionType][type]:
#                 print(article)
#                 exit()
#                 c += 1
#                 print('Articles %d/%d' % (c, l))



#                 articleId = article['articleId']
#                 arcticleStaticId = article['articleStaticId']

#                 articleIdResp = requests.get(getArticleById(articleId))
#                 articleIdJson = articleIdResp.json()
                
#                 arcticleStaticIdResp = requests.get(getArticleById(arcticleStaticId))
#                 arcticleStaticIdJson = arcticleStaticIdResp.json()

#                 articles[type].append(articleIdJson)

#             with open(path + ('/articles-%s.json' % type), 'w') as f:
#                 json.dump(articles, f, ensure_ascii=False)
            

sections = getSections()
# getArticles(sections)

        


