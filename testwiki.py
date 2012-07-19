import bsddb
from gensim.corpora.wikicorpus import remove_markup
from textonly import text_only

db = bsddb.hashopen("../semanticizer-lm-reranking/wikipedia.db", "r")

bunch = [db.next() for _ in xrange(100)]

for _, text in bunch:
    print(remove_markup(text.decode("utf-8")).encode("utf-8"))
    #print(text_only(text))
