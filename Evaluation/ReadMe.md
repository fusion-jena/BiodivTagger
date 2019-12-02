General notes
-------------
* Evaluation is a python script which, processes the resulting GATE files to calculate the metrics of interest 
* It suppose to have two annotation sets 
	* Source set: “BIODIV” which is the set produced by the Pipeline 
	* Target set:  “goldStandard” which is the set of the manual annotaions

Measurement: 
-----------

* **Correct**: the number of words that are tagged the same in both of the source and target set. A word considered to be correct if and only if, it matches from the beginning and the end of the annotation and labeled with the same tag, for example:
	* Source: “Habitat” 221 227 ENVIRONMENT 
	* Target: “Habitat” 221 227 ENVIRONMENT

* **Partial**: the number of words that identified by the pipeline, however, they partially match the target set. A word is marked as partial match if and only if, it is labeled with the same tag but it matches either the start index or the end index in the target set (gold standard). For instance:
	* Example 1: 
        * Source: “acquisition” 519 529 PROCESS
	    * Target: “nutrient acquisition” 510 529 PROCESS
	* Example 2:
        * Source: “dry” 700 703 QUALITY
	    * Target: “dry mass” 700 708 QUALITY

* **Spurious**: the number of words detected and labeled by the pipeline, while, there are no references for them in the target set (gold standard)

* **Missing**: the number of words annotated in the target set (gold standard) but missing or not detected at all by the pipeline
 
Metrics: 
-----------
* **Precision** = (Correct + 0.5 * Partial) / (Correct + Spurious + Partial)
* **Recall** = (Correct + 0.5 * Partial) / (Correct + Missing + Partial)
* **F-Measure** = ((2 * Precision) + Recall) / (Precision + Recall) if we set the beta = 1, it gives the precision and the recall an equal weight. 

Global Metrics: 
-----------
* **Macro Avg** = Macro average of all the three metrics (Precision, Recall, F-Measure), is provided by averaging the metric of all the supported four categories 

* **Micro Avg** = it deal with corpus as a very large document. Such that, it pay attention to the dominant category, the one with the most mentions. That’s why it is more useful for the skewed corpora. 


Resultant Files
---------
* **evaluation_results_files.csv**: This file represents the measurement inside each file.
* **evaluation_results_category.csv**: this file represents the measurement grouped by each category
* **macro_evaluation_results.csv**: this file tells the macro avg as a global metrics
* **micro_evaluation_results.csv**: this file show the micro avg as a global metrics


Reproducibility  
-----------
* make sure the config file has the following entries 
	* execution_mode = 1
	* beta = 1 (balance for precision and recall)
	* src_set_name = “BIODIV”
	* target_set_name = “goldStandard”
* All GATE documents that need to be evaluated must be located directly in the root_dir, default value of it is files as in the config file
* results folder will be automatically created, make sure to remove it before the beginning of the run

* Command line: 
	* Windows: python main.py for python2.7+ or py main.py for python 3+
	* Ubuntu: python main.py python2.7+ or python3 main.py for python3+

* To reproduce the results per data repository, 4 run will be required, each time locate the files from the desired repository directly into the root_dir, default value of the root_dir is “files”

Dependancies:
---------
* pandas 
