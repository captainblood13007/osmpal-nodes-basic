#!/usr/bin/python
# Geocoder program created by Peter Chin, May, 2014. peter.chin@redcross.ca, Open Source license pending
import sys
import os
sys.path.append('ENTER folder location for pyosm.py and geocoder.py here. e.g. /home/peter/osmnodes/lib/ or in Windows... C:\\osmnodes\\lib')
import pyosm
import re
osm = pyosm.OSMXMLFile('ENTER location of your .osm data file here. e.g. /home/peter/osmnodes/new-york-small.osm, or in Windows... C:\\osmnodes\\new-york-small.osm')

'''Geocodes a user entered address and returns a node for processing by osmpalnodesgraph.py
or by osmpalnodesbasic.py. Geocoder will match for query in the following priority: 1. house number and street name '''
'''2. zip code/postal code and city  3. Last option is matching for site name'''

def match_house_number_and_street(queryString):
    for Nid in osm.nodes:
        tag = str(osm.nodes[Nid].tags).lower()
        matchHouseTag = re.search(('addr:housenumber'), tag)
        houseTagContents = re.search('addr:housenumber\': u\'(.*?)\'', tag)
        if houseTagContents:
            houseQuery = re.search(str(houseTagContents.group(1)).lower(), queryString)
            if matchHouseTag and houseTagContents and houseQuery:
                matchStreetTag = re.search(('addr:street'),tag)
                streetTagContents = re.search('addr:street\': u\'(.*?)\'', tag)
                if streetTagContents:
                    streetQuery = re.search(str(streetTagContents.group(1)).lower(), queryString.lower())
                    if matchStreetTag and streetTagContents and streetQuery:
                        return osm.nodes[Nid]['id']

def match_postcode_and_city(queryString):
    for Nid in osm.nodes:
        tag = str(osm.nodes[Nid].tags).lower()
        matchPostcodeTag = re.search(('addr:postcode'), tag)
        postcodeTagContents = re.search('addr:postcode\': u\'(.*?)\'', tag)
        if postcodeTagContents:
            postcodeQuery = re.search(str(postcodeTagContents.group(1)), queryString)
            if matchPostcodeTag and postcodeTagContents and postcodeQuery:
                matchCityTag = re.search(('addr:city'), tag)
                cityTagContents = re.search('addr:city\': u\'(.*?)\'', tag)
                if cityTagContents:
                    cityQuery = re.search(str(cityTagContents.group(1)).lower(), queryString.lower())
                    if matchCityTag and cityTagContents and cityQuery:
                        return osm.nodes[Nid]['id']

'''Finds a site name that is in any tag in .osm file and has more than one word, e.g. Union Squre'''
def match_site_name(queryString):
    for Nid in osm.nodes:
        matchSiteName = re.search((queryString.lower()),str(osm.nodes[Nid].tags).lower())
        if matchSiteName:
            return osm.nodes[Nid]['id']

def geocode_node(queryString):
    try:
        if ' ' in queryString:  #if query string has space then do geocoding
            node = match_house_number_and_street(queryString)
            if node is None:
                node = match_postcode_and_city(queryString)
                if node is None:
                    node = match_site_name(queryString)
        else:
        #just match one word against first result in .osm file
            for Nid in osm.nodes:
                match = re.search((queryString.lower()+'?'), str(osm.nodes[Nid].tags).lower())
                if match:
                    node = osm.nodes[Nid]['id']
        return node
    except:
        e = sys.exc_info()[0]
        l = sys.exc_traceback.tb_lineno
        print 'The following error ocurred: ', e, l
