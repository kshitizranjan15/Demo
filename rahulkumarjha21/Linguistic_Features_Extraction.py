import spacy

nlp=spacy.load('en_core_web_sm')

# Tokenization- It is the task of splitting a text into meaningful segments, called tokens.The input to the tokenizer is a unicode text, and the output is a Doc object.
doc1=nlp(u'Apple is looking at buying U.K. startup for $1 billion.')
for token in doc1:
    print(token.text)
doc2=nlp(u"Apple isn't looking at buying U.K. startup for $1 billion.")
for token in doc2:
    print(token.text)   
    
# Tagger
# Parts Of Speech Tagging
for token in doc2:
    print(f'{token.text:{15}} {token.pos_:{15}}')
# Lemmatization
for token in doc2:
    print(f'{token.text:{15}} {token.lemma_:{15}}')
# Stop Word
for token in doc2:
    print(f'{token.text:{15}} {token.is_stop}')

# Parser
# Syntatic Dependency Parsing
for chunk in doc2.noun_chunks:
    print(f'{chunk.text:{15}} {chunk.root.text:{15}} {chunk.root.dep_}')
    
# NER
# Name Entity Recognization
for ent in doc2.ents:
    print(f'{ent.text:{15}} {ent.label_}')
    
# Sentence Segmentation
doc3=nlp(u'Where you have been Harry? I have been waiting for you since last 1 hour in Diagon Alley. Ooh No! Harry')
for sent in doc3.sents:
    print(sent.text)
doc4=nlp(u'Kapil Dev won... Mahendra Singh Dhoni is the only... And Virat Kolhi hasn\'t...')
for sent in doc4.sents:
    print(sent.text)
doc5=nlp(u'Rahul Kumar Jha # 1941012186 # C.S.E. # C')
for sent in doc5.sents:
    print(sent.text)
# Add Custome Rule For Sentence Segmentation
from spacy.language import Language
@Language.component('custome_segmentationRule')
def custome_segentationRule(doc5):
    for token in doc5[:-1]:
        if(token.text=='#'):
            doc5[token.i+1].is_sent_start=True
    return(doc5)
nlp.add_pipe('custome_segmentationRule',before='parser')
doc5=nlp(u'Rahul Kumar Jha # 1941012186 # C.S.E. # C')
for sent in doc5.sents:
    print(sent.text)    
print(nlp.pipe_names)
# Remove Custome Rule For Sentence Segmentation
nlp.remove_pipe('custome_segmentationRule')
print(nlp.pipe_names)

# Visualization
from spacy import displacy
#displacy.serve(doc5,style='dep')
displacy.serve(doc1,style='ent')
