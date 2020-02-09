webGetLines
===========

Επιστρέφει τα στοιχεία σχετικά με όλες τις γραμμές των λεωφορείων.


Api Endpoint
------------

``http://telematics.oasa.gr/api/?act=webGetLines``


Response
--------

.. code-block:: python

   [
   {
   "LineCode":"815",
   "LineID":"021",
   "LineDescr":"\u03a0\u039b\u0391\u03a4\u0395\u0399\u0391 \u039a\u0391\u039d\u0399\u0393\u0393\u039f\u03a3 - \u0393\u039a\u03a5\u0396H",
   "LineDescrEng":"PLATEIA KANIGKOS - GKIZI"
   },
   ....
   ]



Response Breakdown
------------------

*LineCode*: Το Line_Code είναι ο μοναδικός αριθμός που ορίζει το software της τηλεματικής στην κάθε γραμμή.
Βάσει αυτού του αριθμού γίνονται όλοι συσχετισμοί στην βάση δεδομένων του ΟΑΣΑ. Επίσης φαίνεται να είναι URI.

*lineID*: Unicode formatted string το οποίο είναι ο αριθμός της γραμμής

*LineDescr*: Unicode formatted string, με τον τίτλο της γραμμής, 'ΠΛΑΤΕΙΑ ΚΑΝΙΓΓΟΣ - ΓΚΥΖH(ΚΥΚΛΙΚΗ)'

*LineDescrEng*: Ίδιο με το LineDescr αλλά ascii formatted
