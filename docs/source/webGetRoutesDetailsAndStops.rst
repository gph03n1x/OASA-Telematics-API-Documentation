webGetRoutesDetailsAndStops
===========================

Επιστρέφει τις λεπτομέρειες της διαδρομής και συγκεκριμένα τις στάσεις, την σειρά με την οποία εμφανίζονται και την τοποθεσία τους.
Χρειαζόμαστε και μια παράμετρο που είναι το **routecode** δηλαδή ο κώδικας μιας διαδρομής.
Στο παράδειγμα εμφανίζονται τα απότελέσματα του webGetRoutesDetailsAndStops της διαδρομής ΠΕΙΡΑΙΑΣ-ΒΟΥΛΑ ( **routecode** =2045)


Api Endpoint
------------

``http://telematics.oasa.gr/api/?act=webGetRoutesDetailsAndStops&p1=routecode``


Response
--------

.. code-block:: python

   {
   "details": [
      {"routed_x":"23.63272","routed_y":"37.93851","routed_order":"1"},
      {"routed_x":"23.6326","routed_y":"37.93851","routed_order":"2"},
      ....
   ],
   "stops": [
      {
      "StopCode":"10183","StopID":"25","StopDescr":"\u03a0\u0395\u0399\u03a1\u0391\u0399\u0391\u03a3",
      "StopDescrEng":"PEIRAIAS","StopStreet":null,"StopStreetEng":null,"StopHeading":"93","StopLat":"37.938246",
      "StopLng":"23.6320605","RouteStopOrder":"1","StopType":"0","StopAmea":"0"
      },
      {
      "StopCode":"400191","StopID":"400191","StopDescr":"\u039a\u039b\u0395\u0399\u03a3\u039f\u0392\u0397\u03a3",
      "StopDescrEng":"KLEISOVIS","StopStreet":"\u039a\u039b\u0395\u0399\u03a3\u039f\u0392\u0397\u03a3",
      "StopStreetEng":null,"StopHeading":"165","StopLat":"37.9361702","StopLng":"23.6328014",
      "RouteStopOrder":"2","StopType":"0","StopAmea":"0"
      },
      ....
   ]}
