# Name: Hezheng Fan
# Unique Name: hzfan

import sys
import os
import re
from PorterStemmer import PorterStemmer
import collections

def removeSGML(text):
    """
    Name: removeSGML;
    Input: string;
    Output: string
    :param text:
    :return: result
    Match anything from '<' to '>' and remove
    """
    result = None
    match = re.compile("<.*?>") # remove SGML by matching this pattern
    result = re.sub(match, '', text)
    return result

def tokenizeText(text):
    """
    Name: tokenizeText;
    input: string;
    output: list (of tokens)
    :param text:
    :return: token_list
    Tokenize text.
    """
    # if re is too complicated to write, use for loop"
    token_list = []

    # handle '.'  ',' '?' '!'
    PUNCTUATION = [
        # tokenize '.'
        # in all texts, when '.' represents the end of a sentence, it's split by spaces
        # all other cases do not, thus str.split() can do a proper job split '.'
        (re.compile(r'([^\.])(\.)([\]\)}>"\']*)\s*$'), r"\1 \2\3 "),  # handle '.' at the end of a text
        (re.compile(r'([A-Z]\.*[A-Z]\.*.*?)(\s)s?'), r'<\1> '),  # to handle '.' in abbrev&acronyms, first detect and set '<>' as bound
        (re.compile(r'(\.\s)'), r" \1"),  #seperate all '. '
        (re.compile(r'(\<)([A-Z]\.*[A-Z]\.*.*?)(\>)s?'), r'\2'),  # remove bound of abbrev&acronyms


        # tokenize ','
        (re.compile(r"([:,])([^\d])"), r" \1 \2"),  # ',' at any other places except in a number
        (re.compile(r"([:,])$"), r" \1 "),  # ',' at the end of the line

        # tokenize '?' and '!
        (re.compile(r"[?!]"), r" \g<0> "),

        # tokenize '(' and ')'
        (re.compile(r"[()]"), r" \g<0> "),
    ]

    # handle '-'
    DASH = [
        (re.compile(r"(\-)\n"), r""),  # '-' at the end of the line
        # if dash is not at the end of the line, no need to worry since no space between such word
        # i.e. 'state-of-the-art'
    ]

    # handle '/'
    DATES = [
        (re.compile(r'([^\d])(\/)([^\d])'), r'\1 \3'),  # remove all '/' unless it's used in a date
    ]

    # handle ' ' '
    # contraction expansion dict
    EXPANSION_DICT = {
        "i\'ll": "i will",
        "he\'ll": "he will",
        "she\'ll": "she will",
        "it\'ll": "it will",
        "isn\'t": "is not",
        "wasn\'t": "was not",
        "weren\'t": "were not",
        "hasn\'t": "has not",
        "hadn\'t": "had not",

        # possessive
        "\'s": " 's",
        "s\'": "s '"
    }
    EXPANSION = []
    for x, y in EXPANSION_DICT.items():
        EXPANSION.append((re.compile(x), y))

    for regexp, substitution in PUNCTUATION:
        text = regexp.sub(substitution, text)
    for regexp, substitution in DASH:
        text = regexp.sub(substitution, text)
    for regexp, substitution in DATES:
        text = regexp.sub(substitution, text)
    for regexp, substitution in EXPANSION:
        text = regexp.sub(substitution, text)
    seg_list = text.split()
    #for word in seg_list:

    #print(text.split())
    return seg_list


def removeStopwords(token_list):
    """
    input: list (of tokens);
    output: list (of tokens)
    :param token_list:
    :return: output
    """
    output = []
    stopwords = open('search/stopwords', 'r').read().split()
    for token in token_list:
        if token not in stopwords:
            output.append(token)
    return output


def stemWords(token_list):
    """
    Input: list (of tokens);
    Output: list (of stemmed tokens)
    :param token_list:
    :return: stemmed_tokens
    """
    stemmed_tokens = []
    ps = PorterStemmer()
    # make sure all non-word stuff removed, except numbers
    for token in token_list:
        if token != '.' and token != ',' and token != '?' and token != '!' and token != '\'' and token != '(' and token != ')':
            stemmed_tokens.append(ps.stem(token, 0, len(token)-1))
    return stemmed_tokens



