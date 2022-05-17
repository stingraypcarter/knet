# knet
This project is a simple implementation of boolean networks first proposed by Stuart Kauffman as a means of understanding gene regulatory networks. 

## Explanation
This short program models genes as binary that are either are expressed or are not. Whether or not a gene is expressed depends on the other genes in the network. Relationships between genes are randomly decided at the start of the program as the binary operators: AND, OR, XOR, NAND, NOR, XNOR. The process of gene expression occurs based on the expression of genes in the last iteration. The number of genes and number of iterations of the regulatory process are both arbitrary and are set as commandline arguments. This project demonstrates that as the number of genes, and therefore relations between genes increases, behavior and complexity of the network does not necessarily increase. 

demonstrates that 
