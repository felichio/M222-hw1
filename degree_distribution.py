import collections
import matplotlib.pyplot as plt
import networkx as nx


def plot_degree_distribution(G):
  degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
  # print "Degree sequence", degree_sequence
  degreeCount = collections.Counter(degree_sequence)
  deg, cnt = zip(*degreeCount.items())

  fig, ax = plt.subplots(1, 2)
  ax[0].bar(deg, cnt, width=0.8, color='b')

  ax[0].set_title("Degree Histogram")
  ax[0].set_ylabel("Count")
  ax[0].set_xlabel("Degree")
  ax[0].set_xticks([d  for d in deg])
  ax[0].set_xticklabels(deg)

  # draw graph in inset
  # plt.axes([0.4, 0.4, 0.5, 0.5])
  # Gcc = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True)[0])
  pos = nx.spring_layout(G)
  plt.axis('off')
  nx.draw_networkx_nodes(G, pos, node_size=20)
  nx.draw_networkx_labels(G, pos, font_size=7)
  nx.draw_networkx_edges(G, pos, alpha=0.4)

  plt.show()

