getScheduleDaysMasterline
=========================

Για να χρησιμοποιηθεί χρειαζόμαστε και την παράμετρο *linecode* που μπορούμε να
την βρούμε αν φιλτράρουμε τον αριθμό του λεωφορείου που χρειαζόμαστε από τις
δράσεις webGetLines και webGetLinesWithMLInfo
Επιστρέφει το sdc_code, identifier για το ποιο πρόγραμμα/ωράριο ακολουθεί η γραμμή, το οποίο χρειάζεται για να κληθεί το getSchedLines function.

Για παράδειγμα το Α1 (linecode=962) που είναι η γραμμή ΠΕΙΡΑΙΑΣ-ΒΟΥΛΑ , έχει διαδρομές
ΠΕΙΡΑΙΑΣ-ΒΟΥΛΑ και ΒΟΥΛΑ-ΠΕΙΡΑΙΑΣ.


**Api Endpoint:**

``http://telematics.oasa.gr/api/?act=getScheduleDaysMasterline&p1=linecode``

**Response:**

.. code-block:: python

   [
   {
   "sdc_descr":"\u0398\u0395\u03a1\u0399\u039d\u039f 1 \u039a\u0391\u0398\u0397\u039c\u0395\u03a1\u0399\u039d\u0397",
   "sdc_descr_eng":"SUMMER DAILY",
   "sdc_code":"86",
   "":"0"
   },
   {
   "sdc_descr":"\u0398\u0395\u03a1\u0399\u039d\u039f 1 \u03a3\u0391\u0392\u0392\u0391\u03a4\u039f",
   "sdc_descr_eng":"SUMMER SATURDAY",
   "sdc_code":"87",
   "":"1"},
   {
   "sdc_descr":"\u0398\u0395\u03a1\u0399\u039d\u039f 1 \u039a\u03a5\u03a1\u0399\u0391\u039a\u0397",
   "sdc_descr_eng":"SUMMER SUNDAY",
   "sdc_code":"88",
   "":"0"
   }
   ]
