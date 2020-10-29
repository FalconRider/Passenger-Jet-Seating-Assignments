# Copyright 2019 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.






#Project : Jet Seating Assignments Project                                       ***

import datetime
import networkx as nx
import dwave_networkx as dnx

import matplotlib.pyplot as plt
from dwave.system.samplers import DWaveSampler

from dwave.system.composites import EmbeddingComposite

sampler = EmbeddingComposite(DWaveSampler())
timestamp = datetime.datetime.now()


G = nx.Graph()

#CONSTRAINTS
# 3 x 30 rows. Used generator.
                                                    
G.add_edges_from ([(1, 2 ),(2, 3 ),(3, 4 ),(4, 5 ),(5, 6 ),(6, 7 ),(7, 8 ),(8, 9 ),(9, 10 ),(10, 11 ),(11, 12 ),(12, 13 ),(13, 14 ),(14, 15 ),(15, 16 ),(16, 17 ),(17, 18 ),(18, 19 ),(19, 20 ),(20, 21 ),(21, 22 ),(22, 23 ),(23, 24 ),(24, 25 ),(25, 26 ),(26, 27 ),(27, 28 ),(28, 29 ),(29, 30 ),(31, 32 ),(32, 33 ),(33, 34 ),(34, 35 ),(35, 36 ),(36, 37 ),(37, 38 ),(38, 39 ),(39, 40 ),(40, 41 ),(41, 42 ),(42, 43 ),(43, 44 ),(44, 45 ),(45, 46 ),(46, 47 ),(47, 48 ),(48, 49 ),(49, 50 ),(50, 51 ),(51, 52 ),(52, 53 ),(53, 54 ),(54, 55 ),(55, 56 ),(56, 57 ),(57, 58 ),(58, 59 ),(59, 60 ),(1, 31 ),(2, 32 ),(3, 33 ),(4, 34 ),(5, 35 ),(6, 36 ),(7, 37 ),(8, 38 ),(9, 39 ),(10, 40 ),(11, 41 ),(12, 42 ),(13, 43 ),(14, 44 ),(15, 45 ),(16, 46 ),(17, 47 ),(18, 48 ),(19, 49 ),(20, 50 ),(21, 51 ),(22, 52 ),(23, 53 ),(24, 54 ),(25, 55 ),(26, 56 ),(27, 57 ),(28, 58 ),(29, 59 ),(30, 60 ),(1, 32 ),(2, 33 ),(3, 34 ),(4, 35 ),(5, 36 ),(6, 37 ),(7, 38 ),(8, 39 ),(9, 40 ),(10, 41 ),(11, 42 ),(12, 43 ),(13, 44 ),(14, 45 ),(15, 46 ),(16, 47 ),(17, 48 ),(18, 49 ),(19, 50 ),(20, 51 ),(21, 52 ),(22, 53 ),(23, 54 ),(24, 55 ),(25, 56 ),(26, 57 ),(27, 58 ),(28, 59 ),(29, 60 ),(2, 31 ),(3, 32 ),(4, 33 ),(5, 34 ),(6, 35 ),(7, 36 ),(8, 37 ),(9, 38 ),(10, 39 ),(11, 40 ),(12, 41 ),(13, 42 ),(14, 43 ),(15, 44 ),(16, 45 ),(17, 46 ),(18, 47 ),(19, 48 ),(20, 49 ),(21, 50 ),(22, 51 ),(23, 52 ),(24, 53 ),(25, 54 ),(26, 55 ),(27, 56 ),(28, 57 ),(29, 58 ),(30, 59 ),(61, 62 ),(62, 63 ),(63, 64 ),(64, 65 ),(65, 66 ),(66, 67 ),(67, 68 ),(68, 69 ),(69, 70 ),(70, 71 ),(71, 72 ),(72, 73 ),(73, 74 ),(74, 75 ),(75, 76 ),(76, 77 ),(77, 78 ),(78, 79 ),(79, 80 ),(80, 81 ),(81, 82 ),(82, 83 ),(83, 84 ),(84, 85 ),(85, 86 ),(86, 87 ),(87, 88 ),(88, 89 ),(89, 90 ),(31, 61 ),(32, 62 ),(33, 63 ),(34, 64 ),(35, 65 ),(36, 66 ),(37, 67 ),(38, 68 ),(39, 69 ),(40, 70 ),(41, 71 ),(42, 72 ),(43, 73 ),(44, 74 ),(45, 75 ),(46, 76 ),(47, 77 ),(48, 78 ),(49, 79 ),(50, 80 ),(51, 81 ),(52, 82 ),(53, 83 ),(54, 84 ),(55, 85 ),(56, 86 ),(57, 87 ),(58, 88 ),(59, 89 ),(60, 90 ),(31, 62 ),(32, 63 ),(33, 64 ),(34, 65 ),(35, 66 ),(36, 67 ),(37, 68 ),(38, 69 ),(39, 70 ),(40, 71 ),(41, 72 ),(42, 73 ),(43, 74 ),(44, 75 ),(45, 76 ),(46, 77 ),(47, 78 ),(48, 79 ),(49, 80 ),(50, 81 ),(51, 82 ),(52, 83 ),(53, 84 ),(54, 85 ),(55, 86 ),(56, 87 ),(57, 88 ),(58, 89 ),(59, 90 ),(32, 61 ),(33, 62 ),(34, 63 ),(35, 64 ),(36, 65 ),(37, 66 ),(38, 67 ),(39, 68 ),(40, 69 ),(41, 70 ),(42, 71 ),(43, 72 ),(44, 73 ),(45, 74 ),(46, 75 ),(47, 76 ),(48, 77 ),(49, 78 ),(50, 79 ),(51, 80 ),(52, 81 ),(53, 82 ),(54, 83 ),(55, 84 ),(56, 85 ),(57, 86 ),(58, 87 ),(59, 88 ),(60, 89 )])
#
#


                
S = dnx.maximum_independent_set(G, sampler=sampler, num_reads = 10)

                  

#   adjust your  printout requirments ---------------REPORT---------***

print(" ")
print("--------------------------------------------------------------")
print("Jet Seating Assignments")
print("Run                             ",timestamp)
print("--------------------------------------------------------------")
print("Total avaiable seats - nodes  90 in each section "),
print("Maximum  set size     ", len (S))
print("Missed ", 90 -len(S))
print("Assignments in Nodes this run   ",S)
print("--------------------------------------------------------------")
print(" ")


#GRAPH

k =G.subgraph(S)
notS =list(set(G.nodes())-set(S))
othersubgraph = G.subgraph(notS)
pos = nx.spring_layout(G)
plt.figure()
nx.draw(G,pos=pos)
nx.draw(k,pos=pos)
nx.draw(othersubgraph,pos=pos,node_color ='b')
plt.show()
