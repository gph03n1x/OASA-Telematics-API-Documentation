webGetMasterLines
=================

Επιστρέφει τα στοιχεία σχετικά με όλες τα master lines.

Ως Masterlines, η τηλεματική ορίζει όλες τις πρωταρχικές γραμμές. Για παράδειγμα μπορείτε να δείτε `εδώ <http://oasth.gr/#el/masterinfo/list/17/1/>`_ .
Πρωταρχική γραμμή θεωρείται η γραμμή 84, η οποία έχει ως παιδιά τις γραμμές 84Α και 84Β.
Ο ΟΑΣΑ, δεν χρησιμοποιεί τις masterlines γιατί δεν έχει βασίσει το σύστημα των γραμμών του σε πρωταρχικές γραμμές

Api Endpoint
------------

``http://telematics.oasa.gr/api/?act=webGetMasterLines``


Response
--------

.. code-block:: python

   [
   {
   "ml_code":"9",
   "ml_descr":"\u039a\u0391\u039d\u0399\u0393\u0393\u039f\u03a3 - \u0393\u039a\u03a5\u0396\u0397",
   "ml_descr_eng":null,
   "ml_id":"021",
   "sdc_code":"54",
   "line_code":"1151",
   "is_complex":"2"
   }
   ....
   ]



Response Breakdown
------------------

*ml_id*: Από ότι φαίνεται είναι λογικά το νούμερο της γραμμής.

*ml_code*: Identifier που έχει να κάνει με την περιοχή έναρξης. (Help needed)
Πιθανότατα το ml αντιστοιχεί στο MasterLine.

*sdc_code*: Identifier για το ωράριο που ακολουθεί η γραμμή, δες getSchedLines και getScheduleDaysMasterLine

*line_code*: Το Line_Code είναι ο μοναδικός αριθμός που ορίζει το software της τηλεματικής στην κάθε γραμμή.
Βάσει αυτού του αριθμού γίνονται όλοι συσχετισμοί στην βάση δεδομένων του ΟΑΣΑ. Επίσης φαίνεται να είναι URI.

*ml_descr*: Unicode formatted string, με τον τίτλο της γραμμής, 'ΠΛΑΤΕΙΑ ΚΑΝΙΓΓΟΣ - ΓΚΥΖH(ΚΥΚΛΙΚΗ)'

*ml_descr_eng*: πάντα null λογικά δεν έχει υλοποιηθεί ακόμα αλλά λογικά θα επιστρέφει στο μέλλον το *ml_descr* με ascii χαρακτήρες.

*is_complex* : δεν γνωρίζω τι αντιπροσωπεύει
