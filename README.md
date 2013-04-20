**NetLogoVisualConversion** is a tool (written in Python 2.7) that helps you to use your [NetLogo](http://ccl.northwestern.edu/netlogo/) created networks in many Network Visualizing tools (like [Gephi](http://gephi.org/), [Guess](http://graphexploration.cond.org/) or similar)

Outpot of script is a [GraphML](http://graphml.graphdrawing.org/) format script that you can immediatelly import to your favourit visualization model and continue processing, calculation metrics or visualization of course :) 

=== Other solutions

There is a way to export your NetLogo network through [nw netlogo extension](https://github.com/NetLogo/NetLogo/wiki/Extensions#nw-network-extension), but there are many reasons why it doesn't do acceptable enough work:
* you need to know NetLogo and be invisive to NetLogo model in order to export network
* position of turtles/nodes is "random"
* colors are not preserved
* additional parameters stored in turtles, links are not preserved
* etc

## WHY

Here are some reasons why you want to use _NetLogoVisualConversion_ script:

* **recover all parameters** of your netlogo world in Gephi
    * turtles -> nodes
    * links -> edges
    * **nodes positions** are preserved
        * you can keep and observe a specific topology that is created through your NetLogo model
    * **nodes sizes** and **node colors** are preserved
        * it is very usefull if they **reflect** some internal network characteristics
    * **edge weights** are preserved
    * **breeds** of turtles and edges are preserved
        * you can use that to encode special node/edges **characteristics**, like node opinions, or type of connections between nodes, etc
* **intermediate igraph model**
    * if you do a bit more of Python programmming, you can extend script and play with intermediate igraph model that we go through before exporting to **GraphML** document
* **translation parameters**
    * **nodes sizes** scaling
    * **nodes positions** scalling
    * **edges weights** scaling
    * **ignoring edge weight**
    * **prefixing node names**

### Nice to have features?

If you think that features from the following list would be nice to have, please let me know

* **GraphML -> NetLogo**
    * support for importing GraphML model into NetLogo
    * You might need it if you have a complex network that you want to start your simmulation with 
* **NetLogo over time/ticks -> dynamic (longitudinal) netowrk**
    * it will track your network (turtles+links) changes over time and record it into dynamic network that you can visualize/animate in Gephi, etc
* **Real-time visualizing of currently running NetLogo model in Gephi** (or other compatible tool)
    * it will provide a way to make a real-time connection between running NetLogo model and Gephi
    * any change hapening in NetLogo would in the real time update in your graph in Gephi 
    * Ask for this if you REALY, REALY need it, and please
    * Eplain why do you need it :)

please do:

* Let me know you would benefite from it and I will try to make it
* [fork this project](https://github.com/mprinc/NetLogoVisualConversion/fork) and do work on your on and later ask me to merge
* use this code to make something new

## Instructions

### Prerequisites

You need to have:
1.[NetLogo](http://ccl.northwestern.edu/netlogo/), unless you have NetLogo world already exported
2. [Python 2.7](http://www.python.org/getit/) installed, it should work with Python 3 as well
3. [iGraph package](http://igraph.sourceforge.net/)

### Conversion

You can download script by clicking on **ZIP** button on the top of the page or simple following the link:

[Download link](https://github.com/mprinc/NetLogoVisualConversion/archive/master.zip)

after downloading NetLogoVisualConversion tool
1. unpack it
2. go to shell and 
3. navigate to the folder containing unpacked tool

run the tool in the following way:

`python src/convert.py --help`

You will see a list of parameters you can provide.

## Examples

If you run the tool in the following way:

`python src/convert.py --help`

You will see a list of parameters you can provide.

(NOTE: If you would benefit from some other parameter, please let me know)

If you run it simply as `python src/convert.py` you will get first missing parameter and so on, as long as there are missing parameters :)

Here are some examples of calling script:

```bash
`python src/convert.py --phase convert --filein "data/examples/NetLogo/netlogo world - cliques.csv" \
    --fileout "data/examples/Gephi/conversions/converted - netlogo world - cliques.graphml"
```
converts (`--phase convert`) NetLogo network *"data/examples/NetLogo/netlogo world - cliques.csv"* into *"data/examples/Gephi/conversions/converted - netlogo world - cliques.graphml"*

```bash
python src/convert.py --phase convert --node_size_multiplyer 5 --edge_weight_multiplyer 3 --coord_multiplyer 10 \
    --node-name-prefix "N_" --filein "data/examples/NetLogo/netlogo world - cliques.csv" \
    --fileout "data/examples/Gephi/conversions/converted - netlogo world - cliques.graphml"
```

converts NetLogo network *"data/examples/NetLogo/netlogo world - cliques.csv"* into *"data/examples/Gephi/conversions/converted - netlogo world - cliques.graphml"* with few modifications:
* `--node-name-prefix "N_"` adds the **N_** prefix to each node name
* `--node_size_multiplyer 5` multiplies the size of each node by 5
* ` --edge_weight_multiplyer 3` multiplies the weight of each edge by 3
* ` --coord_multiplyer 10` multiplies the X and Y coordinate (scale up) of each node by 10

```bash
python src/convert.py --phase convert --node_size_multiplyer 5 --edge_weight_ignore true --coord_multiplyer 10 \
    --node-name-prefix "N_" --filein "data/examples/NetLogo/netlogo world - SmallWorldWS.csv" \
    --fileout "data/examples/Gephi/conversions/converted - netlogo world - SmallWorldWS.graphml"
```

Similar to the previous example except that it use different files and by
*  `--edge_weight_ignore true` removes edge weight in resulting graph

Please check in `python src/convert.py --help` for all other parameters.