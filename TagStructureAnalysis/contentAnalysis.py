import spacy
from spacy import displacy

def analyse():
    trf = spacy.load('en_core_web_trf')
    file = open("result.txt", "r")

    doc = trf (file.read())

    for ent in doc.ents:
        print(ent.text, ent.label_)
    # displacy.render(doc, style="ent")