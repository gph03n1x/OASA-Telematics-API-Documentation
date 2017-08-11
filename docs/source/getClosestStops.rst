getClosestStops
===============

Χρησιμοποιώντας το **x** και το **y** το getClosestStops επιστρέφει τις κοντινότερες στάσεις


Api Endpoint
------------

``http://telematics.oasa.gr/api/?act=getClosestStops&p1=x&p2=y``


Response
--------

.. code-block:: python

   [
   {
   "StopCode":"400058","StopID":"400058","StopDescr":"\u0392\u0395\u039d\u0399\u0396\u0395\u039b\u039f\u03a5",
   "StopDescrEng":"VENIZELOY","StopStreet":"\u0393\u03a1.\u039b\u0391\u039c\u03a0\u03a1\u0391\u039a\u0397",
   "StopStreetEng":null,"StopHeading":"42","StopLat":"37.9432677","StopLng":"23.6520113",
   "distance":"0.001443313361679744"
   },
   {
   "StopCode":"400036","StopID":"400036","StopDescr":"\u0392\u0395\u039d\u0399\u0396\u0395\u039b\u039f\u03a5",
   "StopDescrEng":"VENIZELOY","StopStreet":"\u0393\u03a1.\u039b\u0391\u039c\u03a0\u03a1\u0391\u039a\u0397",
   "StopStreetEng":null,"StopHeading":"42","StopLat":"37.9433851","StopLng":"23.6521018",
   "distance":"0.001541670123601801"
   },
   ...
   ]
