# knet
This project is a simple implementation of boolean networks first proposed by Stuart Kauffman as a means of understanding gene regulatory networks. 

## Requirements
- Matplotlib

## Explanation
This short program models genes as binary that are either are expressed or are not. Whether or not a gene is expressed depends on the other genes in the network. Relationships between genes are randomly decided at the start of the program as the binary operators: AND, OR, XOR, NAND, NOR, XNOR. The process of gene expression occurs based on the expression of genes in the last iteration. The number of genes and number of iterations of the regulatory process are both arbitrary and are set as commandline arguments. This project demonstrates that as the number of genes, and therefore relations between genes increases, behavior and complexity of the network does not necessarily increase. This is surprising because the randomly decided stochastic process can often be represented by a finite repetitive cycle.

With a number of genes n, the state of the system can be represented as a decimal value <= 2^n. For this reason, the state of the system can be plotted over a number of iterations without losing information. Very frequently the system falls into a repetitive cycle of length < sqrt(n). From an inforamtion theoretic persepctive this is interesting (at least to me) as the behavior of a seemingly complex system can be compressed. Additionally, the initial expression of the genes is random and for differing starts the genes are still likely to fall into a simple cycle. For some networks this demonstrates stability and resiliency to initial condition while for others it indicates chaos and high sensitivity to initial conditions.

## Examples
- Here a set of 10 genes falls into a fixed state in only three iterations.
  [10 Stable](Resources/10_Stable.jpg)
- In this example 10 genes fall into a cycle in 12 iterations with a cycle length of 9 repeating the states: [0, 160, 148, 44, 16, 172, 52, 28, 76].
  [10 Cycle](Resources/10_Cycle.jpg)
- Increasing the number of genes to 100 leads to a more complex cycle occuring at iteration 72 with a length 28.
  [100 Cycle](Resources/100_Cycle.jpg)


## More Reading
Here the cycles represent attractors that may occur in gene regulation and expression where the iteration length represents transient time. This model is highly simplified but still exemplifies the power of randomly assembled relational networks. Kauffman first proposed gene attractors while trying to understand how cells become specialized in early human development. Additionally he tied the idea of attractor complexity to the probability of a cell becoming cancerous. For more reading on this and boolean networks check out theses links!
- [Gene Regulatory Networks Wikipedia](https://en.wikipedia.org/wiki/Gene_regulatory_network)
- [Boolean Networks Wikipedia](https://en.wikipedia.org/wiki/Boolean_network)
- [Homeostasis and Differentiation in Random Genetic Control Networks](https://www.nature.com/articles/224177a0)
- [Stability of the Kauffman model](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.65.016129)
