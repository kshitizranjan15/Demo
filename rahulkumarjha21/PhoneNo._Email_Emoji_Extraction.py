import spacy
from spacy.matcher import Matcher
nlp=spacy.load('en_core_web_sm')

# Text Extraction Using Linguistic Autonomation
matcher=Matcher(nlp.vocab)

found_matches=[]

pattern=[{'LOWER':'facebook'},{'LEMMA':'be'},{'POS':'ADV','OP':'*'},{'POS':'ADJ'}]
matcher.add('facebook',[pattern])
doc=nlp(u'Facebook is pretty cool. Although facebook was very ugly in the past')
for token in doc:
    print(token,token.pos_)
found_matches.append(matcher(doc))
print(found_matches)
for f_matches in found_matches:
    for match_id,start,end in f_matches:
        string_id=nlp.vocab.strings[match_id]
        span=doc[start:end]
        print(match_id,string_id,start,end,span)
        
# Phone Number Extraction
# 9572780375 +919572780375 0657-3293500
matcher=Matcher(nlp.vocab)
found_matches=[]
pattern1=[{"ORTH":"+"},{'SHAPE':'dd'},{'SHAPE':'dddd','LENGTH':10}]
pattern2=[{'SHAPE':'dddd','LENGTH':10}]
pattern3=[{'SHAPE':'dddd'},{'ORTH':'-'},{'SHAPE':'dddd','LENGTH':7}]
pattern4=[{'ORTH':'('},{'SHAPE':'ddd'},{'ORTH':')'},{'SHAPE':'dddd','LENGTH':4},{'ORTH':'-','OP':'?'},{'SHAPE':'dddd','LENGTH':4}]
matcher.add('phone',[pattern1,pattern2,pattern3,pattern4])
doc=nlp(u'Phone Number 1: 9572780375, Phone Number2: + 91 9572780375, Phone Number3: 0657-3293500, Phone Number 4: (123) 4567 8900, Phone Number 5: (123) 4567-8900')
for token in doc:
    print(token)
found_matches.append(matcher(doc))
print(found_matches)
for f_matches in found_matches:
    for match_id,start,end in f_matches:
        string_id=nlp.vocab.strings[match_id]
        span=doc[start:end]
        print(match_id,string_id,start,end,span)
        
# Email Extraction
pattern=[{'TEXT':{'REGEX':'[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+'}}]
matcher=Matcher(nlp.vocab)
matcher.add('phone',[pattern])
doc=nlp(u'Rahul Kumar Jha- jharahulkumar02@gmail.com or 1941012186.c.rahulkumarjha@gmail.com')
for token in doc:
    print(token)
found_matches.append(matcher(doc))
print(found_matches)
for f_matches in found_matches:
    for match_id,start,end in f_matches:
        string_id=nlp.vocab.strings[match_id]
        span=doc[start:end]
        print(match_id,string_id,start,end,span)

# EMOJI AND HASHTAG EXTRACTION
matcher = Matcher(nlp.vocab)
pos_emoji = ["😀", "😃", "😂", "🤣", "😊", "😍"]  # Positive emoji
neg_emoji = ["😞", "😠", "😩", "😢", "😭", "😒"]  # Negative emoji
pos_patterns = [[{"ORTH": emoji}] for emoji in pos_emoji]
neg_patterns = [[{"ORTH": emoji}] for emoji in neg_emoji]

def label_sentiment(matcher, doc, i, matches):
    match_id, start, end = matches[i]
    if doc.vocab.strings[match_id] == "HAPPY":  
        doc.sentiment += 0.1  
    elif doc.vocab.strings[match_id] == "SAD":
        doc.sentiment -= 0.1  

matcher.add("HAPPY", pos_patterns, on_match=label_sentiment)  # Add positive pattern
matcher.add("SAD", neg_patterns, on_match=label_sentiment)  # Add negative pattern
matcher.add("HASHTAG", [[{"ORTH": "#"}, {"IS_ASCII": True}]])
doc = nlp("Hello world 😀 #MondayMotivation")

matches = matcher(doc)
for match_id, start, end in matches:
    string_id = doc.vocab.strings[match_id]  # Look up string ID
    span = doc[start:end]
    print(string_id, span.text)
    
# PHRASE MATCHING IN OTHER FILE

# NAME ENTITY RECOGNIZATION IN OTHER FILE