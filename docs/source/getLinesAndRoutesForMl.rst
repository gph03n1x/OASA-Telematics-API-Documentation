getLinesAndRoutesForMl
======================

Επιστρέφει τις διαδρομές σχετικά με την διαδρομή μιας γραμμής.
Για να χρησιμοποιηθεί χρειαζόμαστε και την παράμετρο *mlcode* που μπορούμε να
την βρούμε αν φιλτράρουμε τον αριθμό του λεωφορείου που χρειαζόμαστε από τη
δράση webGetLinesWithMLInfo

Στο παράδειγμα έχουμε mlcode=9


**Api Endpoint:**

``http://telematics.oasa.gr/api/?act=getLinesAndRoutesForMl&p1=mlcode``


**Response:**

.. code-block:: python

   [
   {
   "line_code":"815",
   "line_id":"021",
   "line_descr":"\u03a0\u039b\u0391\u03a4\u0395\u0399\u0391 \u039a\u0391\u039d\u0399\u0393\u0393\u039f\u03a3 - \u0393\u039a\u03a5\u0396H",
   "line_descr_eng":"PLATEIA KANIGKOS - GKIZI",
   "afetiria":"\u03a0\u039b\u0391\u03a4\u0395\u0399\u0391 \u039a\u0391\u039d\u0399\u0393\u0393\u039f\u03a3",
   "terma":"\u03a0\u039b\u0391\u03a4\u0395\u0399\u0391 \u0393\u039a\u03a5\u0396\u0397",
   "afetiria_en":"PLATEIA KANIGOS",
   "terma_en":"PLATEIA GYZI",
   "line_id_gr":"021",
   "sdc_code":"86"
   }
   ]
