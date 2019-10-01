from cltk.corpus.utils.importer import CorpusImporter
from cltk.stem.latin.j_v import JVReplacer
from cltk.tokenize.word import WordTokenizer
from cltk.stem.lemma import LemmaReplacer


cato_agri_praef = "Est interdum praestare mercaturis rem quaerere, nisi tam periculosum sit, et item foenerari, si tam honestum. Maiores nostri sic habuerunt et ita in legibus posiverunt: furem dupli condemnari, foeneratorem quadrupli. Quanto peiorem civem existimarint foeneratorem quam furem, hinc licet existimare. Et virum bonum quom laudabant, ita laudabant: bonum agricolam bonumque colonum; amplissime laudari existimabatur qui ita laudabatur. Mercatorem autem strenuum studiosumque rei quaerendae existimo, verum, ut supra dixi, periculosum et calamitosum. At ex agricolis et viri fortissimi et milites strenuissimi gignuntur, maximeque pius quaestus stabilissimusque consequitur minimeque invidiosus, minimeque male cogitantes sunt qui in eo studio occupati sunt. Nunc, ut ad rem redeam, quod promisi institutum principium hoc erit."

latin_importer = CorpusImporter('latin')
latin_importer.import_corpus('latin_models_cltk')
latin_importer.import_corpus('latin_text_latin_library')
#latin_corpora = latin_importer.list_corpora


jv_replacer = JVReplacer()
cato_agri_praef = jv_replacer.replace(cato_agri_praef.lower())

word_tokenizer = WordTokenizer('latin')
cato_word_tokens = word_tokenizer.tokenize(cato_agri_praef.lower())
cato_word_tokens = [token for token in cato_word_tokens if token not in [',', '.', ':', ';']]

lemmatizer = LemmaReplacer('latin')
lemmata = lemmatizer.lemmatize(cato_word_tokens)
print(lemmata)

#lemmatize and check vs original form for accuracy

lemmata_orig = lemmatizer.lemmatize(cato_word_tokens, return_raw=True)
print(lemmata_orig)

#count all the words
print(len(lemmata))

#count unique words
print(len(set(lemmata)))

#measure lexical diversity

lexical_diversity = len(set(lemmata)) / len(lemmata)
print("The lexical diversity is:", lexical_diversity)