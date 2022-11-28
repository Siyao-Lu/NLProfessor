import re
from PorterStemmer import PorterStemmer

def removeSGML(text):
    """
    Name: removeSGML;
    Input: string;
    Output: string
    :param text:
    :return: result
    Match anything from '<' to '>' and remove
    """
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

