webGetStops
===========

Επιστρέφει τις στάσεις μιας διαδρομής. Χρειαζόμαστε και μια παράμετρο που είναι
το **routecode** δηλαδή ο κώδικας μιας διαδρομής . Στο παράδειγμα εμφανίζεται η πρώτη
στάση της διαδρομής ΠΕΙΡΑΙΑΣ-ΒΟΥΛΑ (**routecode**=2045)


Api Endpoint
------------

``http://telematics.oasa.gr/api/?act=webGetStops&p1=routecode``


Response
--------

.. code-block:: python

   [
   {
   "StopCode":"10183",
   "StopID":"25",
   "StopDescr":"\u03a0\u0395\u0399\u03a1\u0391\u0399\u0391\u03a3",
   "StopDescrEng":"PEIRAIAS",
   "StopStreet":null,
   "StopStreetEng":null,
   "StopHeading":"93",
   "StopLat":"37.938246",
   "StopLng":"23.6320605",
   "RouteStopOrder":"1",
   "StopType":"0",
   "StopAmea":"0"
   },
   ....
   ]
