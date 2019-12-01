from config import *
import os
import pandas as pd


def saveDataFrameToCSV(pd1, csv_path, append):
    if not os.path.exists(results_dir):
        os.mkdir(results_dir)

    dataset_path = os.path.join(results_dir, csv_path)

    if append:
        with open(dataset_path, 'a+') as f:
            pd1.to_csv(dataset_path, mode='a', index=False, header=False)
    else:
        with open(dataset_path, 'a+') as f:
            pd1.to_csv(dataset_path, mode='a', index=False, header=True)


def addMetricsToDataframe(file, correct, missing, spurious, partial, pr, recall, f_score):
    # fileId, correct, missing, specious, partials, pr, r, f
    pd1 = pd.DataFrame({"ID": pd.Series(file), "Correct": pd.Series(correct)
                           , "Missing": pd.Series(missing), "Spurious": pd.Series(spurious)
                           , "Partial": pd.Series(partial), "Pr": pd.Series(pr)
                           , "Recall": pd.Series(recall), "F-Score": pd.Series(f_score)})
    return pd1


def saveMetricsToCSV(avg_pr, avg_recall, avg_f_score, file_path):
    pd1 = pd.DataFrame({"Pr": pd.Series(avg_pr), "Recall": pd.Series(avg_recall), "F_Score": pd.Series(avg_f_score)})
    saveDataFrameToCSV(pd1, file_path, False)
