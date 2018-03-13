webRouteDetails
===============

Επιστρέφει τις λεπτομέρειες της διαδρομής δηλαδή την τοποθεσία των στάσεων και την σειρά με την οποία τις 'επισκέπτεται' το λεωφορείο.
Χρησιμοποιείται κυρίως για απεικόνηση στο google maps
Χρειαζόμαστε και μια παράμετρο που είναι το **routecode** δηλαδή ο κώδικας μιας διαδρομής.
Στο παράδειγμα εμφανίζονται τα απότελέσματα του webRouteDetails της διαδρομής ΠΕΙΡΑΙΑΣ-ΒΟΥΛΑ ( **routecode** = 2045 )

Api Endpoint
------------

``http://telematics.oasa.gr/api/?act=webRouteDetails&p1=routecode``


Response
--------

.. code-block:: python

   [
   {"routed_x":"23.63272","routed_y":"37.93851","routed_order":"1"},
   {"routed_x":"23.6326","routed_y":"37.93851","routed_order":"2"},
   {"routed_x":"23.63233","routed_y":"37.93833","routed_order":"3"},
   ....
   ]
