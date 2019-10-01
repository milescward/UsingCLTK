#This is the import of the right part of the CLTK library

from cltk.corpus.utils.importer import CorpusImporter

#you use the corpus importer class to import corpora into your
#program
# See https://github.com/cltk for all official corpora

my_latin_downloader = CorpusImporter('latin')

# Use this variable to see what corpora are available

latin_corpora = my_latin_downloader.list_corpora
print(latin_corpora)

# Import several corpora

my_latin_downloader.import_corpus('latin_text_latin_library')
my_latin_downloader.import_corpus('latin_models_cltk')
my_latin_downloader.import_corpus('latin_text_poeti_ditalia')

#import some greek corpora too

my_greek_downloader = CorpusImporter('greek')
greek_corpora = my_greek_downloader.list_corpora
greek_corpora = my_greek_downloader.list_corpora
my_greek_downloader.import_corpus('greek_models_cltk')

my_greek_downloader.import_corpus('greek_text_lacus_curtius')

my_greek_downloader.import_corpus('greek_text_first1kgreek')

#todo look up course on using the terminal window in pyCharm
print(greek_corpora)


