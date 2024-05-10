#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    best_score = None
    best_score_key = None
    for key, value in a_dictionary.items():
        if best_score is None or best_score < value:
            best_score = value
            best_score_key = key

    return best_score_key
