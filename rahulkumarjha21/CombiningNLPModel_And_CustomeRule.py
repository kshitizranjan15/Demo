import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens.span import Span

nlp=spacy.load('en_core_web_sm')

doc1=nlp(u'Mr. Dhoni is from Ranchi. Mr Singh is from Punjab. Mrs Singh is from Punjab. Mrs. Singh is from Punjab. Dr Singh is from Punjab. Dr. Singh is from Punjab')

for entity in doc1.ents:
    print(entity.text,entity.label_,spacy.explain(entity.label_))
print(doc1.ents)
# Add Custome Name Entity Recognization
news_ents=[]
for ent in doc1.ents:
    if(ent.label_=='PERSON' and ent.start!=0):
        prev_token=doc1[ent.start-1]
        print('Check:',prev_token.text)
        if prev_token.text in ('Dr.','Mr.','Mrs.'):
            new_ent=Span(doc1,ent.start-1,ent.end,label=ent.label_)
            print('Check:',new_ent)
            news_ents.append(new_ent)
            print('Check:',news_ents)
doc1.ents=list(doc1.ents)+news_ents
print(doc1.ents)

print('NEW')

doc1=nlp(u'Mr. Dhoni is from Ranchi. Mr Singh is from Punjab. Mrs Singh is from Punjab. Mrs. Singh is from Punjab. Dr Singh is from Punjab. Dr. Singh is from Punjab')
for entity in doc1.ents:
    print(entity.text,entity.label_,spacy.explain(entity.label_))