


## Description
This program uses clustering approach to find out the best binding protein for an aptamer with an unkown binding protein.
This is usefull for identification of Aptamer Motifs that bind to proteins, and are generated by whole cell SELEX.

This program runs by clustering polypeptide chains after vectorising them by using PseAAC algorithm.
The program has two options. You can either upload a FASTA folder with protein sequences (kindly note that the program will
return an error message if presented with sequences that contain sequences other than protein), or you can generate polypeptides,
based on a Probability matrix installed in the program. The length of the polypeptide is a user input.

After clustering a FASTA file is generated containg the clustered polypetide sequences and their cluster number. 
A picture of the clusters is also generated, to visualise the clusters.

Hdock link is included in the software package. The cluster centers are to be docked using hex dock and the best docking 
cluster can be indentified as the cluster center that shows the least binding energy.

Once the best binding cluster is identlfied the user can take the polypeptides in the best binding cluster and reculster,
using KAMI or randomly select proteins from the cluster to find the best match.

Kindly note that using this program for a low number of proteins (less than 10) will not be a very efficient 
use of the program. The program works best for a large sample size and can reduce the docking requirements in such cases
by 90%.

## Installation


To run first ensure all python dependencies are in order. 
Can be found in dependency.yml

Install with anaconda:  
``` conda env create -f dependency.yml ```

Then run with: 
``` python app.py ``` <br>
(do not close the terminal). <br>
Open a browser and navigate to 
http://localhost:5000/
The web-app will be running.


## Usage

Upload a FASTA file or select generate polypeptide. The length of the polypeptide will need to be mentioned in this case.
Enter the number of clusters to be generated and the lambda value (note: Lambda should be less then the length of the smallest protein in the FASTA, or after generation)
(note: we recommend using a lambda value od 5-6 for running the program)
Select run.
The Cluster centers sequences can be seen on the window, and a downloadable file conatining the clustered proteins will appear.
Download the Cluster centers, and the clustered file.
Dock the cluster center sequences using Hex dock, inclueded in the software package.
(kindly note that if you run the software using generated proteins, you will need to generate a PDB file before running the docking step)
Select the best cluster, based on the cluster center which shows the least binding energy
Dock random sequences in the best cluster, or re-eneter the best cluster FASTA into this program to recluster 
