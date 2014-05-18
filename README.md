osmpal-nodes-basic
==================

OpenStreetMap tool to find nearest and farthest nodes from .osm file.



About this Program:
===================

OSM Pal Nodes Basic is an OpenStreetMap text-only tool to find nearest and farthest nodes of interest from an .osm file. For example, you're visiting another city or you just moved to another city. You can use this tool to find the nearest amenities such as nearest coffee shop, restaurant, pub, school, etc.  The benefit of using this tool you don't need to load the osm data into a database or set up a web map server to do the node analysis. You just need to download an .osm file and run this python tool.  It includes a built-in geocoder so that you can enter a street address or zip/postal codes for analysis (see installation instructions below).

This is the basic text-only version. If you want a graphical tool to compare OpenStreetmap nodes, try https://github.com/developingcountries/osmpal-nodes-graphical

Installation:
=============

1.  Use your web browser to copy the code from each file or use the git program, i.e. git clone https://github.com/developingcountries/osmpal-nodes-basic/

2.  Use a text editor to edit line 5 in the file osmpalnodesbasic.py file so that the sys.path.append statement points to the correct folder location for pyosm.py and geocoder.py, e.g. /home/peter/osmpal/lib/ or in Windows... C:\ \osmpal\ \lib' ALSO, use your text editor to edit line 5 in the file geocoder.py. Line 5 SHOULD POINT TO THE FOLDER LOCATION OF the pyosm.py library file, e.g. '/home/peter/osmpal/lib/'.

3.  To use this application, you will also need to download an .osm data file, which has the map data. This repository has a sample .osm data file for New York city (new-york-small.osm) that you can use.  If you want to use your own osm data, download and run the JOSM Openstreet map tool at https://josm.openstreetmap.de/download/josm.jnlp
Once JOSM is running, click on the button that says download map data from OSM server, you'll see a world map. In the world map, click on the tab called "Areas around places" and then type the location you want to search, e.g. New York City. Narrow the area in the city that you want to do the node analysis, e.g. Union Square, New York City. Once you have your area, Use 'file' menu > 'Save As...' to save the file as an .osm file to your computer.

   Note: You can only download small .osm map sections in JOSM because  the OpenstreetMap api will limit the map area you can download. When you have your .osm file, use your text editor and edit Line 8 of the osmpalnodesbasic.py file AND ALSO EDIT Line 8 of the geocoder.py file with the location of the .osm map data file, e.g. osm = pyosm.OSMXMLFile('/home/peter/osmpal/new-york-small.osm', or in Windows... C:\ \osmpal\ \new-york-small.osm)
    

4.  Run this tool and check for the nearest or farthest point of interest. Using our new-york-osm.osm example file, to get the nearest tagged node to Union square, New York City, go into the command line and  CHANGE TO THE DIRECTORY THAT CONTAINS THE FILES and type: python osmpalnodesbasic.py nearest_node_tagged 246512355 $'amenity\': u\'cafe'  It will then return the cafe nearest to node number 246512355, which is a node in Union Square in New York City.   Other amenity possbilites for checking other points of interest include using 'restaurant', 'school', or 'pub' instead of 'cafe'.   Consult http://wiki.openstreetmap.org/wiki/Key:amenity?uselang=en-US for a complete list of amenity nodes that you can search. Instead of searching for an amenity tag, you can also search for a tag such as leisure, tourism, sport or historic.

5.  You can also use the geocoder to process a node. For example, you want to find the coffee shop nearest to 870 Broadway in New York City, in python command line, In Linux or Mac command line, you would enter python osmpalnodesbasic.py nearest_node_tagged $'870 broadway' $'amenity\': u\'cafe'  In Windows, you would use " " quotes, and type: python osmpalnodesbasic.py nearest_node_tagged "870 broadway" "amenity\': u\'cafe"
    
    Note: the $ dollar signs before 870 broadway and before amenity for Linux or Mac. Windows python would use the double quotes only.  See step 6 for command line options. The geocoder processes according to this order of priority: house number and street name have highest priority, second highest priority is zip code/postal code and city combination (e.g. 10010 new york), third highest priority is site name such as 'union square', and least highest priority is a one word address such as 'starbucks'.
    
    
