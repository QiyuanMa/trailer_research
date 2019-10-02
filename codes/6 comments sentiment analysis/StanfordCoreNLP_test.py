from pycorenlp import StanfordCoreNLP
#8080
nlp_wrapper = StanfordCoreNLP('http://localhost:9000')

doc = "I like this chocolate. This chocolate is not good. The chocolate is delicious. Its a very tasty chocolate. This is so bad"
annot_doc = nlp_wrapper.annotate(doc,
    properties={
       'annotators': 'sentiment',
       'outputFormat': 'json',
       'timeout': 1000,
    })

for sentence in annot_doc["sentences"]:
    print ( " ".join([word["word"] for word in sentence["tokens"]]) + " => " \
        + str(sentence["sentimentValue"]) + " = "+ sentence["sentiment"])

