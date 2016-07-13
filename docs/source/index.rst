.. OASA Telematics API documentation master file, created by
   sphinx-quickstart on Tue Jul 12 15:01:15 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to OASA Telematics API's documentation!
===============================================

The api has the following form ::
   http://telematics.oasa.gr/api/?act=action&p1=parameter1&p2=parameter2

Μέσα από το `script`_ το οποίο χρησιμοποιούν στο http://telematics.oasa.gr/
τα requests που έχω τεκμηριώσει ως τώρα είναι **POST** requests τα οποία περνάνε
τις παραμέτρους στο url .


Actions:

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

.. _script: http://telematics.oasa.gr/js/script.js

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
