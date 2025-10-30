# Exploring Biological Networks: Centrality and Clustering Analysis on the BIO-CE-GN Dataset
**Learning from Networks Project**

This project was developed as part of the course *“Learning from Networks”* for the Master’s Degree in Computer Engineering.  
The goal of this project is to analyse a **biological network** and perform various graph-theoretic analyses to understand its structural and functional properties.

---

## **Dataset**
The dataset used in this project is the **BIO-CE-GN** network, obtained from the [Network Repository](https://networkrepository.com/bio-ce-gn.php).  
It represents a **biological neural connectivity network** (Celegans) where:
- **Nodes** represent neurons  
- **Edges** represent synaptic connections between neurons  
- The network is **directed** and **weighted**

### Dataset Information:
- **Number of Nodes:** 2,975  
- **Number of Edges:** 54,990  
- **Maximum Degree:** 242  
- **Average Degree:** 48  
- **Size:** ~512 KB  

---

## **Source (Citation)**
For the dataset:  
> Ryan A. Rossi and Nesreen K. Ahmed,  
> *The Network Data Repository with Interactive Graph Analytics and Visualization*,  
> AAAI, 2015.  
> [https://networkrepository.com](https://networkrepository.com)

---

## **Objectives**
The main goal of this project is to study the **structure and properties** of the biological network, and to compare the results with typical features observed in real-world biological systems.

Specifically, we aim to:
1. Compute **basic graph properties** (size, degree distribution, connectivity, density)  
2. Calculate **centrality measures** (degree, closeness, betweenness)  
3. Analyse **clustering coefficient** and **community structure**  
4. Optionally, explore **motifs** and **biological relevance** of network patterns  ??

---

## **Methodology**
The project will use **Python** and the **NetworkX** package to:
- Load and process the graph dataset  
- Perform topological analysis  
- Generate visualizations  
- Store computed metrics in structured outputs (JSON, CSV, PNG)

All analyses and experiments will be performed on local machines using Jupyter Notebook or Python scripts.

---

## **Instructions to Replicate Experiments**

To reproduce the results, follow these steps:

1. **Download the dataset:**  
   From [https://networkrepository.com/bio-ce-gn.php](https://networkrepository.com/bio-ce-gn.php)

2. **Extract** the dataset into the `data/` directory.  

3. **Install dependencies:**  
   ```bash
   pip install -r requirements.txt


## **Results**
