webRoutesForStop
================

Επιστρέφει πληροφορίες σχετικά με μια στάση.
Χρειαζόμαστε και μια παράμετρο που είναι το **stopcode** δηλαδή ο κώδικας μιας στάσης.
Για να τον βρούμε μπορούμε να χρησιμοποιήσουμε την webGetStops.
Στο παράδειγμα εμφανίζονται τα απότελέσματα του webRoutesForStop της στάσης ΗΣΑΠ Ν.ΦΑΛΗΡΟΥ (**stopcode**=400075)


Api Endpoint
------------

``http://telematics.oasa.gr/api/?act=webRoutesForStop&p1=stopcode``


Response
--------

.. code-block:: python

   [
   {
   "RouteCode":"1867",
   "LineCode":"851",
   "RouteDescr":"\u03a0\u0395\u0399\u03a1\u0391\u0399\u0391\u03a3 - \u039d. \u03a3\u039c\u03a5\u03a1\u039d\u0397",
   "RouteDescrEng":"PEIRAIAS - NEA SMYRNI",
   "RouteType":"1",
   "RouteDistance":"22205.03",
   "LineID":"130",
   "LineDescr":"\u03a0\u0395\u0399\u03a1\u0391\u0399\u0391\u03a3 - \u039d. \u03a3\u039c\u03a5\u03a1\u039d\u0397 (\u039a\u03a5\u039a\u039b\u0399\u039a\u0397)",
   "LineDescrEng":"PEIRAIAS - NEA SMIRNI",
   "MasterLineCode":"202"
   },
   {
   "RouteCode":"1881",
   "LineCode":"871",
   "RouteDescr":"\u03a0\u0395\u0399\u03a1\u0391\u0399\u0391\u03a3 - \u0391\u039d\u03a9 \u0393\u039b\u03a5\u03a6\u0391\u0394\u0391",
   "RouteDescrEng":"PEIRAIAS - ANO GLYFADA",
   "RouteType":"1",
   "RouteDistance":"21369.72",
   "LineID":"\u03921",
   "LineDescr":"\u03a0\u0395\u0399\u03a1\u0391\u0399\u0391\u03a3 - \u0391\u039d\u03a9 \u0393\u039b\u03a5\u03a6\u0391\u0394\u0391",
   "LineDescrEng":"PEIRAIAS - ANO GLYFADA",
   "MasterLineCode":"59"
   },
   ....
   ]
