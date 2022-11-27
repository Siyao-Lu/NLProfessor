######################################################
# weighting scheme:
# spec choice: tfc.tfx
# my choice: nfc.nfx
######################################################

######################################################
# inverted index structure design:
# Use python dictionary, since during indexing documents, the program will do random access a lot,
# thus in order to reduce access time, use a hashmap structure, which in python is dict.
# What it will look like inside:
# {
#   'doc_count': int count total documents
#
# 	'word1': {'df': int, document frequency for word1,
# 			  'doc_list': {doc1: tf, doc2: tf, ...}
# 			  }
#   'word2':...
#   ...
# }
######################################################


import sys
import collections
import preprocess
import math
import numpy as np
import json


def documentWeightsHelper(docs_scheme, index_map):
    """
    input: document weighting scheme
    input: inverted index
    return: weight matrix,
    return: docs length
    return: corresponding document number array

    helper function to calculate documents weights vectors
    """
    # pop doc_count for convenience, add back later
    doc_count = index_map.pop('doc_count')

    # list of strings, stores in the sequence corresponding to the weight in vector of weight matrix
    word_loc_map = list(index_map.keys())

    index_map['doc_count'] = doc_count

    # weights matrix,
    # each row corresponds to a document weights vector,
    # each column corresponds to weights for a specific word weights, in the sequence of word_loc_map
    weights_matrix = np.zeros((doc_count, len(word_loc_map)))
    doc_length = np.zeros((doc_count,))

    # calculate weights vectors
    for doc in range(doc_count):
        weights_vec = []
        if docs_scheme == 'tfc':
            for word in word_loc_map:
                if word in index_map and doc in index_map[word]['doc_list']:
                    f = math.log10(index_map['doc_count']/index_map[word]['df']) # calc f
                    w_temp = index_map[word]['doc_list'][doc] * f
                    weights_vec.append(w_temp) # calc t*f
                else:
                    weights_vec.append(0)
            weights_vec = np.array(weights_vec)

        if docs_scheme == 'nfc':
            f_vec = []
            for word in word_loc_map:
                if word in index_map and doc in index_map[word]['doc_list']:
                    w_temp = index_map[word]['doc_list'][doc]
                    weights_vec.append(w_temp)
                else:
                    weights_vec.append(0)
                f = math.log10(index_map['doc_count'] / index_map[word]['df'])  # calc f
                f_vec.append(f)
            f_vec = np.array(f_vec)
            weights_vec = np.array(weights_vec)
            weights_vec = 0.5 + 0.5 * np.divide(weights_vec, np.max(weights_vec))
            weights_vec = np.multiply(weights_vec, f_vec)

        c = np.linalg.norm(weights_vec, 2)
        weights_vec = np.divide(weights_vec, c)

        weights_matrix[doc] = weights_vec

        # calculate length
        doc_length[doc] = np.linalg.norm(weights_vec, 2)

    return weights_matrix, doc_length, word_loc_map

def indexDocument(text, docs_scheme, query_scheme, index_map):
    """
    input: the content of the document (string);
    input: weighting scheme for documents (string);
    input: weighting scheme for query (string);
    input/output: inverted index (your choice of data structure)

    preprocess the content provided as input, i.e., apply removeSGML, tokenizeText,
    removeStopwords, stemWords, as you did in Assignment 1.
    add the tokens to the inverted index provided as input and compile the counts necessary to
    calculate the term weights for the given weighting schemes.
    Note: the inverted index will be updated with the tokens from the document being processed.
    """
    if (docs_scheme == 'tfc' and query_scheme == 'tfx') or (docs_scheme == 'nfc' and query_scheme == 'nfx') or (docs_scheme == 'tfc' and query_scheme == 'nfx') or (docs_scheme == 'nfc' and query_scheme == 'tfx'):
        text = text.lower()
        text = preprocess.removeSGML(text)
        token_list = preprocess.tokenizeText(text)
        token_list = preprocess.removeStopwords(token_list)
        token_list = preprocess.stemWords(token_list)
        doc = index_map['doc_count']

        # use a intermediate word dictionary to count word tf
        counter = collections.Counter(token_list)
        # merge counter to the inverted index map
        for word, tf in counter.items():
            if word in index_map:
                index_map[word]['doc_list'][doc] = tf
                index_map[word]['df'] += 1
            else:
                index_map[word] = {'df': 1, 'doc_list': {doc: tf}}
    else:
        raise ValueError('Input scheme not accepted yet, please try other scheme in command line')


    return index_map