6.  List of commands:

    In your command line, ***IF YOU KNOW A NODE NUMBER TO PROCESS***, use any of the following commands:
    
    python osmpalnodesbasic.py nearest_node_tagged 246512355 $'amenity\': u\'cafe'    #Prints the cafe nearest to node 246512355   You can enter your own OpenStreetmap node number instead of  246512355. 'cafe' can be replaced with another Openstreetmap amenity such as 'pub', 'restaurant', 'university', 'school', etc.     ***In Windows, type: *** python osmpalnodesbasic.py nearest_node_tagged "870 broadway" "amenity\': u\'cafe"  ***Note that commands below are examples Linux/Mac command line. To run in Windows, simply change the $' ' to double quotes to wrap the parameters " "***
   
    python osmpalnodesbasic.py farthest_node_tagged 246512355 $'amenity\': u\'cafe'    #Prints and graphs the cafe farthest from node 246512355 (within the bounding area of the .osm file being used).  To run in Windows, type: python osmpalnodesbasic.py farthest_node_tagged 246512355 "amenity\': u\'cafe" 
   
    python osmpalnodesbasic.py nearest_node 246512355    #Prints and graphs the node (point) that's nearest to node number 246512355.  This node will be any generic node, and will not show the desired tagged node such as cafe, restaurant, etc.  
   
   python osmpalnodesbasic.py farthest_node 246512355    #Prints and graphs the node (point) farthest away from node 246512355.  This node will be any generic node.   
   
   ***IF YOU WANT TO GEOCODE AN ADDRESS***, use any of the following commands: 
   
   python osmpalnodesbasic.py nearest_node_tagged $'union square' $'amenity\': u\'cafe'   #Outputs the cafe that's nearest any point in Union Square. The geocoder provides a point in Union Square using just the landmark name of Union Square.
   
   python osmpalnodesbasic.py nearest_node_tagged $'870 broadway' $'amenity\': u\'cafe'    #Outputs the cafe that's nearest any point at 870 Broadway in New York, using the street address and street name combination from geocoder.py
   
   python osmpalnodesbasic.py nearest_node_tagged $'10010 new york' $'amenity\': u\'cafe'   #Outputs the cafe that's nearest any point at the 10010 zip code, using the zip code/postal code and city combination in the geocoder.
   
   python osmpalnodesbasic.py nearest_node_tagged $'mcdonald\'s' $'amenity\': u\'hospital'    #Outputs the hospital that's nearest to a one word location such as mcdonald's restaurant.

   Many other possible combinations: 
   
   python osmpalnodesbasic.py farthest_node_tagged $'mcdonald\'s' $'amenity\': u\'cafe'    #Outputs the cafe that's farthest away from a one word location such as mcdonald's restaurant.
   
   python osmpalnodesbasic.py nearest_node $'870 broadway'  #Outputs any generic point that's nearest to the geocoded point at 870 broadway in New York City.
   
   If you want to map out the node that was received, just copy the URL outputted in the command line. It will provide an Openstreetmap web link for you to see the node, e.g. http://www.openstreetmap.org/node/1740966205  You can also use the JOSM program (from step 4) or the OpenStreetMap website to find other nodes that you want to analyze, or simply enter an address for geocoding. 

7.  NOTE: the pyosm.py library file was forked from the repo at https://github.com/werner2101/python-osm, based on original code by Rory McCann (http://blog.technomancy.org/), and Modifications by Christoph Lupprich (http://www.stopbeingcarbon.com), and modifications by Werner Hoch (http://www.h-renrew.de). 
I added some getitem functions in pyosm.py to make it easier to get the node XML info. 

8.  LIMITATIONS: This program can only compare nodes (i.e. points) in OpenStreetMap. It will not be able to compare Openstreetmap landmarks that are ways (generally roads and large spaces) or relations (spatial relationships).  This tool only uses 2 dimensional Euclidean distance comparisons of nearest and farthest nodes. It does not take elevation (Z distance) into consideration. This is usually fine for small map area comparisions, such as in cities and towns.  Small .osm files are recommended ( less than 100 megabytes).  This tool may take longer, like a few minutes, to parse larger .osm files and will definitely bog down or hang on .osm files larger than 100 MB.
