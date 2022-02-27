import networkx as nx
import pandas as pd
import degree_distribution
 
# read all the 5 csv files
# keep only the distinct pairs of source target since we will ignore the books and the weights
 
# all_books = ["book1.csv", "book2.csv", "book3.csv", "book4.csv", "book5.csv"]
all_books = ["stack_network_links.csv"]

li = []
 
for f in all_books:
    tmp = pd.read_csv(f)
    li.append(tmp)
 
df = pd.concat(li, axis=0, ignore_index=True)
 
df = df[['source', 'target']]
df.drop_duplicates(subset=['source', 'target'], inplace=True)

#print(df.head(20))
 
# create the ASOIAF networkx object
G = nx.from_pandas_edgelist(df,  source='source', target='target')

# create a random graph networkx object
#G = nx.erdos_renyi_graph(len(G.nodes()), 2*len(G.edges())/(len(G.nodes())*(len(G.nodes())-1)))
#G = nx.watts_strogatz_graph(len(G.nodes()), 7, 0.3)

print("\nNumber of nodes: %d" % len(G.nodes()))
 
print("\nNumber of edges: %d" % len(G.edges()))

graphs = list([G.subgraph(c) for c in nx.connected_components(G)])
print("\nConnected components: %d" % (len(graphs)))
for i, g in enumerate(graphs):
    print("\nComponent-%d" % i)
    print("\tSize: %d" % len(g.nodes()))
    print("\tAverage shortest path: %f" % nx.average_shortest_path_length(g))
    print("\tDiameter: %d" % nx.diameter(g))

print("\n\nAverage clustering coefficient: %f\n" % nx.average_clustering(G))

for g in graphs:
    degree_distribution.plot_degree_distribution(g)


