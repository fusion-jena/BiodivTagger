# BiodivTagger Pipeline
This folder contains the text mining pipeline to extract biological entities, namely materials, processes, environmental terms and data parameters. It requires Java version 8.0 and [GATE](https://gate.ac.uk/) 8.6. It was tested under Ubuntu 16.0 and Windows 10.

# Prerequisites
The BiodivTagger pipeline requires the [ontology plugin] (https://github.com/GateNLP/gateplugin-Ontology). Please install and activate the plugin first before loading the BiodivTagger. Download or clone the plugin to your local machine. In GATE 8.6, open the CREOLE Plugin Manager, click on the '+' sign, select 'Directory URL' and navigate to the folder where the plugin is located. Click 'OK' and the Ontology Plugin appears in the plugin list. In order to activate it, check the 'Load now' box.

# How to Run
Please make sure that GATE 8.6 and the [ontology plugin] (https://github.com/GateNLP/gateplugin-Ontology) are installed and activated. Open the application.xgapp file in the [Pipeline](../master/Pipeline/BT8.6) folder. The application provides a cached version of all ontologies. If you want to do any ontological changes, you need to install an own triple store, e.g., [GraphDB](http://graphdb.ontotext.com/). Alternatively, you can use remote terminology services.

# Updates

New features in v1.1 (04.08.2020):
* Service release for GATE 8.6 
* minor bugfixes in Latitude/Longitude detection


First release was v1.0 (02.12.2019)

# License 
This pipeline is distributed under the [GNU GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html). 