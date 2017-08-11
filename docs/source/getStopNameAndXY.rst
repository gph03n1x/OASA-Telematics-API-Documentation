getStopNameAndXY
================

Επιστρέφει το όνομα της στάσης και τις συντεταγμένες της.
Χρειαζόμαστε και μια παράμετρο που είναι το **stopcode** δηλαδή ο κώδικας μιας στάσης.
Για να τον βρούμε μπορούμε να χρησιμοποιήσουμε την webGetStops.
Στο παράδειγμα εμφανίζονται τα απότελέσματα του getStopArrivals της στάσης ΗΣΑΠ Ν.ΦΑΛΗΡΟΥ ( **stopcode** = 400075 )


Api Endpoint
------------

``http://telematics.oasa.gr/api/?act=getStopNameAndXY&p1=stopcode``


Response
--------

.. code-block:: python

   [
   {
   "stop_descr":"\u0397\u03a3\u0391\u03a0 \u039d.\u03a6\u0391\u039b\u0397\u03a1\u039f\u03a5",
   "stop_descr_matrix_eng":"ISAP.N.FALIROY",
   "stop_lat":"37.9445913",
   "stop_lng":"23.6671421"
   "stop_heading":"88",
   "stop_id":"400075"
   }
   ]
