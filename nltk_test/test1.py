# -*- coding: utf-8 -*-

import nltk
# nltk.download()

# # 分句-------------------
# sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
# paragraph = """The first time I heard that song was in Hawaii on radio.
# ... I was just a kid, and loved it very much! What a fantastic song!"""
# sentences = sent_tokenizer.tokenize(paragraph)
# print sentences
# # 分句-------------------
#
# # 分词------------------
# from nltk.tokenize import WordPunctTokenizer
# sentence = """Are you old enough to remember Michael Jackson attending
# ... the Grammys with Brooke Shields and Webster sat on his lap during the show?"""
# words = WordPunctTokenizer().tokenize(sentence)
# print words
# # 分词------------------

text = 'That U.S.A. poster-print costs $12.40... 海岛大亨'
# pattern = r'''''(?x)    # set flag to allow verbose regexps
#     ([A-Z]\.)+        # abbreviations, e.g. U.S.A.
#   | \w+(-\w+)*        # words with optional internal hyphens
#   | \$?\d+(\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
#    | \.\.\.            # ellipsis
#    | [][.,;"'?():-_`]  # these are separate tokens; includes ], [
#  '''
pattern = r"""(?x)                   # set flag to allow verbose regexps
              (?:[A-Z]\.)+           # abbreviations, e.g. U.S.A.
              |\d+(?:\.\d+)?%?       # numbers, incl. currency and percentages
              |\w+(?:[-']\w+)*       # words w/ optional internal hyphens/apostrophe
              |\.\.\.                # ellipsis
              |(?:[.,;"'?():-_`])    # special characters with meanings
            """
listsx = nltk.regexp_tokenize(text, pattern)
for one in listsx:
    print one