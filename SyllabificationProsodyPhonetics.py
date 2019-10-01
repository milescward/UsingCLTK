from cltk.stem.latin.syllabifier import Syllabifier
from cltk.tokenize.word import WordTokenizer

cato_agri_praef = "Est interdum praestare mercaturis rem quaerere, nisi tam periculosum sit, et item foenerari, si tam honestum. Maiores nostri sic habuerunt et ita in legibus posiverunt: furem dupli condemnari, foeneratorem quadrupli. Quanto peiorem civem existimarint foeneratorem quam furem, hinc licet existimare. Et virum bonum quom laudabant, ita laudabant: bonum agricolam bonumque colonum; amplissime laudari existimabatur qui ita laudabatur. Mercatorem autem strenuum studiosumque rei quaerendae existimo, verum, ut supra dixi, periculosum et calamitosum. At ex agricolis et viri fortissimi et milites strenuissimi gignuntur, maximeque pius quaestus stabilissimusque consequitur minimeque invidiosus, minimeque male cogitantes sunt qui in eo studio occupati sunt. Nunc, ut ad rem redeam, quod promisi institutum principium hoc erit."
word_tokenizer = WordTokenizer('latin')
cato_word_tokens = word_tokenizer.tokenize(cato_agri_praef)
cato_word_tokens_no_punt = [token for token in cato_word_tokens if token not in ['.', ',', ':', ';']]

#print(cato_word_tokens_no_punt)

syllabifier = Syllabifier()

#for word in cato_word_tokens_no_punt:
    #syllables = syllabifier.syllabify(word)
    #print(word, syllables)

############################################################

#use the macronizer
from cltk.prosody.latin.macronizer import Macronizer

macronizer = Macronizer('tag_ngram_123_backoff')

text = 'Quo usque tandem, O Catilina, abutere nostra patientia?'

prose_text = macronizer.macronize_text(text)
print(prose_text)