<p align = "center"><img src = "https://user-images.githubusercontent.com/74304423/146420213-3c28708b-2a6c-479f-bb83-84ea747c3944.png">  </p>

<p>
<h2>  Project review</h2>
Graph calculator is a simple program that can create, load(via JSON file) , and edit directed weighted graphs. After receiving/loading a graph from a JSON file it can be used as the basis for many graph operations, such as finding the shortest path between two nodes, finding the center, etc...<br>
The manipulated graph can be saved to json file.
</p>

<h2> Algorithms </h2>


 <ul>
  
  <li> <strong>Shortest path: </strong>We call Dijkstra's algorithm on the source node, fetch the parents array it returns, and use it to calculate the path to the destination vertex Then, using backtracking we construct the path between these two nodes. </li>
  <li> <strong> Center: </strong>The implementation is rather simple, we first compute the eccentricity of each node <a href="https://en.wikipedia.org/wiki/Distance_(graph_theory)">(eccentricity:wikipedia) </a> using Dijkstra's algorithm on each vertex and taking the max distance. then, we  pick the vertex with the smallest eccentricy as the center</li>
  
  <li> <strong> Tsp-Traveling salesmen problem: </strong> We start from some random node from the list, perform the Dijkstra algorithm, and travel to the closest Unvisited node from the list, we keep doing that until we reached all the nodes from the list. following this method will yield us a valid path, albeit not necessarily the shortest. we repeat this process for each node in the list, each time picking another vertex as a starting point. in the end we return the shortest path we've found</li>  

 <h3> DIjkstra's shortest path algorithm</h3>
 <p>
  Dijkstra's algorithm played a major part in our work, being part of every algorithm. After our first implementation of the algorithm (using regular priority queue) proved to be too slow for our purposes, we implemented it again using python's min heap Queue library - heapq.
Using the new implementation and after little bit of profiling, we managed to  greatly improve our running time.
 </p>


 <h2> UML diagram </h2>
 <br>
 <p align = "center"><img src = "https://user-images.githubusercontent.com/74304423/146753790-d87e99b6-1ebc-4b13-848d-61780a15cbf5.jpg">  </p>
 
 
 <h2> How to run the project </h2>
 
 First, download/clone the project from git. 
Afterwards do the following:
- Extract the downloaded zip file, and open the project in Python environment workspace (VERY IMPORTANT TO DOWNLOAD THE LIBRARY "MATPLOTLIB").
- In class "main" you run the project itself as described:
  - There are 4 check functions that are already in the project. you can change each one of them as you desire, 
  or to create a new check function.
  - example of a check function:
 
 ![1](https://user-images.githubusercontent.com/93203695/147487620-605869a2-5c94-4f9b-a703-b530457ba76c.png)

  - To upload a graph from a Json file do the following: 
    - Init an empty graph - for the GraphAlgo:
 
 <p align = "center"><img src = "https://user-images.githubusercontent.com/93203695/147488000-0f1f1c60-4e54-4729-9d4b-2e632224e317.png"> </p>
 
    - Write the path to where the file is at:
 
 <p align = "center"><img src = "https://user-images.githubusercontent.com/93203695/147488127-85596b74-875a-4a0d-a998-ee172b1ec78d.png">  </p>
 
    - Init a GraphAlgo from a json file: 
 
 <p align = "center"><img src = "https://user-images.githubusercontent.com/93203695/147488308-032f2c37-c6f0-4dd3-9497-221dcb3473ec.png">  </p>

  - To create a graph (not via upload), do the following:
    - Create an empty directed graph:
 
 <p align = "center"><img src = "https://user-images.githubusercontent.com/93203695/147488448-1e232ce8-eaad-4a9f-86f7-9ed2400a6231.png">  </p>
    - Insert the nodes and edges you desire, as in the example:
 
 <p align = "center"><img src = "https://user-images.githubusercontent.com/93203695/147488627-1d32d42d-16f6-4a77-92b6-2089841a0dd4.png">  </p>

 To run the algorithms, just call the algorithm function that you would like to activate,
 inside a print call, so you will get the answer of the algorithm.
 - Example: Here we call the algorithm "shortest path"
 
 <p align = "center"><img src = "https://user-images.githubusercontent.com/93203695/147490162-c4273dd2-c38c-4757-b678-0e48b137a95e.png">  </p>

 To run changes on the graph, call the function that you would like to,
 and don't forget to call right afterwards to the function plot_graph() in order to see the changes.
 - Example: first picture shows the graph before the changes, the second shows the graph after we called the function "remove edge":
 
 ![before](https://user-images.githubusercontent.com/93203695/147489593-26cea9b3-67db-4f0a-92ce-b90aefd78a96.png)

 ![after](https://user-images.githubusercontent.com/93203695/147489602-17563019-04e7-4837-b414-d72ffe73c451.png)

 Example of how to write the changes and plotting the graph:
 
 ![changes](https://user-images.githubusercontent.com/93203695/147489633-0261f345-3a69-402a-bd51-80f5516ce82f.png)

 
   
 <h2> Visual representation </h2>
Some examples of graphs visualizations:
<h3> Graph A0: </h3>
 
![Figure_1](https://user-images.githubusercontent.com/93203695/147485865-6c30dac7-429d-43d5-ae08-988effedcd5c.png)


<h3> Graph A5: </h3>
 
 ![Figure_6](https://user-images.githubusercontent.com/93203695/147486227-370eaf71-3b21-475a-b074-08c6f0a64708.png)
