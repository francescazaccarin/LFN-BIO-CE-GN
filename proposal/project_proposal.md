# Learning from Networks — Project Proposal

## 1. Title

Exploring Biological Networks: Centrality and Clustering Analysis on the BIO-CE-GN Dataset

This project was developed as part of the course *“Learning from Networks”* for the Master’s Degree in Computer Engineering.  
The goal of this project is to analyse a biological network and perform various graph-theoretic analyses to understand its structural and functional properties.
---


## 2. Motivation

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

**Citation:**  
Rossi, R. A., & Ahmed, N. K. (2015). *The Network Data Repository with Interactive Graph Analytics and Visualization.* AAAI.

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

# Appendix: Team Contributions and AI Tools

## Contributions
| Member | Contribution | Fraction |
|---------|---------------|-----------|
| Francesca Zaccarin | Repository setup, dataset integration, README draft
| ZhangShen | Motivation writing, proposal structure, references and appendix

## Use of AI Tools
We used ChatGPT to refine the writing style and structure of the proposal document.
