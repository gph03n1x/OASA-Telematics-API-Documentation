getRoutesForLine
================

Επιστρέφει τις διαδρομές σχετικά με την διαδρομή μιας γραμμής όμοια με την webGetRoutes.
Για να χρησιμοποιηθεί χρειαζόμαστε και την παράμετρο **linecode** που μπορούμε να
την βρούμε αν φιλτράρουμε τον αριθμό του λεωφορείου που χρειαζόμαστε από τις
δράσεις webGetLines και webGetLinesWithMLInfo

Για παράδειγμα το Α1 (**linecode**=962) που είναι η γραμμή ΠΕΙΡΑΙΑΣ-ΒΟΥΛΑ , έχει διαδρομές
ΠΕΙΡΑΙΑΣ-ΒΟΥΛΑ και ΒΟΥΛΑ-ΠΕΙΡΑΙΑΣ.


Api Endpoint
------------

``http://telematics.oasa.gr/api/?act=getRoutesForLine&p1=linecode``


Response
--------

.. code-block:: python

   [
   {
   "route_code":"2045",
   "route_id":"01",
   "route_descr":"\u03a0\u0395\u0399\u03a1\u0391\u0399\u0391\u03a3 - \u0392\u039f\u03a5\u039b\u0391",
   "route_active":"1",
   "route_descr_eng":"PEIRAIAS - VOULA"
   },
   {
   "route_code":"2046",
   "route_id":"02",
   "route_descr":"\u0392\u039f\u03a5\u039b\u0391 - \u03a0\u0395\u0399\u03a1\u0391\u0399\u0391\u03a3",
   "route_active":"1",
   "route_descr_eng":"VOULA - PEIRAIAS"
   }
   ]
