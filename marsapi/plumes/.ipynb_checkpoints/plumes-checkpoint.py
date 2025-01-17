###############################################################################
# DEPENDENCIES
###############################################################################

import json
import geojson
import geopandas as gpd
from ..request import request

###############################################################################
# CONSTANTS
###############################################################################

###############################################################################
# FUNCTIONS
###############################################################################

def list_sectors():
    ''' Lists all the sectors
    :returns: DataFrame. Sector names.
    '''
    # Get the list
    sectors = request._request(request.URLIB.PLUMESECTOR)
    print(sectors)
    # Companies as data frame
    sectors = request._json_response_to_df(sectors)
    print(sectors)
    # Rename the column
    sectors.columns = ['Sectors']
    print(sectors)
    # Return the list
    return sectors

def list_satellites():
    ''' Lists all the satellites
    :returns: DataFrame. Satellite names.
    '''
    # Get the list
    satellites = request._request(request.URLIB.PLUMESAT)
    # Companies as data frame
    satellites = request._json_response_to_df(satellites)
    # Rename the column
    satellites.columns = ['Satellites']
    # Return the list
    return satellites

def list_sources():
    ''' Lists all the sources
    :returns: dict. Source list.
    '''
    # Get the list
    sources = request._request(request.URLIB.PLUMESOURCE)
    # Companies as data frame
    sources = request._json_response_to_df(sources)
    # Return the list
    return sources

def list_imagecoord(limit = None,
                    country = None,
                    sector = None,
                    source = None,
                    satellite = None,
                    asdf = False):
    ''' Lists all the sources
    :returns: dict. Source list.
    '''
    # Add the filters to the url
    url_full = request._add_url_filters(
        request.URLIB.PLUMEIMGCOORD,
        filters = {
            'limit':limit,
            'country':country,
            'sector':sector,
            'source':source,
            'satellite':satellite})
    # Get the list
    imgcoord = request._request(url_full)
    # Companies as data frame
    imgcoord = json.loads(imgcoord)
    # Coerce to dataframe if requested
    if asdf: imgcoord = gpd.GeoDataFrame.from_features(imgcoord['features'])
    # Return the list
    return imgcoord

def list_plumes(limit = None,
                country = None,
                sector = None,
                source = None,
                satellite = None,
                asdf = False):
    ''' Lists all the sources
    :returns: json. Source list.
    '''
    # Add the filters to the url
    url_full = request._add_url_filters(
        request.URLIB.PLUMEGEOJSON,
        filters = {
            'limit':limit,
            'country':country,
            'sector':sector,
            'source':source,
            'satellite':satellite})
    # Get the list
    plumes = request._request(url_full)
    # Companies as data frame
    plumes = json.loads(plumes)
    # Coerce to dataframe if requested
    if asdf: plumes = gpd.GeoDataFrame.from_features(plumes['features'])
    # Return the list
    return plumes

def list_centroids(limit = None,
                   country = None,
                   sector = None,
                   source = None,
                   satellite = None,
                   asdf = False):
    ''' Lists all the sources
    :returns: json. Source list.
    '''
    # Add the filters to the url
    url_full = request._add_url_filters(
        request.URLIB.PLUMECENTROID,
        filters = {
            'limit':limit,
            'country':country,
            'sector':sector,
            'source':source,
            'satellite':satellite})
    # Get the list
    centroids = request._request(url_full)
    # Companies as data frame
    centroids = json.loads(centroids)
    # Coerce to dataframe if requested
    if asdf: centroids = gpd.GeoDataFrame.from_features(centroids['features'])
    # Return the list
    return centroids

