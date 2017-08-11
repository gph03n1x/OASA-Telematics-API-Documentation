.. OASA Telematics API documentation master file, created by
   sphinx-quickstart on Tue Jul 12 15:01:15 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to OASA Telematics API's documentation!
===============================================

The api has the following form ::
   http://telematics.oasa.gr/api/?act=action&p1=parameter1&p2=parameter2

Μέσα από το `script`_ (Script v0.1.1) το οποίο χρησιμοποιούν στο http://telematics.oasa.gr/
τα requests που έχω τεκμηριώσει ως τώρα είναι **POST** requests τα οποία περνάνε
τις παραμέτρους στο url .


**Code example: Python**

Χρήση του API μέσω python requests. Το μόνο που αλλάζει είναι το endpoint.

.. code-block:: python

   >>> import requests
   >>> response = requests.post("http://telematics.oasa.gr/api/?act=getLinesAndRoutesForMl&p1=9")
   >>> json_response = response.json()
   >>> print(json_response[0]["line_descr"])
   'ΠΛΑΤΕΙΑ ΚΑΝΙΓΓΟΣ - ΓΚΥΖH'

**Code example: BASH**

Το ίδιο request με BASH. Πρέπει να είναι εγκατεστημένα το **curl** και το **jq**.

.. code-block:: bash

    $ curl -s "telematics.oasa.gr/api/?act=getLinesAndRoutesForMl&p1=9" | jq '.[].line_descr' 
    "ΠΛΑΤΕΙΑ ΚΑΝΙΓΓΟΣ - ΓΚΥΖH(ΚΥΚΛΙΚΗ)"
    
**Code example: PowerShell**

Και με powershell με χρήση της Invoke-RestMethod.

.. code-block:: powershell

   PS C:\> (Invoke-RestMethod "http://telematics.oasa.gr/api/?act=getLinesAndRoutesForMl&p1=9").line_descr
   ΠΛΑΤΕΙΑ ΚΑΝΙΓΓΟΣ - ΓΚΥΖH(ΚΥΚΛΙΚΗ)
       
Actions
-------

.. toctree::
   :maxdepth: 2

   webGetLines
   webGetLinesWithMLInfo
   webGetRoutes
   webGetStops
   webRouteDetails
   webRoutesForStop
   webGetRoutesDetailsAndStops
   getStopArrivals
   getBusLocation
   getScheduleDaysMasterline
   getLinesAndRoutesForMl
   getRoutesForLine
   getMLName
   getLineName
   getRouteName
   getStopNameAndXY
   getSchedLines
   getClosestStops

.. _script: http://telematics.oasa.gr/js/script.js
