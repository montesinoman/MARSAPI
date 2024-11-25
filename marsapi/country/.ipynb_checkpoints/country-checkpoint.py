###############################################################################
# DEPENDENCIES
###############################################################################

import request
import json

###############################################################################
# CONSTANTS
###############################################################################

###############################################################################
# FUNCTIONS
###############################################################################

def list_all():
    ''' Lists all the countries
    :returns: DataFrame. Country code and name.
    '''
    # Get the list
    countries = request._request(request.URLIB.COUNTRIES)
    # Companies as data frame
    countries = request._json_response_to_df(countries)
    # Return the list
    return countries

def find_id(countryname):
    ''' Tries to find the country ID
    :param countryname: str. Country code.
    '''
    # List all companies
    all_countries = list_all()
    # Find the company name
    this_country = all_countries[
        all_countries['name'].str.contains(countryname,
                                           case=False,
                                           na=False)]
    # Return the ID
    return this_country['code'].iloc[0]

def get_stats(country):
    ''' Get IMEO/MARS statistics of a country for a given year
    :param companyid: str. IMEO country ID.
    :param year: int. Year of the stats.
    :returns: dict. IMEO/MARS statistics
    '''
    # Build URL
    this_url = request.URLIB.COUNTRYSTATS % (country)
    # Request the information
    country_stats = request._request(this_url)
    # Turn into a data frame
    country_stats = json.loads(country_stats)
    # Return
    return country_stats

def get_info(countryid, year):
    ''' Get information of a country for a given year
    :param countryid: str. IMEO country code.
    :param year: int. Information on that year.
    :returns:
    '''
    # Build URL
    this_url = request.URLIB.COUNTRYFACTS % (countryid, str(year))
    # Request the information
    country_facts = request._request(this_url)
    # Turn into a data frame
    country_facts = json.loads(country_facts)
    # Return
    return country_facts
