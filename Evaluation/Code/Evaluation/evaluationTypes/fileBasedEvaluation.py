from os import listdir
from os.path import isfile, join
from evaluationModule import *
from metrics import *
from inout import *

def debug_evaluation_for_files():
    onlyfiles = [f for f in listdir(root_dir) if isfile(join(root_dir, f))]
    print(onlyfiles)

    for i, file in zip(range(len(onlyfiles)), onlyfiles):
        root = get_root(file)
        src_set, target_set = get_sets(root, src_set_name, target_set_name)

        # original sets
        src_pd = get_anno_lst(src_set)
        target_pd = get_anno_lst(target_set)

        # Correct (Matches) ...
        correct_pd = get_correct(src_pd, target_pd)
        saveDataFrameToCSV(correct_pd, file + "_correct.csv", False)

        # Partials ...
        remaining = get_difference(correct_pd, src_pd)  # src - correct
        partial_src_pd, partial_target_pd = get_partial_matches(remaining, target_pd)
        saveDataFrameToCSV(partial_src_pd, file + "_partial_src_records.csv", False)

        # Missing ...
        src_without_partial = get_difference(partial_src_pd, src_pd)  # src - partial
        target_without_partial = get_difference(partial_target_pd, target_pd)  # target - partial
        missing_pd = get_difference(src_without_partial, target_without_partial)  # target - src
        saveDataFrameToCSV(missing_pd, file + "_missing.csv", False)

        # Spurious ...
        # temporary add partials to the target then get the difference
        target_with_partial = target_pd.append(partial_src_pd, ignore_index=True)
        spurious_pd = get_difference(target_with_partial, src_pd)  # src - (target + partial)
        saveDataFrameToCSV(spurious_pd, file + "_spurious.csv", False)

        # Statistics ...
        correct = len(correct_pd)
        missing = len(missing_pd)
        spurious = len(spurious_pd)
        partial = len(partial_src_pd)

        # Metrics
        pr = get_precision(correct, partial, spurious)
        recall = get_recall(correct, partial, missing)
        f_score = get_f_score(pr, recall)
        print(pr, recall, f_score)

        df = addMetricsToDataframe(file, correct, missing, spurious, partial, pr, recall, f_score)

        saveDataFrameToCSV(df, csv_path, append=bool(i))
        print("Saved to the CSV!")



def run_evaluation_for_files():
    onlyfiles = [f for f in listdir(root_dir) if isfile(join(root_dir, f))]
    print(onlyfiles)

    for i, file in zip(range(len(onlyfiles)), onlyfiles):
        root = get_root(file)
        src_set, target_set = get_sets(root, src_set_name, target_set_name)

        # original sets
        src_pd = get_anno_lst(src_set)
        target_pd = get_anno_lst(target_set)
        src = len(src_pd)
        target = len(target_pd)

        # Matches ...
        correct_pd = get_correct(src_pd, target_pd)

        # Partials ...
        # Partials ...
        remaining_src = get_difference(correct_pd, src_pd)  # src - correct
        remaining_target = get_difference(correct_pd, target_pd)
        partial_pd, partial_target_pd = get_partial_matches(remaining_src, remaining_target)

        # Statistics ...
        correct = len(correct_pd)
        partial = len(partial_pd)

        missing = target - (correct + partial)
        spurious = src - (correct + partial)

        # Metrics
        pr = get_precision(correct, partial, spurious)
        recall = get_recall(correct, partial, missing)
        f_score = get_f_score(pr, recall)
        print(pr, recall, f_score)

        df = addMetricsToDataframe(file, correct, missing, spurious, partial, pr, recall, f_score)

        saveDataFrameToCSV(df, csv_path, append=bool(i))
        print("Saved to the CSV!")
