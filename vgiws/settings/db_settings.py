#!/usr/bin/env python
# -*- coding: utf-8 -*-


############################################################
# POSTGRESQL
############################################################

# A dictionary with the settings about connection
__PGSQL_CONNECTION_SETTINGS__ = {
    "HOSTNAME": "database",
    "USERNAME": "postgres",
    "PASSWORD": "password",
    "DATABASE": "pauliceia",
    "PORT": 5432
}

# A dictionary with the settings about Test/Debug connection
__DEBUG_PGSQL_CONNECTION_SETTINGS__ = {
    "HOSTNAME": "database",
    "USERNAME": "postgres",
    "PASSWORD": "password",
    "DATABASE": "pauliceia",
    "PORT": 5432
}


############################################################
# GEOSERVER
############################################################

# A dictionary with the settings about connection
__GEOSERVER_CONNECTION_SETTINGS__ = {
    "HOSTNAME": "localhost",
    "PORT": 8001,
    "WORKSPACE": "pauliceia",
    "DATASTORE": "pauliceia",
}

# A dictionary with the settings about Test/Debug connection
__DEBUG_GEOSERVER_CONNECTION_SETTINGS__ = {
    "HOSTNAME": "localhost",
    "PORT": 8001,
    "WORKSPACE": "pauliceia",
    "DATASTORE": "pauliceia",
}


############################################################
# GEOSERVER-REST
############################################################

# A dictionary with the settings about connection
__GEOSERVER_REST_CONNECTION_SETTINGS__ = {
    "HOSTNAME": "localhost",
    "PORT": 3001,
}
