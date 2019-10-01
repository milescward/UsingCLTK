from nltk.tokenize.punkt import PunktLanguageVars
from nltk.util import bigrams
from nltk.util import trigrams
from nltk.util import ngrams

#declaring a sentence and tokenizing it
s = 'Ut primum nocte discussa sol novus diem fecit, et somno simul emersus et lectulo, anxius alioquin et nimis cupidus cognoscendi quae rara miraque sunt, reputansque me media Thessaliae loca tenere qua artis magicae nativa cantamina totius orbis consono orbe celebrentur fabulamque illam optimi comitis Aristomenis de situ civitatis huius exortam, suspensus alioquin et voto simul et studio, curiose singula considerabam. Nec fuit in illa civitate quod aspiciens id esse crederem quod esset, sed omnia prorsus ferali murmure in aliam effigiem translata, ut et lapides quos offenderem de homine duratos et aves quas audirem indidem plumatas et arbores quae pomerium ambirent similiter foliatas et fontanos latices de corporibus humanis fluxos crederem; iam statuas et imagines incessuras, parietes locuturos, boves et id genus pecua dicturas praesagium, de ipso vero caelo et iubaris orbe subito venturum oraculum.'.lower()
p = PunktLanguageVars()
tokens = p.word_tokenize(s)
print(tokens)

#using bigrams(2 words at a time)
b = bigrams(tokens)
print([x for x in b])

#using trigrams (three words at a time)
t = trigrams(tokens)
print([x for x in t])

#using ngrams (n words at a time)
five_gram = ngrams(tokens, 5)
print([x for x in five_gram])



