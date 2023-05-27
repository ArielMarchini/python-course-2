def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    translated_words = (words[word] for word in sentence.split())
    translated_sentence = ' '.join(translated_words)
    return translated_sentence

