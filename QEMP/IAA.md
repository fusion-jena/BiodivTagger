# Inter-Annotator-Agreement Measures for the QEMP corpus

The Inter-Annotator-Agreement (IAA) measure states two things: 

1.  how precise and clear categories are described 
2.  how difficult it is for humans to categorize the given terms. 

Usually, IAA is computed with Cohen's Kappa (2 annotators), Fleiss Kappa (> 2 annotators) or Krippendorff's alpha.
These metrics are fine for classification tasks but difficult to use in annotation tasks as k statistics require the counting of missing values. For instance, annotators might label different instances. 
If one annotator didn't lable a term but the second annotator did it, it would count as 'non-entity for the first annotator. 
It is not clear and defined how many terms this 'non-entity comprises, but Kappa metric can only be computed if the amount of these negative cases is quantified.

Therefore, in Named Entity Recognition tasks, other metrics are preferred such as Precision, Recall and F-Measure from Information Retrieval (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1090460/).
Here, one annotator set is used as "key" set, whereas the other annotator set is used as reference set. 
At first, some statistics are computed: the exact matches (both annotators labeled that term or phrase with the exact start/end offset), partial matches (annotations are overlapping but not identical in span) and
the missing phrases in annotator set A and the spurious annotations from annotator set B. Precision, Recall and F-Measure are computed as stated in our publication or at GATE's website (https://gate.ac.uk/sale/tao/splitch10.html#sec:eval:prf).

As the annotation of biological entities is difficult and fuzzy, which is also reflected in our results, we conducted two further rounds to create the final gold standard. 
The annotators discussed their results and created a gold standard set based on their common decisions. 
A biodiversity expert was consulted to take the final decisions in cases where the annotators could not come to an agreement.


Legend:
* Match - exact matches (both annotators labeled that term or phase with the exact start/end offset)
* Only A - only annotator A labeled the term/phrase (missing annotations)
* Only B - only annotator B labeled the term/phrase (spurious annotations)
* F1.0 means the β value in the F-Measure formular is set to 1; P and R  are weighted equally 
* lenient matching permits partial matches, annotations are overlapping but not identical in span

A - key set

B - reference set


## Bexis


| Document | Match |  Only A | Only B | Precision | Recall | F1.0-lenient | 
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| bexis_18007.xml | 3	| 31 |27 |	0.1000 | 0.0882 | 0.0938 |
| bexis_20206.xml	| 0	| 142 | 0	| 1.0000 | 0.0000 | 0.0000 |
| bexis_21136.xml	| 70| 29 |	9	| 0.8861 | 0.7071 | 0.7865 |
| bexis_21489.xml	| 18| 10 |	1	| 0.9474 | 0.6429 | 0.7660 |
| bexis_23430.xml	| 27| 11 |	6	| 0.8235 | 0.7179 | 0.7671 |
| BEXIS.19166.xml | 30	| 160 |349 | 0.0816 | 0.1623 | 0.1086 |
| BEXIS.22607.xml | 61	| 24 | 81 | 0.4336 | 0.7209	| 0.5415 |
| BEXIS.24986.xml | 15	| 8	| 26 |   0.3810 | 0.6667	| 0.4848 |
| BEXIS.25206.xml | 96	| 6	| 400 | 0.2063 | 0.9455	| 0.3388 |
| BEXIS.25786.xml | 70	| 41 |101 |  0.4481 | 0.6667 | 0.5359 |

## Befchina

| Document | Match |  Only A | Only B | Precision | Recall | F1.0-lenient | 
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| befchina_82.xml | 166	| 109 |68 | 0.7280 | 0.6254 | 0.6728 |
| befchina_150.xml | 126	| 176 |108 |	0.5731 | 0.4517 | 0.5052 |
| befchina_162.xml	| 144	| 8 | 142	| 0.5069 | 0.9481 | 0.6606 |
| befchina_224.xml	| 0	| 107 | 0	| 1.0000 | 0.0000 | 0.0000 |
| befchina_315.xml	| 124	| 190 | 75	| 0.6512 | 0.4242 | 0.5138 |
| befchina_331.xml	| 279| 25 |	11	|0.9622 | 0.9180 | 0.9396 |
| befchina_539.xml	| 278| 27 |	7	| 0.9754 | 0.9115 | 0.9424 |
| befchina_540.xml	|217| 55 |	16	| 0.9325 | 0.8007 | 0.8616 |
| befchina_542.xml	|357| 170 |	79	| 0.8631 | 0.7455 | 0.8000 |
| befchina_577.xml	| 150| 20 |118	| 0.5613 | 0.8830 | 0.6864 |


