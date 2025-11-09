# Learning from Networks — Project Proposal

## 1. Title

Exploring Biological Networks: Centrality and Clustering Analysis on the BIO-CE-GN Dataset

---


## 2. Motivation

Biological neural systems are amazing and complex networks that govern how living organisms deal with information.
Learning about their structure may help scientists figure out how links among neurons influence communication and the way they work.

As a case study, we analyze the *BIO-CE-GN* dataset that describes the entire neural network of *C. elegans*.
If we represent neurons as nodes and synapses as edges, graph theory can be used to investigate how the network is structured and how information potentially moves through it.

We aim to apply results from network science in description of its main structural properties—connectivity, centrality and clustering—and in uncovering the patterns that could be found available in other real world networked systems.
Reach The goals of the *How to Learn from Networks* class are also embraced by this project, where graph based models can aid our understanding of complex systems.

---

## 3. Dataset
The dataset used in this project is the **BIO-CE-GN** network, obtained from the [Network Repository](https://networkrepository.com/bio-ce-gn.php).  
It represents a **biological neural connectivity network** (*C. elegans*) where:
- **Nodes** represent neurons  
- **Edges** represent synaptic connections between neurons  
- The network is **directed** and **weighted**

**Dataset Information:**
- **Number of Nodes:** 2,975  
- **Number of Edges:** 54,990  
- **Maximum Degree:** 242  
- **Average Degree:** 48  
- **Size:** ~512 KB  

---

## 4. Objectives and Methodology
### 4.1 Objectives
The main goal of this project is to study the **structure and properties** of the biological network and compare the results with patterns typically observed in real-world biological systems.

Specifically, we aim to:
1. Compute **basic graph properties** (size, degree distribution, connectivity, density)  
2. Calculate **centrality measures** (degree, closeness, betweenness)  
3. Analyse **clustering coefficient** and **community structure**  
4. Optionally, explore **motifs** and **biological relevance** of network patterns  

### 4.2 Methodology
The project will use **Python** and the **NetworkX** package to:
- Load and process the graph dataset  
- Perform topological analysis  
- Generate visualizations  
- Store computed metrics in structured outputs (JSON, CSV, PNG)

All analyses and experiments will be performed on local machines using Jupyter Notebook or Python scripts.

---

## 5. Intended Experiments

---

## 6. References

1. Ryan A. Rossi and Nesreen K. Ahmed (2015). *The Network Data Repository with Interactive Graph Analytics and Visualization.* AAAI. [https://networkrepository.com](https://networkrepository.com)
2. Newman, M. E. J. (2003). *The Structure and Function of Complex Networks.* *SIAM Review*, 45(2), 167–256.
3. Brandes, U. (2001). *A Faster Algorithm for Betweenness Centrality.* *Journal of Mathematical Sociology*, 25(2), 163–177.
4. Watts, D. J., & Strogatz, S. H. (1998). *Collective Dynamics of ‘Small-World’ Networks.* *Nature*, 393(6684), 440–442.

---

# Appendix: Team Contributions and AI Tools

## Contributions
| Member | Contribution | Fraction |
|---------|---------------|-----------|
| Francesca Zaccarin | Repository setup, dataset integration, README draft
| ZhangShen | Motivation writing, proposal structure, references and appendix

## Use of AI Tools
We used ChatGPT to refine the writing style and structure of the proposal document.
