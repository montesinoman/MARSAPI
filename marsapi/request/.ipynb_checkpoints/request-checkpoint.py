###############################################################################
# DEPENDENCIES
###############################################################################

import subprocess
import json
import pandas
import os
import sys

###############################################################################
# CONSTANTS
###############################################################################

class URLIB:
    # Root URL
    root = 'https://methanedata.unep.org'
    # HEALTH block
    HEALTH = os.path.join(root,'api/healthcheck')
    # COUNTRY block
    COUNTRIES = os.path.join(root,'api/countries')
    COUNTRYSTATS = os.path.join(root,'api/countries/%s/keystats')
    COUNTRYFACTS = os.path.join(root,'api/factsheets/country/%s/year/%s')
    # PLUME block
    PLUMES = os.path.join(root,'api/plumes')
    PLUMEGEOJSON = os.path.join(root,'api/plumes/geojson')
    PLUMECENTROID = os.path.join(root,'api/plumes/centroids/geojson')
    PLUMEIMGCOORD = os.path.join(root,'api/plumes/images-coordinates')
    PLUMESAT = os.path.join(root,'api/plumes/satellites')
    PLUMESECTOR = os.path.join(root,'api/sector')
    PLUMESOURCE = os.path.join(root,'api/plumes/sources')
    # COMPANY block
    COMPANY = os.path.join(root,'api/companies')
    COMPANYFACT = os.path.join(root,'api/factsheets/company/%s/year/%s')

###############################################################################
# FUNCTIONS
###############################################################################

def _add_url_filters(url, filters):
    ''' Adds filters to the url
    :param url: str. URL.
    :param filters: list. List of filters.
    :returns: str. URL with the filters
    '''
    # Build a list with the filters
    filter_list = [f'{filtr.key()}={filtr.value().replace(" ","%20")}' \
                   for filtr in filters if filtr.value() is not None]
    # Join all filters
    filter_path = ('&').join(filter_list)
    # Add to the url
    url_with_filters = os.path.join(url, filter_path)
    # Return the full URL
    return url_with_filters

def _request(url):
    ''' Sends the request and captures the response
    :param url: str. URL for the request
    :returns: str. Response
    '''
    # Send the request
    response = subprocess.run(['curl', url],
                              capture_output=True,
                              text=True)
    # Check all good
    if response.returncode == 0:
        # Get the response 
        out =  response.stdout
    # Otherwise
    else:
        # Warn
        sys.exit(f"Error: {response.returncode} with {url}")
    # Return the response
    return out

def _healthcheck():
    ''' Checks that API is running
    '''
    # Check the health of the API
    vitals = _request(URLIB.HEALTH)
    # All goo if response is ''
    ishealthy = ('MethaneData public API' == vitals)
    # Retrun
    return ishealthy

def _json_response_to_df(response):
    ''' Convert a request response to data frame
    :param response: str. Request reponse.
    '''
    # Load the JSON
    json_response = json.loads(response)
    # Coercing to DataFrame
    df_response = pandas.DataFrame(json_response)
    # Return the dataframe
    return df_response
    