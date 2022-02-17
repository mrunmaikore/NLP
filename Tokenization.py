import nltk
nltk.download('all')
from nltk.tokenize import sent_tokenize, word_tokenize
text="Global warming has become an undisputed fact about our current livelihoods; our planet is warming up "+\
      "and we are definitely part of the problem. However, this isn’t the only environmental problem that we should"+\
      "be concerned about. All across the world, people are facing a wealth of new and challenging environmental problems "+\
      "every day. Some of them are small and only affect a few ecosystems, but others are drastically changing the landscape "+\
      "of what we already know."
print(sent_tokenize(text))
print(word_tokenize(text))
