from evaluationTypes.categoryBasedEvaluation import run_evaluation_for_categories
from evaluationTypes.fileBasedEvaluation import run_evaluation_for_files, debug_evaluation_for_files
import datetime


def debug():
    a = datetime.datetime.now()

    debug_evaluation_for_files()
    run_evaluation_for_categories()

    b = datetime.datetime.now()
    print("All files processed in: {0}".format(b - a))


def run():
    a = datetime.datetime.now()

    run_evaluation_for_files()
    run_evaluation_for_categories()

    b = datetime.datetime.now()
    print("All files processed in: {0}".format(b - a))
