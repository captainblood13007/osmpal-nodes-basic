#!/usr/bin/python
import sys
import os
PYOSM_DIR = os.path.join(os.path.dirname(__file__), 'ENTER THE DIRECTORY LOCATION OF THE PYOSM FILE HERE, e.g. /home/peter/osmpal/lib/')
sys.path.append(PYOSM_DIR)
import pyosm
osm = pyosm.OSMXMLFile('ENTER THE LOCATION OF THE OPENSTREETMAP .OSM FILE HERE, e.g. /home/peter/osmpal/new-york-small.osm')
import re

def dist(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5

def nearest_node_tagged(nodeID, qry):
    try:
        for Nid in osm.nodes:
            if osm.nodes[Nid]['id'] == nodeID:
                X1 = osm.nodes[Nid]['lon']
                Y1 = osm.nodes[Nid]['lat']
                originalNode = Nid
        #arbitrarily large starting distance for comparison
        nearestDist = 100
        for Nid in osm.nodes:
            match = re.search('\''+qry+'(.*)', str(osm.nodes[Nid]['tags']))
            newDist = dist(X1, Y1, osm.nodes[Nid]['lon'], osm.nodes[Nid]['lat'])
            if match and newDist < nearestDist and Nid is not originalNode:
                nearestDist = newDist
                nearestNode = Nid
                nearestTag = match.group(1)
        print 'Nearest Distance (not to scale) is: ', nearestDist
        print '\n Nearest Node for your query is node number: ', nearestNode
        print '\n Nearest tagged node is: ', nearestTag
    except:
        e = sys.exc_info()[0]
        print 'The following error ocurred: ', e

def farthest_node_tagged(nodeID, qry):
    try:
        for Nid in osm.nodes:
            if osm.nodes[Nid]['id'] == nodeID:
                X1 = osm.nodes[Nid]['lon']
                Y1 = osm.nodes[Nid]['lat']
                originalNode = Nid
        #arbitrarily small starting distance for comparison
        farthestDist = 0
        for Nid in osm.nodes:
            match = re.search('\''+qry+'(.*)', str(osm.nodes[Nid]['tags']))
            newDist = dist(X1, Y1, osm.nodes[Nid]['lon'], osm.nodes[Nid]['lat'])
            if match and newDist > farthestDist and Nid is not originalNode:
                farthestDist = newDist
                farthestNode = Nid
                farthestTag = match.group(1)
                XFAR = osm.nodes[farthestNode]['lon']
                YFAR = osm.nodes[farthestNode]['lat']
        print '\n Farthest Node for your query is node number: ', farthestNode
        print '\n Farthest tagged node is: ', farthestTag
    except:
        e = sys.exc_info()[0]
        print 'The following error ocurred: ', e

def farthest_node(nodeID):
    #First loop through to get coordinates
    for nid in osm.nodes:
        if osm.nodes[nid]['id'] == nodeID:
            X1 = osm.nodes[nid]['lon']
            Y1 = osm.nodes[nid]['lat']
            originalNode = nid
            print '\n Your original node number is: ', originalNode
    #Arbitrarily small number that variable newDist will be bigger than in comparison below
    farthestDist = 0
    #Second loop through to calculate distance
    try:
        for Nid in osm.nodes:
            newDist = dist(X1, Y1, osm.nodes[Nid]['lon'], osm.nodes[Nid]['lat'])
            if newDist > farthestDist and Nid is not originalNode:
                farthestDist = newDist
                farthestNode = Nid
        if originalNode is not None:
            print '\n Farthest Node number is: ', farthestNode
            print '\n Farthest Distance calculated (not to scale) from your original node is : ', farthestDist
            XFAR = osm.nodes[farthestNode]['lon']
            YFAR = osm.nodes[farthestNode]['lat']
    except:
        e = sys.exc_info()[0]
        print 'The following error ocurred: ', e

def nearest_node(nodeID):
    #Need to loop through to get coordinates
    for nid in osm.nodes:
        if osm.nodes[nid]['id'] == nodeID:
            X1 = osm.nodes[nid]['lon']
            Y1 = osm.nodes[nid]['lat']
            originalNode = nid
            print '\n Your original node (starting node) number is :', originalNode
    # Start with arbitrarily large nearestDist and get smaller and smaller distance
    nearestDist = 10000
    try:
        for Nid in osm.nodes:
            newDist = dist(X1, Y1, osm.nodes[Nid]['lon'], osm.nodes[Nid]['lat'])
            if newDist < nearestDist and Nid is not originalNode:
                nearestDist = newDist
                nearestNode = Nid
        if originalNode is not None:
            print '\n Nearest Node number is: ', nearestNode
            print '\n Nearest Distance calculated (not to scale): ', nearestDist
            XNEAR = osm.nodes[nearestNode]['lon']
            YNEAR = osm.nodes[nearestNode]['lat']
    except:
        e = sys.exc_info()[0]
        print 'The following error ocurred: ', e

#Allow user to choose the function in command line
# e.g. python osmpalnodesbasic.py nearest_node_tagged 26301254 $'amenity\': u\'cafe'
if __name__ == "__main__":
    if sys.argv[1] == 'nearest_node_tagged':
        nearest_node_tagged(int(sys.argv[2]), sys.argv[3])
    elif sys.argv[1] == 'farthest_node_tagged':
        farthest_node_tagged(int(sys.argv[2]), sys.argv[3])
    elif sys.argv[1] == 'nearest_node':
        nearest_node(int(sys.argv[2]))
    elif sys.argv[1] == 'farthest_node':
        farthest_node(int(sys.argv[2]))
