getStopArrivals
===============

Επιστρέφει τα λεωφορεία που αναμένει σύντομα η στάση.
Χρειαζόμαστε και μια παράμετρο που είναι το **stopcode** δηλαδή ο κώδικας μιας στάσης.
Για να τον βρούμε μπορούμε να χρησιμοποιήσουμε την webGetStops.
Στο παράδειγμα εμφανίζονται τα απότελέσματα του getStopArrivals της στάσης ΗΣΑΠ Ν.ΦΑΛΗΡΟΥ (**stopcode**=400075)


Api Endpoint
------------

``http://telematics.oasa.gr/api/?act=getStopArrivals&p1=stopcode``


Response
--------

.. code-block:: python

   [
   {
   "route_code":"2033",
   "veh_code":"50328",
   "btime2":"5"
   },
   {
   "route_code":"2005",
   "veh_code":"20521",
   "btime2":"5"
   }
   ]
