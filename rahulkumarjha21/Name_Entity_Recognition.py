import spacy
nlp=spacy.load('en_core_web_sm')

# Name Entity Recognition Function
def view_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            print(ent.text+"-"+ent.label_+"-"+spacy.explain(ent.label_))
    else:
        print('Not Found')

# Document Intilization
doc=nlp(u'Hello World!')
doc2=nlp(u'New Zealand won the World Test Championship 2021. Vivo Brand!')

# Method Call
view_ents(doc)
view_ents(doc2)

# Add Own NER Single Value At A Time
# import span from spacy tokens
# NER to be added as a token
doc=nlp(u'Vivo, New Zealand won the World Test Championship 2021. By Vivo!')
from spacy.tokens import Span
# Call ORG Entity From Vocabulary
ORG=doc.vocab.strings[u'ORG']
# Entity Number
print(ORG)
# Add NER inside Span
new_ent=Span(doc,0,1,label=ORG)
# Append new_ents In doc.ents (New)
doc.ents=list(doc.ents)+[new_ent]
# Method Call
view_ents(doc)

# Add Own NER Multiple Value At A Time
from spacy.matcher import PhraseMatcher
# Create Object Of Phrase Matcher Class With Nlp Vocabulary As Object
matcher=PhraseMatcher(nlp.vocab)
# Define the Phrase List
phrase_list=['rahul kumar', 'rahul-kumar','jha']
# Define The Pattern with the Phrase List
pattern=[nlp(text) for text in phrase_list]
# Adde Pattern To matcher Phrase matcher class using matcher method
matcher.add('rahul',pattern)
# Document Intialization
doc1=nlp(u'my name is rahul kumar jha. rahul-kumar-jha')
# Check For Phrase Matching
found_matches=matcher(doc1)
# Entity Number
print(found_matches)
# Call ORG Entity From Vocabulary
PROD=doc1.vocab.strings[u'PRODUCT']
# Add NER inside Span
new_ents=[Span(doc1,match[1],match[2],label=PROD) for match in found_matches]
# Append new_ents In doc.ents (New)
doc1.ents=list(doc1.ents)+new_ents
print(doc1.ents)
# Method Call
view_ents(doc1)

# To get A Specific Label Entity
doc=nlp(u'I won the price of $100 which is equivalient to 100 dollars')
for entity in doc.ents:
    if(entity.label_=="MONEY"):
        print(entity.text+"-"+entity.label_+"-"+spacy.explain(entity.label_))
        
# Length Of Specific Entity List
print(len([ent for ent in doc.ents if ent.label_=='MONEY']))