osmpal-nodes-basic
==================

OpenStreetMap tool to find nearest and farthest nodes from .osm file



About this Program:
===================

OSM Nodes Basic is a lightweight  OpenStreetMap tool to find nearest and farthest nodes from .osm file. This is the text-version python tool. If you want a graphical display of the nodes, try https://github.com/developingcountries/osmpal-nodes-graphical

Installation:
=============

1.  Download the code with your web browser or git clone https://github.com/developingcountries/osmpal-nodes-basic 

2.  Use a text editor to edit line 5 in the file osmpalnodesbasic.py file  
 Line 5 SHOULD POINT TO THE LOCATION OF the pyosm.py library file, e.g. '/home/peter/osmpal/lib/')  This points to the pyosm.py library file that parses the OpenStreetMap data. 

3.  To use this application, you will also need to download an .osm data file, which has the map data.   A good source is at http://metro.teczno.com/ Download and save an .osm file to your working directory, e.g. /home/peter/osmpal/new-york.osm   NOTE: the other Openstreetmap data formats like .pbf will not work--it has to be .osm format file. 
 Now, use your text editor again and edit Line 8 of the osmpalnodesbasic.py file with the location of the .osm map data file, e.g.
osm = pyosm.OSMXMLFile('/home/peter/osmpal/new-york.osm') 

4.  Run this tool and check for the nearest or farthest node. To get the farthest node in Ubuntu Linux, go into the command line and type:
python -c 'import osmpalnodesbasic; osmpalnodesbasic.farthest_node(299046361)'  
Or, you can type python -c 'import osmpalnodesbasic; osmpalnodesbasic.nearest_node(299046361)' to get the nearest point to this node in Time Square. 

5.  Use a similar command in Mac Python or Windows python. The part inside the brackets of osmpalnodesbasic.farthest_node(299046361) is where you enter the node number that you want to check.  In our example, this will give you the farthest node from Times Square in New York City (node # 299046361) You can also try this with other cities.  If you need to get a node number of a starting point that you want to check, go to Openstreetmap.org and enter a location and then zoom into find the node number. E.G. A node in Paris, France would show a URL such as http://www.openstreetmap.org/node/17807753#map=14/48.8565/2.3521  Then you would grab the node number which is 17807753 to find the nearest or farthest node in relation to node # 17807753  Please be patient with the processing: it normally takes 2 minutes or more to get the result because the .osm is a huge XML data file.  I'm working on improving the speed in future versions of this tool. 

6.  NOTE: the pyosm.py library file was forked from the repo at https://github.com/werner2101/python-osm, based on original code by Rory McCann (http://blog.technomancy.org/), and Modifications by Christoph Lupprich (http://www.stopbeingcarbon.com), and modifications by Werner Hoch (http://www.h-renrew.de). 
I added some getitem functions in pyosm.py to make it easier to get the node XML info. 

7.  LIMITATIONS: This program can only compare nodes in OpenStreetMap. It will not be able to compare Openstreetmap landmarks that are ways (generally roads and large spaces) or relations (spatial relationships).  This tool only uses 2 dimensional Euclidean distance comparisons of nearest and farthest nodes. It does not take elevation (Z distance) into consideration. This is usually fine for smaller map area comparisions, such as in cities and towns. 
