import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# === CONFIG ============================================================== 

DATA_PATH = Path("data/bio-CE-GN.edges")

# Se volete considerare il grafo diretto metti True
DIRECTED = False

# Se il grafo è enorme puoi mettere False per usare una betweenness approssimata
EXACT_BETWEENNESS = True


# === LOADING & PREPROCESSING ============================================ #

def load_graph():
    """
    Load the BIO-CE-GN network from an edge list file.
    Expected format: each line 'u v' oppure 'u v weight'.
    """
    if DIRECTED:
        G = nx.read_edgelist(
            DATA_PATH,
            create_using=nx.DiGraph(),
            nodetype=str,
            data=(("weight", float),),
        )
    else:
        G = nx.read_edgelist(
            DATA_PATH,
            create_using=nx.Graph(),
            nodetype=str,
            data=(("weight", float),),
        )
    return G


def preprocess_graph(G: nx.Graph) -> nx.Graph:
    """
    Remove self-loops and collapse possible multi-edges.
    """
    # rimuovi self-loop
    G.remove_edges_from(nx.selfloop_edges(G))

    # se fosse MultiGraph, trasformalo in grafo semplice
    if isinstance(G, (nx.MultiGraph, nx.MultiDiGraph)):
        if DIRECTED:
            G = nx.DiGraph(G)
        else:
            G = nx.Graph(G)

    return G


# === BASIC STATS ======================================================== #

def compute_basic_stats(G: nx.Graph):
    degrees = dict(G.degree())
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    avg_degree = sum(degrees.values()) / num_nodes if num_nodes > 0 else 0.0
    density = nx.density(G)

    stats = {
        "directed": G.is_directed(),
        "num_nodes": num_nodes,
        "num_edges": num_edges,
        "avg_degree": avg_degree,
        "density": density,
        "num_connected_components": nx.number_connected_components(G)
        if not G.is_directed()
        else None,
    }
    return stats, degrees


# === CENTRALITIES & CORRELATION ======================================== #

def compute_centralities(G: nx.Graph) -> pd.DataFrame:
    """
    Compute degree, betweenness and PageRank centralities
    and return them as a pandas DataFrame indexed by node id.
    """
    print("Computing degree centrality...")
    degree_c = nx.degree_centrality(G)

    print("Computing betweenness centrality...")
    if EXACT_BETWEENNESS:
        betw_c = nx.betweenness_centrality(G, normalized=True)
    else:
        # approssimazione (più veloce)
        betw_c = nx.betweenness_centrality(G, k=100, normalized=True, seed=42)

    print("Computing PageRank...")
    pagerank_c = nx.pagerank(G)

    df = pd.DataFrame(
        {
            "degree": pd.Series(degree_c),
            "betweenness": pd.Series(betw_c),
            "pagerank": pd.Series(pagerank_c),
        }
    )

    return df


def compute_correlation(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute Pearson correlation matrix between centrality measures.
    """
    corr = df.corr(method="pearson")
    return corr

def plot_distributions(centralities: pd.DataFrame):
    """
    Plot simple histograms for each centrality measure and save them as PNG.
    """
    plots_dir = Path("results") / "plots"
    plots_dir.mkdir(exist_ok=True, parents=True)

    for col in centralities.columns:
        values = centralities[col].values

        plt.figure()
        plt.hist(values, bins=50)
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.title(f"Distribution of {col} centrality")
        plt.tight_layout()
        plt.savefig(plots_dir / f"{col}_distribution.png")
        plt.close()
        
# === SAVING RESULTS ===================================================== #

def save_results(stats: dict, centralities: pd.DataFrame, corr: pd.DataFrame):
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)

    # 1) statistiche di base
    basic_stats_path = results_dir / "basic_stats.txt"
    with basic_stats_path.open("w") as f:
        for k, v in stats.items():
            f.write(f"{k}: {v}\n")

    # 2) centralità per ogni nodo
    centralities_path = results_dir / "centralities.csv"
    centralities.to_csv(centralities_path, index_label="node")

    # 3) matrice di correlazione
    corr_path = results_dir / "centrality_correlation.csv"
    corr.to_csv(corr_path)

    # 4) top 20 nodi per ogni centralità (utile per il midterm)
    top_dir = results_dir / "top_nodes"
    top_dir.mkdir(exist_ok=True)

    for col in centralities.columns:
        top = (
            centralities[[col]]
            .sort_values(by=col, ascending=False)
            .head(20)
        )
        top.to_csv(top_dir / f"top20_{col}.csv", index_label="node")

    print(f"Saved results to '{results_dir}/'.")


# === MAIN =============================================================== #

def main():
    print("Loading graph...")
    G = load_graph()

    print("Preprocessing graph...")
    G = preprocess_graph(G)

    print("Computing basic stats...")
    stats, _ = compute_basic_stats(G)
    print("Basic stats:", stats)

    print("Computing centralities...")
    centralities = compute_centralities(G)

    print("Computing correlation matrix...")
    corr = compute_correlation(centralities)
    
    print("Plotting centrality distributions...")
    plot_distributions(centralities)

    print("Saving results...")
    save_results(stats, centralities, corr)

    print("Done.")


if __name__ == "__main__":
    main()
