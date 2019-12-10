# BiodivTagger Repository

This repository provide contains the QEMP corpus, a metadata corpus from biodiversity research data with 50 metadata files from 5 different repositories and biodiversity related projects as well as the BiodivTagger, a text mining pipeline that extracts biological entities.


## Structure

* [Pipeline](../master/Pipeline) *contains the text mining pipeline to annotate biological Named Entities.*
* [Evaluation](../master/Evaluation) *contains the python script to evaluate the pipeline with the gold standard and the evaluation results.*
* [QEMP Corpus](../master/QEMP) *contains the raw metadata xml files per data repository and the gold standard in json format.*
* [Ontological Issues List](../master/conflicts_missing_annotations.md) *provides a list with missing ontological entries and ontological conflicts.*

## Licenses

* [Pipeline](../master/Pipeline) *The BiodivTagger is distributed under the [GNU GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)*
* [QEMP Corpus](../master/QEMP) *The QEMP corpus is distributed under the [CC-BY-4.0](https://creativecommons.org/licenses/by-nc/4.0/)*