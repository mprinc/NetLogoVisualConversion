<img src="http://cl.ly/image/272q3f1u313b/Rendr-logotype.png" width="395" height="100">

[Backbone.js](http://backbonejs.org/) apps seamlessly on both the client and the server. Allow your web server to serve fully-formed HTML pages to any deep link of your app, while preserving the snappy feel of a traditional Backbone.js client-side MVC app.


Build status: [![travis-ci status](https://secure.travis-ci.org/airbnb/rendr.png)](http://travis-ci.org/#!/airbnb/rendr/builds)

## Base classes

### `BaseView`

#### Public methods


The default implementation returns something reasonable: essentially `view.model.toJSON()` or `{models: view.collection.toJSON()}`. 

```js
var MyView = BaseView.extend({
  getTemplateData: function() {
  }
});
```

#### Methods you can override for custom view behaviors

*Environment: shared.*


## WHY
* recover all parameters of your netlogo world in Gephi
** turtles -> nodes
** links -> edges
** nodes positions are preserved
*** you can keep and observe a specific topology that is created through NetLogo model
** nodes sizes and colors are preserver
*** it is very usefull if they reflect some internal network characteristics
** edge weights are preserved
** breeds of turtles and edges are preserved
*** you can use that to encode special node/edges characteristics, like opinions, or type of connections between nodes, etc
* igraph model
** if you did a bit of programmming you can extend script and play with intermediate igraph model that we go through before exporting to GraphML document
* transition parameters
** nodes sizes scaling
** nodes positions scalling
** edges weights scaling
** ignoring edge weight
** prefixing node names

=== Nice to have features?
If you think that features from the following list would be nice to have, please let me know
* GraphML -> NetLogo
* NetLogo time -> GraphML dynamic

## Examples
python src/convert.py --phase convert --filein "data/examples/NetLogo/netlogo world - cliques.csv" --fileout "data/examples/Gephi/conversions/converted - netlogo world - cliques.graphml"

python src/convert.py --phase convert --node_size_multiplyer 5 --edge_weight_multiplyer 3 --edge_weight_ignore true --coord_multiplyer 10 \
    --node-name-prefix "N_" --filein "data/examples/NetLogo/netlogo world - cliques.csv" \
    --fileout "data/examples/Gephi/conversions/converted - netlogo world - cliques.graphml"

python src/convert.py --phase convert --node_size_multiplyer 5 --edge_weight_multiplyer 3 --edge_weight_ignore true --coord_multiplyer 10 \
    --node-name-prefix "N_" --filein "data/examples/NetLogo/netlogo world - SmallWorldWS.csv" \
    --fileout "data/examples/Gephi/conversions/converted - netlogo world - SmallWorldWS.graphml"