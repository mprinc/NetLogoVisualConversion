python src/convert.py --phase convert --filein "data/examples/NetLogo/netlogo world - cliques.csv" --fileout "data/examples/Gephi/conversions/converted - netlogo world - cliques.graphml"

python src/convert.py --phase convert --node_size_multiplyer 5 --edge_weight_multiplyer 3 --edge_weight_ignore true --coord_multiplyer 10 \
    --node-name-prefix "N_" --filein "data/examples/NetLogo/netlogo world - cliques.csv" \
    --fileout "data/examples/Gephi/conversions/converted - netlogo world - cliques.graphml"

python src/convert.py --phase convert --node_size_multiplyer 5 --edge_weight_multiplyer 3 --edge_weight_ignore true --coord_multiplyer 10 \
    --node-name-prefix "N_" --filein "data/examples/NetLogo/netlogo world - SmallWorldWS.csv" \
    --fileout "data/examples/Gephi/conversions/converted - netlogo world - SmallWorldWS.graphml"

WHY
---------
- recover all parameters of your netlogo world in Gephi
    - turtles -> nodes
    - links -> edges
    - nodes positions are preserved
        - you can keep and observe a specific topology that is created through NetLogo model
    - nodes sizes and colors are preserver
        - it is very usefull if they reflect some internal network characteristics
    - edge weights are preserved
    - breeds of turtles and edges are preserved
        - you can use that to encode special node/edges characteristics, like opinions, or type of connections between nodes, etc
- igraph model
    - if you did a bit of programmming you can extend script and play with intermediate igraph model that we go through before exporting to GraphML document
- transition parameters
    - nodes sizes scaling
    - nodes positions scalling
    - edges weights scaling
    - ignoring edge weight
    - prefixing node names

Nice to have?
-------------------------
- GraphML -> NetLogo
- NetLogo time -> GraphML dynamic