from config import *
#Ref: https://gate.ac.uk/sale/tao/splitch10.html
# Precision, Recall, F-Measure

def get_precision(correct, partial, spurious):
    x = get_measurement(correct, partial, spurious)
    return round(x, 3)

def get_recall(correct, partial, missing):
    x = get_measurement(correct, partial, missing)
    return round(x, 3)


def get_measurement(correct, partial, variable):
    if correct + variable + partial == 0:
        return 0

    x = (correct + (0.5 * partial)) / (correct + variable + partial)
    return round(x, 3)


def get_f_score(pr, recall):
    if pr + recall == 0:
        return 0

    x = ((beta * beta + 1) * pr * recall) / ((beta * beta * pr) + recall)
    return round(x, 3)

