from cltk.tag.pos import POSTag

aen = """arma virumque cano, Troiae qui primus ab oris
Italiam, fato profugus, Laviniaque venit
litora, multum ille et terris iactatus et alto
vi superum saevae memorem Iunonis ob iram;
multa quoque et bello passus, dum conderet urbem,               5
inferretque deos Latio, genus unde Latinum,
Albanique patres, atque altae moenia Romae."""

#remove line breaks
aen = aen.replace('\n', ' ')

tagger = POSTag('latin')
aen_tagged = tagger.tag_ngram_123_backoff(aen)
print(aen_tagged)

cae_tagged = tagger.tag_crf('Gallia est omnis divisa in partes tres')
print(cae_tagged)