osmpal-nodes-basic
==================

OpenStreetMap tool to find nearest and farthest nodes from .osm file, with graphical display using matplotlib and networkx.



About this Program:
===================

OSM Pal Nodes Basic is an OpenStreetMap text-only tool to find nearest and farthest nodes of interest from .osm file. For example, you're visiting another city or you just moved to another city. You can use this tool to find the nearest amenities such as nearest coffee shop, restaurant, pub, school, etc.  The benefit of using this tool you don't need to load the osm data into a database or set up a web map server to do the node analysis. You just need to download an .osm file and run this python tool. 

This is the basic text-only version. If you want a graphical tool to compare OpenStreetmap nodes, try https://github.com/developingcountries/osmpal-nodes-graphical

Installation:
=============

1.  Download the code with your web browser or git clone https://github.com/developingcountries/osmpal-nodes-graphical/

2.  Use a text editor to edit line 4 in the file osmpalnodesgraph.py file  
 Line 4 SHOULD POINT TO THE LOCATION OF the pyosm.py library file, e.g. '/home/peter/osmpal/lib/')  This points to the pyosm.py library file that parses the OpenStreetMap data. 

3.  To use this application, you will also need to download an .osm data file, which has the map data. This repository has a sample .osm data file for New York city (new-york-small.osm) that you can try.  If you want to use your own osm data, download and run the JOSM Openstreet map tool at https://josm.openstreetmap.de/download/josm.jnlp
Once JOSM is running, click on the button that says download map data from OSM server, you'll see a world map. In the world map, click on the tab called "Areas around places" and then type the location you want to search, e.g. New York City. Narrow the area in the city that you want to do the node analysis, e.g. Union Square, New York City. Once you have
your area, Use 'file' menu > 'Save As...' to save the file as an .osm file to your computer.
Note: You can only download small .osm map sections in JOSM because  the OpenstreetMap api will limit the map area you can download. When you have your .osm file, use your text editor and edit Line 7 of the osmpalnodesgraph.py file with the location of the .osm map data file, e.g. osm = pyosm.OSMXMLFile('/home/peter/osmpal/new-york-small.osm') 

4.  Run this tool and check for the nearest or farthest point of interest. Using our new-york-osm.osm example file, to get the nearest tagged node to Union square, New York City, go into the command line and type: python osmpalnodesgraph.py nearest_node_tagged 246512355 $'amenity\': u\'cafe'  It will then return the cafe nearest to node number 246512355, which is a node in Union Square in New York City.  The result will also be graphed for you. Other possbilites for checking other points of interest include using 'restaurant' or 'pub' instead of 'cafe'.  Consult http://wiki.openstreetmap.org/wiki/Category:En:Key:amenity for a complete list of amenity nodes that you can search. 

5.  List of commands:

   In your command line, you can enter these commands:
 
   python osmpalnodes.py nearest_node_tagged 246512355 $'amenity\': u\'cafe'    #Prints out the cafe nearest to node 246512355   You can enter your own OpenStreetmap node number instead of  246512355. 'cafe' can be replaced with another Openstreetmap amenity such as 'pub', 'restaurant', 'university', 'school', etc.        
   
   python osmpalnodes.py farthest_node_tagged 246512355 $'amenity\': u\'cafe'    #Prints the cafe farthest from node 246512355 (within the bounding area of the .osm file being used).     
   
   python osmpalnodes.py nearest_node 246512355    #Prints the node (point) that's nearest to node number 246512355.  This node will be any generic node, and will not show the desired tagged node such as cafe, restaurant, etc.    
   
   python osmpalnodes.py farthest_node 246512355    #Prints the node (point) farthest away from node 246512355.  This node will be any generic node. 
   
   If you want to map out the node that was received, just go to the Openstreetmap website to map out the node. E.G. you entered: python osmpalnodes.py nearest_node_tagged 246512355 $'amenity\': u\'cafe'  and got node # 1740966205 (a Starbucks coffee shop) as the output.  Just go to http://www.openstreetmap.org/node/1740966205  You can also use the JOSM program (from step 4) or the OpenStreetMap website to find other nodes that you want to analyze.  

6.  NOTE: the pyosm.py library file was forked from the repo at https://github.com/werner2101/python-osm, based on original code by Rory McCann (http://blog.technomancy.org/), and Modifications by Christoph Lupprich (http://www.stopbeingcarbon.com), and modifications by Werner Hoch (http://www.h-renrew.de). 
I added some getitem functions in pyosm.py to make it easier to get the node XML info. 

7.  LIMITATIONS: This program can only compare nodes (i.e. points) in OpenStreetMap. It will not be able to compare Openstreetmap landmarks that are ways (generally roads and large spaces) or relations (spatial relationships).  This tool only uses 2 dimensional Euclidean distance comparisons of nearest and farthest nodes. It does not take elevation (Z distance) into consideration. This is usually fine for small map area comparisions, such as in cities and towns.  Small .osm files are recommended ( less than 100 megabytes).  This tool may take longer, like a few minutes, to parse larger .osm files and will definitely bog down or hang on .osm files larger than 100 MB.