def retrieveDocuments(query, index_map, docs_scheme, query_scheme, weights_matrix, doc_length, word_loc_map):
    """
    input: query (string);
    input: inverted index (your choice of data structure);
    input: weighting scheme for documents (string);
    input: weighting scheme for query (input);
    input: weights_matrix, doc_length, word_loc_map; see documentWeightsHelper comments
    output: ids for relevant documents, along with similarity scores (dictionary)

    preprocess the query, i.e., removeSGML, tokenizeText, removeStopwords, stemWords, as you did in Assignment 1
    determine the set of documents from the inverted index that include at least one token from the query.
    calculate the cosine similarity between the query and each of the documents in this set,
    using the given weighting schemes to calculate the document and the query term weights
    """
    # process query
    query = query.lower()
    query = preprocess.removeSGML(query)
    token_list = preprocess.tokenizeText(query)
    token_list = preprocess.removeStopwords(token_list)
    token_list = preprocess.stemWords(token_list)
    counter = collections.Counter(token_list)
    counter_seq = list(counter.keys())

    # find the set of docs that have words in query
    doc_set = set()
    for word in counter.keys():
        if word in index_map:
            # add potential new doc number to the set
            doc_set.update(index_map[word]['doc_list'].keys())
        else:
            pass



    # calculate query weights
    query_weights = []
    if query_scheme == 'tfx':
        for word in word_loc_map:
            if word in counter:
                f = math.log10(index_map['doc_count'] / index_map[word]['df'])  # calc f
                w_temp = counter[word] * f
                query_weights.append(w_temp)  # calc t*f
            else:
                query_weights.append(0)
        query_weights = np.array(query_weights)
    if query_scheme == 'nfx':
        f_vec = []
        for word in word_loc_map:
            if word in counter:

                w_temp = counter[word]
                query_weights.append(w_temp)
            else:
                query_weights.append(0)
            f = math.log10(index_map['doc_count'] / index_map[word]['df'])  # calc f
            f_vec.append(f)
        f_vec = np.array(f_vec)
        query_weights = np.array(query_weights)

        query_weights = 0.5 + 0.5 * np.divide(query_weights, np.max(query_weights))
        query_weights = np.multiply(query_weights, f_vec)
    # calculate cos similarity for each relevant doc
    doc_sim_dict = {}
    for doc in doc_set:
        # as addressed in lecture do not consider query length
        cos = np.sum(np.multiply(query_weights, weights_matrix[doc])) / doc_length[doc]
        doc_sim_dict[doc] = cos


    return doc_sim_dict










def main():
    docs_scheme = "tfc"
    query_scheme = "tfx"
    db_file = sys.argv[1]
    query = ' '.join(sys.argv[2:])
 


    # Opening JSON file
    with open(db_file) as json_file:
        data = json.load(json_file)

    # init a inverted index structure
    index_map = {'doc_count': 0}

    # sort in alphanumeric list order to better accommodate later output
    classes = sorted(data.keys())
    for _class in classes:
        text = data[_class]['name'] + ' ' + data[_class]['desc']
        index_map = indexDocument(text, docs_scheme, query_scheme, index_map)
        index_map['doc_count'] += 1

    weights_matrix, doc_length, word_loc_map = documentWeightsHelper(docs_scheme, index_map)

    query_doc_dict = {}
    doc_sim_dict = retrieveDocuments(query, index_map, docs_scheme, query_scheme,
                        weights_matrix, doc_length, word_loc_map)
    candidates = doc_sim_dict
    doc_list, sim_list = zip(*candidates.items()) # makes sure sequences match
    sort_idx = np.argsort(-np.array(sim_list))
    doc_list = np.array(doc_list)[sort_idx]
    sim_list = np.array(sim_list)[sort_idx]
    for i in range(len(doc_list[:5])):
        print(data[classes[doc_list[i]]])




if __name__ == '__main__':
    main()

