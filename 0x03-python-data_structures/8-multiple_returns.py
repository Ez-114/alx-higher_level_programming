#!/usr/bin/python3

def multiple_returns(sentence):
    tup = ()
    if sentence is None or len(sentence) == 0:
        tup = (0, None)
        return (tup)

    tup = (len(sentence), sentence[0])
    return (tup)
