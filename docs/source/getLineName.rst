getLineName
===========

Επιστρέφει το όνομα της γραμμής.
Για να χρησιμοποιηθεί χρειαζόμαστε και την παράμετρο **linecode** που μπορούμε να
την βρούμε αν φιλτράρουμε τον αριθμό του λεωφορείου που χρειαζόμαστε από τις
δράσεις webGetLines και webGetLinesWithMLInfo

Για παράδειγμα το Α1 ( **linecode** = 962 ) που είναι η γραμμή ΠΕΙΡΑΙΑΣ-ΒΟΥΛΑ , έχει διαδρομές
ΠΕΙΡΑΙΑΣ-ΒΟΥΛΑ και ΒΟΥΛΑ-ΠΕΙΡΑΙΑΣ.


Api Endpoint
------------

``http://telematics.oasa.gr/api/?act=getLineName&p1=linecode``


Response
--------

.. code-block:: python

   [
   {
   "line_descr":"\u03a0\u0395\u0399\u03a1\u0391\u0399\u0391\u03a3 - \u0392\u039f\u03a5\u039b\u0391",
   "line_descr_eng":"PEIRAIAS - VOYLA"
   }
   ]
