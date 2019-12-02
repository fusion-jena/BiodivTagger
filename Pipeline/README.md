# BiodivTagger Pipeline
This folder contains the text mining pipeline to extract biological entities, namely materials, processes, environmental terms and data parameters. It requires Java version 8.0 and [GATE](https://gate.ac.uk/) 8.1 or [GATE](https://gate.ac.uk/) 8.2. It was tested under Ubuntu 16.0 and Windows 10.

# How to Run
Please make sure that GATE 8.1 or 8.2 is installed and running. Open the application.xgapp file in the [Pipeline](../master/Pipeline) folder. The application provides a cached version of all ontologies. If you want to do any ontological changes, you need to install an own triple store, e.g., [GraphDB](http://graphdb.ontotext.com/). Alternatively, you can use remote terminology services.


# License 
This pipeline is distributed under the [GNU GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html). 