getBusLocation
==============

Επιστρέφει την τοποθεσία των λεωφορείων μιας συγκεκριμένης διαδρομής.
Χρειαζόμαστε και μια παράμετρο που είναι το **routecode** δηλαδή ο κώδικας
μιας διαδρομής . Στο παράδειγμα εμφανίζεται η απάντηση της διαδρομής
ΠΕΙΡΑΙΑΣ-ΒΟΥΛΑ (**routecode**=2045)


Api Endpoint
------------

``http://telematics.oasa.gr/api/?act=getBusLocation&p1=routecode``


Response
--------

.. code-block:: python

   [
   {
   "VEH_NO":"40860",
   "CS_DATE":"Jul 13 2016 11:05:32:000PM",
   "CS_LAT":"37.9018570",
   "CS_LNG":"23.7197450",
   "ROUTE_CODE":"2045"
   },
   {
   "VEH_NO":"40875",
   "CS_DATE":"Jul 13 2016 11:05:36:000PM",
   "CS_LAT":"37.9364170",
   "CS_LNG":"23.6405150",
   "ROUTE_CODE":"2045"
   }
   ]
