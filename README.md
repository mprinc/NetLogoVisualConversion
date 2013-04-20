*## Introduction

*NetLogoVisualConversion** is a tool (written in Python 2.7) that helps you to use your [NetLogo](http://ccl.northwestern.edu/netlogo/) created networks in many Network Visualizing tools (like [Gephi](http://gephi.org/), [Guess](http://graphexploration.cond.org/) or similar)

Outpot of script is a [GraphML](http://graphml.graphdrawing.org/) format script that you can immediatelly import to your favourit visualization model and continue processing, calculation metrics or visualization of course :) 

### Other solutions

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

1. [NetLogo](http://ccl.northwestern.edu/netlogo/), unless you have NetLogo world already exported
2. [Python 2.7](http://www.python.org/getit/) installed, it should work with Python 3 as well
3. [iGraph package](http://igraph.sourceforge.net/)

### NetLogo Export

Exporting NetLogo World from NetLogo is straight forward:

1. Open NetLogo
2. Load NetLogo model
3. Execute it and stop in the moment you want to take snapshopt
4. Go to the menu and choose: File > Export > Export world ...
5. Save file
    1. The best place to save your file is into the data folder of the folder containing the **NetLogoVisualConversiontool** tool
    2. If you stored it to the ***data*** folder and named it `world.csv` then you can convert it by passing ` --filein "data/world.csv"` to the tool

### Conversion

You can download the **NetLogoVisualConversiontool** tool by clicking on the **ZIP** button on the top of the page or simple following the link:

[Download link](https://github.com/mprinc/NetLogoVisualConversion/archive/master.zip)

after downloading NetLogoVisualConversion tool
1. unpack it
2. go to shell and 
3. navigate to the folder containing unpacked tool (stay in it, do not go to the src folder)

run the tool in the following way:

`python src/convert.py --help`

You will see a list of parameters you can provide.

### Import in Gephi

1. Start Gephi
2. Choose import from menu: File > Open ...
    1. Choose file you want to import
    2. Unselect **Auto-scale** checkbox (otherwise node sizes will be lost, etc)

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

Here are the conversion instructions for the rest of netlogo world examples you can find in `data/examples/NetLogo/` folder.

```bash
python src/convert.py --phase convert --node_size_multiplyer 5 --edge_weight_multiplyer 3 --coord_multiplyer 10 \
    --node-name-prefix "N_" --filein "data/examples/NetLogo/netlogo world - OpinionFormationModelToy.csv" \
    --fileout "data/examples/Gephi/conversions/converted - netlogo world - OpinionFormationModelToy.graphml"
```

```bash
python src/convert.py --phase convert --node_size_multiplyer 5 --edge_weight_ignore true --coord_multiplyer 10 \
    --node-name-prefix "N_" --filein "data/examples/NetLogo/netlogo world - RandomGraphs-static-geo.csv" \
    --fileout "data/examples/Gephi/conversions/converted - netlogo world - RandomGraphs-static-geo.graphml"
```

```bash
python src/convert.py --phase convert --node_size_multiplyer 5 --edge_weight_ignore true --coord_multiplyer 10 \
    --node-name-prefix "N_" --filein "data/examples/NetLogo/netlogo world - RandomGraphs-rand-encounter.csv" \
    --fileout "data/examples/Gephi/conversions/converted - netlogo world - RandomGraphs-rand-encounter.graphml"
```

Please check in `python src/convert.py --help` for all other parameters.

## Screenshoots

### Small Worlds Model

NetLogo model:

![NetLogo model](https://dl.dropboxusercontent.com/u/4976813/tools/NetLogoVisualConversion/NetLogo%20-%20SmallWorldWS.png "NetLogo Small Worlds model")

is converted into:

![Gephi graph](https://dl.dropboxusercontent.com/u/4976813/tools/NetLogoVisualConversion/Gephi%20-%20SmallWorldWS.png "Gephi Small Worlds model")

This model and documentation was adapted by Eytan Bakshy and Lada Adamic from:  Wilensky, U. (2005).  NetLogo Small Worlds model.  http://ccl.northwestern.edu/netlogo/models/SmallWorlds.  Center for Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL.

### RandomGraphs (Static-Geo)

NetLogo model:

![NetLogo model](https://dl.dropboxusercontent.com/u/4976813/tools/NetLogoVisualConversion/NetLogo%20-%20SmallWorldWS.png "NetLogo RandomGraphs (Static-Geo) model")

is converted into:

![Gephi graph](https://dl.dropboxusercontent.com/u/4976813/tools/NetLogoVisualConversion/NetLogo%20-%20RandomGraphs-static-geo.png "Gephi RandomGraphs (Static-Geo) model")

#### COPYRIGHT AND LICENSE

This model was adapted by Lada Adamic from Uri Wilensky's Giant Component model in NetLogo's models library http://ccl.northwestern.edu/netlogo/models/GiantComponent.

![CC BY-NC-SA 3.0](http://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png)

This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 License.  To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/ or send a letter to Creative Commons, 559 Nathan Abbott Way, Stanford, California 94305, USA.

### RandomGraphs (Rand-Encounter)

NetLogo model:

![NetLogo model](https://dl.dropboxusercontent.com/u/4976813/tools/NetLogoVisualConversion/NetLogo%20-%20RandomGraphs-rand-encounter.png "NetLogo RandomGraphs (Rand-Encounter) model")

is converted into:

![Gephi graph](https://dl.dropboxusercontent.com/u/4976813/tools/NetLogoVisualConversion/Gephi%20-%20RandomGraphs-rand-encounter.png "Gephi RandomGraphs (Rand-Encounter) model")

or after applying ForceAtlas 2 layout:

![Gephi graph](https://dl.dropboxusercontent.com/u/4976813/tools/NetLogoVisualConversion/Gephi%20-%20RandomGraphs-rand-encounter%20-%20Forced.png "Gephi RandomGraphs (Rand-Encounter) model - Forced")

#### COPYRIGHT AND LICENSE

This model was adapted by Lada Adamic from Uri Wilensky's Giant Component model in NetLogo's models library http://ccl.northwestern.edu/netlogo/models/GiantComponent.

![CC BY-NC-SA 3.0](http://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png)

This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 License.  To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/ or send a letter to Creative Commons, 559 Nathan Abbott Way, Stanford, California 94305, USA.

### Opinion Formation

NetLogo model:

![NetLogo model](https://dl.dropboxusercontent.com/u/4976813/tools/NetLogoVisualConversion/NetLogo%20-%20OpinionFormationModelToy.png "NetLogo RandomGraphs (Rand-Encounter) model")

is converted into:

![Gephi graph](https://dl.dropboxusercontent.com/u/4976813/tools/NetLogoVisualConversion/Gephi%20-%20OpinionFormationModelToy.png "Gephi RandomGraphs (Rand-Encounter) model")

## CREDITS AND REFERENCES

Created by Lada Adamic 2008
