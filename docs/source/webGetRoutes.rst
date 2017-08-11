webGetRoutes
============

Επιστρέφει τις διαδρομές σχετικά με την διαδρομή μιας γραμμής.
Για να χρησιμοποιηθεί χρειαζόμαστε και την παράμετρο **linecode** που μπορούμε να
την βρούμε αν φιλτράρουμε τον αριθμό του λεωφορείου που χρειαζόμαστε από τις
δράσεις webGetLines και webGetLinesWithMLInfo

Για παράδειγμα το Α1 ( **linecode** = 962 ) που είναι η γραμμή ΠΕΙΡΑΙΑΣ-ΒΟΥΛΑ , έχει διαδρομές
ΠΕΙΡΑΙΑΣ-ΒΟΥΛΑ και ΒΟΥΛΑ-ΠΕΙΡΑΙΑΣ.


Api Endpoint
------------

``http://telematics.oasa.gr/api/?act=webGetRoutes&p1=linecode``


Response
--------

.. code-block:: python

   [
   {
   "RouteCode":"2045",
   "LineCode":"962",
   "RouteDescr":"\u03a0\u0395\u0399\u03a1\u0391\u0399\u0391\u03a3 - \u0392\u039f\u03a5\u039b\u0391",
   "RouteDescrEng":"PEIRAIAS - VOULA",
   "RouteType":"1",
   "RouteDistance":"22385.44"
   },
   {
   "RouteCode":"2046",
   "LineCode":"962",
   "RouteDescr":"\u0392\u039f\u03a5\u039b\u0391 - \u03a0\u0395\u0399\u03a1\u0391\u0399\u0391\u03a3",
   "RouteDescrEng":"VOULA - PEIRAIAS",
   "RouteType":"2",
   "RouteDistance":"22644.61"
   }
   ]