## PANGAEA

| Document | Match |  Only A | Only B | Precision | Recall | F1.0-lenient | 
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
|PANGAEA_897419.xml | 81	| 39 |34 | 0.7134 | 0.6855 | 0.6996 |
|PANGAEA_897964.xml | 29	| 7 |7 | 0.8056 | 0.8056 | 0.8056 |
|PANGAEA_898301.xml | 23	| 3 |9 | 0.7188 | 0.8846 | 0.7931 |
|PANGAEA_898616.xml | 0	| 2 |30 | 0.0000 | 0.0000 | 0.0000 |
|PANGAEA_899258.xml | 41 | 7 |4 | 0.9111 | 0.8542 | 0.8817 |
|PANGAEA_899845.xml | 21 | 25 |53 | 0.3026 | 0.4792 | 0.3710 |
|PANGAEA_900053.xml | 27 | 18 |16 | 0.6444 | 0.6170 | 0.6304 |
|PANGAEA_901178.xml | 65 | 09 |17 | 0.8000 | 0.8831 | 0.8395 |
|PANGAEA_901371.xml | 20 | 23 |31 | 0.3922 | 0.4651 | 0.4255 |
|PANGAEA_901852.xml | 37 | 23 |15 |0.7273 | 0.6349 | 0.6780 |

## Dryad

| Document | Match |  Only A | Only B | Precision | Recall | F1.0-lenient | 
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
|Dryad_203055.xml | 5	| 1 |6 | 0.4545 | 0.8333 | 0.5882 |
|Dryad_204343.xml | 17	| 0 |20 | 0.4872 | 1.000 | 0.6552 |
|Dryad_210598.xml | 11	| 10 |11 | 0.5217 | 0.5455 | 0.5333 |
|Dryad_211775.xml | 1	| 1 |3 | 0.5000 | 0.7500 | 0.600 |
|Dryad_212091.xml | 21	| 13 |4 | 0.8400 | 0.6176 | 0.7119 |
|Dryad_215642.xml | 1	| 0 |9 | 0.1000 | 1.000 | 0.1818 |
|Dryad_213760.xml | 22	| 14 |30 | 0.4340 | 0.6216 | 0.5111 |
|Dryad_214431.xml | 16	| 11 |11 | 0.6071 | 0.6071 | 0.6071 |
|Dryad_215197.xml | 3	| 6 |54 | 0.0526 | 0.333 | 0.0909 |
|Dryad_216617.xml | 6	| 6 |35 | 0.1463 | 0.5000 | 0.2264 |

## idiv

| Document | Match |  Only A | Only B | Precision | Recall | F1.0-lenient | 
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
|idiv.59.xml | 42	| 2 |39 | 0.5301 | 0.9565 | 0.6822 |
|idiv.65.xml | 16	| 3 |39 | 0.8421 | 1.0000 | 0.9143 |
|idiv.100.xml | 15	| 11 |15 | 0.500 | 0.5769 | 0.5357 |
|idiv.101.xml | 4	| 14 |32 | 0.111 | 0.2222 | 0.1481 |
|idiv.103.xml | 34	| 6 | 5 | 0.8718 | 0.8500 | 0.8608 |
|idiv.107.xml | 13	| 9 |27 | 0.3250 | 0.5909 | 0.4194 |
|idiv.108.xml | 22	| 2 |63 | 0.2574 | 0.9200 | 0.4144 |
|idiv.112.xml | 13	| 3 | 3 | 0.8125 | 0.8125 | 0.8125 |
|idiv.114.xml | 17	| 8 | 1 | 0.6923 | 1.0000 | 0.8182 |
|idiv.119.xml | 23	| 26 | 4 | 0.8571 | 0.4800 | 0.6154 |



