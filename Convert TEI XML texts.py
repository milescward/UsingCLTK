from cltk.corpus.utils.importer import CorpusImporter
#todo what the hell is this and why am I doing it
from cltk.corpus.greek.tei import onekgreek_tei_xml_to_text


latin_importer = CorpusImporter('latin')
greek_importer = CorpusImporter('greek')

latin_corpora = latin_importer.list_corpora
greek_corpora = greek_importer.list_corpora

latin_importer.import_corpus('latin_text_perseus')

#todo is this useful at all?
text = onekgreek_tei_xml_to_text()

#todo I dont actually have any local corpora, how do I get some?

latin_importer.import_corpus('phi5', '~/cltk/corpora/PHI5')
print(latin_corpora)
#print(greek_corpora)ls -l ~/cltk_data/greek/text/greek_text_first1kgreek_plaintext/ | wc -l