def main():
    """
    driver program executes following steps
    i. open the folder containing the data collection, provided as the first argument on the command line
       (e.g., cranfieldDocs/), and read one file at a time from this folder.
    ii. for each file, apply, in order: removeSGML, tokenizeText, removeStopwords, stemWords
    iii. in addition, write code to determine (this is after step ii above):
    - the total number of words in the collection (numbers should be counted as words)
    - vocabulary size (i.e., number of unique terms)
    - most frequent 50 words in the collection, along with their frequencies
      (list in reverse order of their frequency, i.e., from most to least frequent)
    :return:
    """
    # step i and ii
    folder = sys.argv[1]
    files = os.listdir(path=folder)
    merged_stemword_list = []
    # print(files[1])
    for file in files:
        with open(folder+file, 'r') as fp:
            text = fp.read()
        text = removeSGML(text)
        token_list = tokenizeText(text)
        token_list = removeStopwords(token_list)
        stemword_list = stemWords(token_list)
        merged_stemword_list += stemword_list
    word_count_list = collections.Counter(merged_stemword_list)

    # step iii
    word_count = sum(word_count_list.values())
    vocabulary_size = len(set(word_count_list.keys()))

    # for the most common word part, since I did some extra process the frequencies will differ from one that only
    # perform the basic requirement of the spec. i.e.'number)' -> 'number' ')' and ')' is removed during step ii
    k_word_list = []
    k_word_freq_list = []
    for k, v in word_count_list.most_common(50):
        k_word_list.append(k)
        k_word_freq_list.append(v)

    # write to file preprocess.output
    with open('preprocess.output', 'w') as f:
        f.write("Words " + str(word_count) + '\n')
        f.write("Vocabulary " + str(vocabulary_size) + '\n')
        f.write("Top 50 words\n")

        for i in range(len(k_word_list)):
            f.write(k_word_list[i] + " " + str(k_word_freq_list[i]) + '\n')

    answer_helper(word_count, vocabulary_size, word_count_list, folder, files)


def answer_helper(word_num, vocab_size, word_count_list, folder, files):

    cur_word_count = 0
    unique_word_count = 0
    for k, v in word_count_list.most_common():
        if cur_word_count < 0.25*word_num:
            break
        cur_word_count += v
        unique_word_count += 1

    subset_size = 100
    subset_range = [[50, 550], [600, 1100]]
    range_stats = []

    merged_stemword_list = []
    # print(files[1])
    for cur_range in subset_range:
        for file in range(cur_range[0], cur_range[1]):
            with open(folder+files[file], 'r') as fp:
                # print(folder + files[file])
                text = fp.read()
            text = removeSGML(text)
            token_list = tokenizeText(text)
            token_list = removeStopwords(token_list)
            stemword_list = stemWords(token_list)
            merged_stemword_list += stemword_list
        word_count_list = collections.Counter(merged_stemword_list)
        word_count = sum(word_count_list.values())
        vocabulary_size = len(set(word_count_list.keys()))
        range_stats.append([word_count, vocabulary_size])

    with open('preprocess.answers', 'w') as f:
        f.write("Total Number of Words in Cranfield collection: " + str(word_num) + "\n")
        f.write("Vocabulary Size in Cranfield collection: " + str(vocab_size) + "\n")
        f.write("\n")
        f.write("The minimum number of unique words in the Cranfield collection accounting for 25% of the total number of words in the collection?" +
                      str(unique_word_count) + "\n")
        f.write("\n")
        f.write("Subset Statistics\n")
        for i in range(len(subset_range)):
            f.write("sample size: " + str(subset_range[i][1]-subset_range[i][0]) + "\n")
            f.write("Total Number of Words in "+"Cranfield collection: " + str(range_stats[i][0]) + "\n")
            f.write("Vocabulary Size in " + "Cranfield collection: " + str(range_stats[i][1]) + "\n")
            f.write("\n")


if __name__ == "__main__":
    main()








    """
    # test code that works through all essential functions
    folder = sys.argv[1]
    files = os.listdir(path=folder)
    # print(files[1])
    with open(folder+files[1], 'r') as fp:
        text = fp.read()
    text = removeSGML(text)
    # text = 'i\'ve The current\'s /population of U.S.A.S i-\ns 332,087.410 as of Friday. 01/22/2021, based on Worldometer elaboration of the latest United Nations\' data.'
    token_list = tokenizeText(text)
    token_list = removeStopwords(token_list)
    print(token_list)
    stemword_list = stemWords(token_list)
    print(stemword_list)
    """

    # an effective test for tokenizeText
    # text = 'i\'ve The current\'s /population of U.S.A.S i-\ns 332,087.410 as of Friday. 01/22/2021, based on Worldometer elaboration of the latest United Nations\' data.'



    #print(re.sub("([A-Z]\.*){2,}s?", "", text))
    #print(text)
    #print(tokenizeText(text))



    """
    sample code on how to modify strings
    str1 = "mystring"
    list1 = list(str1)
    list1[5] = 'u'
    str1 = ''.join(list1)
    print(str1)
    """
