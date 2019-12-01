import os
import pandas as pd
import xml.etree.ElementTree as ET
from config import *


def get_root(file):
    root = ET.parse(os.path.join(root_dir, file)).getroot()
    return root


def get_sets(root, src_set_name, target_set_name):
    anno_sets = root.findall('AnnotationSet')

    for anno_set in anno_sets:
        anno_set_name = anno_set.get("Name")
        if anno_set_name is not None:
            if anno_set_name.lower() == src_set_name.lower():
                src_set = anno_set
                continue
            if anno_set_name.lower() == target_set_name.lower():
                taget_set = anno_set
                continue

    return src_set, taget_set


def get_anno_lst(anno_set, s_tags=SUPPORTED_TAGS):
    my_set = None
    anno_lst = anno_set.findall("Annotation")
    for anno in anno_lst:
        s = anno.get("StartNode")
        e = anno.get("EndNode")
        t = anno.get("Type")
        if t in s_tags:
            if my_set is None:
                my_set = {(s, e, t)}
            else:
                my_set.update([(s, e, t)])

    start = []
    end = []
    tag = []
    if my_set is not None:
        for anno_elem in my_set:
            start = start + [anno_elem[0]]
            end = end + [anno_elem[1]]
            tag = tag + [anno_elem[2]]

    pd1 = pd.DataFrame({'start': pd.Series(start), 'end': pd.Series(end), 'tag': pd.Series(tag)})
    return pd1


def get_correct(src_pd, target_pd):
    tag = []
    start = []
    end = []
    for i in range(len(src_pd)):
        for j in range(len(target_pd)):
            if src_pd["start"][i] == target_pd["start"][j] and \
                    src_pd["end"][i] == target_pd["end"][j] and \
                    src_pd["tag"][i] == target_pd["tag"][j]:
                start = start + [src_pd["start"][i]]
                end = end + [src_pd["end"][i]]
                tag = tag + [src_pd["tag"][i]]

    pd1 = pd.DataFrame({'start': pd.Series(start), 'end': pd.Series(end), 'tag': pd.Series(tag)})
    return pd1


def get_difference(A, B):  # B - A
    tag = []
    start = []
    end = []
    for i in range(len(B)):
        found = False
        for j in range(len(A)):
            if B["start"][i] == A["start"][j] and \
                    B["end"][i] == A["end"][j] and \
                    B["tag"][i] == A["tag"][j]:
                found = True

        if not found:
            start = start + [B["start"][i]]
            end = end + [B["end"][i]]
            tag = tag + [B["tag"][i]]

    pd1 = pd.DataFrame({'start': pd.Series(start), 'end': pd.Series(end), 'tag': pd.Series(tag)})
    return pd1


# def get_text(root, start, end):
#    text = ""
#    textWithNodes = root.find('TextWithNodes')
#    nodes = textWithNodes.findall("Node")
#    for node in nodes:
#        id = node.get("id")
#        if id == start or id == end:
#            if node.text is not None:
#                text = text + node.text
#    return text


def get_partial_matches(src_pd, target_pd):
    tag = []
    start = []
    end = []

    tag_target = []
    start_target = []
    end_target = []

    for i in range(len(src_pd)):
        for j in range(len(target_pd)):
            if src_pd["tag"][i] == target_pd["tag"][j]:
                if (int(src_pd["start"][i]) == int(target_pd["start"][j]) and \
                    int(src_pd["end"][i]) < int(target_pd["end"][j])) \
                        or \
                        (int(src_pd["start"][i]) > int(target_pd["start"][j]) and \
                         int(src_pd["end"][i]) == int(target_pd["end"][j])): \

                        start = start + [src_pd["start"][i]]
                        end = end + [src_pd["end"][i]]
                        tag = tag + [src_pd["tag"][i]]

                        start_target = start_target + [target_pd["start"][j]]
                        end_target = end_target + [target_pd["end"][j]]
                        tag_target = tag_target + [target_pd["tag"][j]]



    partial_matches_pd = pd.DataFrame({'start': pd.Series(start), 'end': pd.Series(end), 'tag': pd.Series(tag)})
    partial_target_matches_pd = pd.DataFrame({'start': pd.Series(start_target), 'end': pd.Series(end_target), 'tag': pd.Series(tag_target)})

    assert len(partial_matches_pd) == len(partial_target_matches_pd)
    return partial_matches_pd, partial_target_matches_pd

def get_partial_matches(src_pd, target_pd):
    tag = []
    start = []
    end = []

    tag_target = []
    start_target = []
    end_target = []

    for i in range(len(src_pd)):
        for j in range(len(target_pd)):
            if src_pd["tag"][i] == target_pd["tag"][j]:
                if (int(src_pd["start"][i]) == int(target_pd["start"][j]) and \
                    int(src_pd["end"][i]) < int(target_pd["end"][j])):
                    start = start + [src_pd["start"][i]]
                    end = end + [src_pd["end"][i]]
                    tag = tag + [src_pd["tag"][i]]

                    start_target = start_target + [target_pd["start"][j]]
                    end_target = end_target + [target_pd["end"][j]]
                    tag_target = tag_target + [target_pd["tag"][j]]

                elif (int(src_pd["start"][i]) > int(target_pd["start"][j]) and \
                     int(src_pd["end"][i]) == int(target_pd["end"][j])):

                    start = start + [src_pd["start"][i]]
                    end = end + [src_pd["end"][i]]
                    tag = tag + [src_pd["tag"][i]]

                    start_target = start_target + [target_pd["start"][j]]
                    end_target = end_target + [target_pd["end"][j]]
                    tag_target = tag_target + [target_pd["tag"][j]]



    partial_matches_pd = pd.DataFrame({'start': pd.Series(start), 'end': pd.Series(end), 'tag': pd.Series(tag)})
    partial_target_matches_pd = pd.DataFrame({'start': pd.Series(start_target), 'end': pd.Series(end_target), 'tag': pd.Series(tag_target)})

    assert len(partial_matches_pd) == len(partial_target_matches_pd)
    return partial_matches_pd, partial_target_matches_pd
