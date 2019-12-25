import nltk
from nltk import *
from nltk.corpus import stopwords
#nltk.download()
from ApiProje.models import Ozet
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize


def create_frequency_table(text_string) -> dict:
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text_string)
    ps = PorterStemmer()
    lst = []
    freqTable = dict()
    for kelime in words:
        kelime = ps.stem(kelime)
        if kelime in stopWords:
            continue
        if kelime in freqTable:
            freqTable[kelime] += 1
        else:
            freqTable[kelime]  = 1
    for i in freqTable:
        lst.append(Ozet(1, i, freqTable[i]))
    return freqTable #lst

def _score_sentences(sentences, freqTable) -> dict:
    sentenceValue = dict()

    for sentence in sentences:
        word_count_in_sentence = (len(word_tokenize(sentence)))
        for wordValue in freqTable:
            if wordValue in sentence.lower():
                if sentence[:10] in sentenceValue:
                    sentenceValue[sentence[:10]] += freqTable[wordValue]
                else:
                    sentenceValue[sentence[:10]] = freqTable[wordValue]

        sentenceValue[sentence[:10]] = sentenceValue[sentence[:10]] // word_count_in_sentence

    return sentenceValue

def _find_average_score(sentenceValue) -> int:
    sumValues = 0
    for entry in sentenceValue:
        sumValues += sentenceValue[entry]
    # Average value of a sentence from original text
    average = int(sumValues / len(sentenceValue))
    return average

def _generate_summary(sentences, sentenceValue, threshold):
    sentence_count = 0
    summary = ''
    for sentence in sentences:
        if sentence[:10] in sentenceValue and sentenceValue[sentence[:10]] > (threshold):
            summary += " " + sentence
            sentence_count += 1
    return summary

def GetByOzet(cumle):
    ozet = create_frequency_table(cumle)
    sentences = sent_tokenize(cumle)
    sentence_scores = _score_sentences(sentences, ozet)
    threshold = _find_average_score(sentence_scores)
    summary = _generate_summary(sentences, sentence_scores, 1.5 * threshold)
    return summary