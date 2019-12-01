from os import listdir
from os.path import isfile, join
from evaluationModule import *
from metrics import *
from inout import *
import numpy as np


def __get_metrics_per_category(correct_lst, partial_lst, spurious_lst, missing_lst):
    for st_i, supported_tag in zip(range(len(SUPPORTED_TAGS)), SUPPORTED_TAGS):
        # Metrics
        pr = get_precision(correct_lst[st_i], partial_lst[st_i], spurious_lst[st_i])
        recall = get_recall(correct_lst[st_i], partial_lst[st_i], missing_lst[st_i])
        f_score = get_f_score(pr, recall)
        print(supported_tag)
        print(pr, recall, f_score)
        print("\n")

        df = addMetricsToDataframe(supported_tag, correct_lst[st_i], missing_lst[st_i], spurious_lst[st_i],
                                   partial_lst[st_i] \
                                   , pr, recall, f_score)

        saveDataFrameToCSV(df, category_csv_path, append=bool(st_i))
        print("Saved to the Categories CSV!")


def __get_macro_avg_metrics(correct_lst, partial_lst, spurious_lst, missing_lst):
    pr_lst = []
    recall_lst = []
    f_score_lst = []
    for st_i, supported_tag in zip(range(len(SUPPORTED_TAGS)), SUPPORTED_TAGS):
        # Metrics
        pr = get_precision(correct_lst[st_i], partial_lst[st_i], spurious_lst[st_i])
        recall = get_recall(correct_lst[st_i], partial_lst[st_i], missing_lst[st_i])
        f_score = get_f_score(pr, recall)

        pr_lst = pr_lst + [pr]
        recall_lst = recall_lst + [recall]
        f_score_lst = f_score_lst + [f_score]

    avg_pr = round(sum(pr_lst) / len(pr_lst), 3)
    avg_recall = round(sum(recall_lst) / len(recall_lst), 3)
    avg_f_score = round(sum(f_score_lst) / len(f_score_lst), 3)
    saveMetricsToCSV(avg_pr, avg_recall, avg_f_score, macro_csv_path)
    print(avg_pr, avg_recall, avg_f_score)


def __get_micro_avg_metrics(correct_lst, partial_lst, spurious_lst, missing_lst):
    correct = 0
    partial = 0
    spurious = 0
    missing = 0

    for st_i, supported_tag in zip(range(len(SUPPORTED_TAGS)), SUPPORTED_TAGS):
        correct = correct + correct_lst[st_i]
        partial = partial + partial_lst[st_i]
        spurious = spurious + spurious_lst[st_i]
        missing = missing + missing_lst[st_i]

    micro_pr = get_precision(correct, partial, spurious)
    micro_recall = get_recall(correct, partial, missing)
    micro_f_score = get_f_score(micro_pr, micro_recall)

    saveMetricsToCSV(micro_pr, micro_recall, micro_f_score, micro_csv_path)
    print("Saved to the Micro CSV!")


def run_evaluation_for_categories():
    onlyfiles = [f for f in listdir(root_dir) if isfile(join(root_dir, f))]
    print(onlyfiles)

    # 4 x 1 lists accumlator for each category
    correct_lst = np.zeros(shape=(len(SUPPORTED_TAGS)))
    partial_lst = np.zeros(shape=(len(SUPPORTED_TAGS)))
    missing_lst = np.zeros(shape=(len(SUPPORTED_TAGS)))
    spurious_lst = np.zeros(shape=(len(SUPPORTED_TAGS)))

    for i, file in zip(range(len(onlyfiles)), onlyfiles):
        root = get_root(file)
        src_set, target_set = get_sets(root, src_set_name, target_set_name)

        for st_i, supported_tag in zip(range(len(SUPPORTED_TAGS)), SUPPORTED_TAGS):
            # original sets
            src_pd = get_anno_lst(src_set, [supported_tag])
            target_pd = get_anno_lst(target_set, [supported_tag])
            src = len(src_pd)
            target = len(target_pd)

            # Matches ...
            correct_pd = get_correct(src_pd, target_pd)

            # Partials ...
            remaining_src = get_difference(correct_pd, src_pd)  # src - correct
            remaining_target = get_difference(correct_pd, target_pd)
            partial_pd, partial_target_pd = get_partial_matches(remaining_src, remaining_target)

            # Statistics ...
            correct = len(correct_pd)
            partial = len(partial_pd)
            missing = target - (correct + partial)
            spurious = src - (correct + partial)

            correct_lst[st_i] = correct_lst[st_i] + correct
            partial_lst[st_i] = partial_lst[st_i] + partial
            missing_lst[st_i] = missing_lst[st_i] + missing
            spurious_lst[st_i] = spurious_lst[st_i] + spurious

    __get_metrics_per_category(correct_lst, partial_lst, spurious_lst, missing_lst)

    # Macro and Micro calculations ...
    __get_macro_avg_metrics(correct_lst, partial_lst, spurious_lst, missing_lst)
    __get_micro_avg_metrics(correct_lst, partial_lst, spurious_lst, missing_lst)
