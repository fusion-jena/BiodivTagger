root_dir = "../files"
results_dir = "../results"

src_set_name = "BIODIV"
target_set_name = "goldStandard"
beta = 1 #balance between pr and recall in F-Score measurement
csv_path = "evaluation_results_files.csv"
category_csv_path = "evaluation_results_category.csv"
macro_csv_path = "macro_evaluation_results.csv"
micro_csv_path = "micro_evaluation_results.csv"
SUPPORTED_TAGS = ["Environment", "Material", "Process", "Quality"]

#1 = Run
#2 = Debug
execution_mode = 2