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
   "Line_Code":"815",
   "Line_ID":"021",
   "Line_Descr":"\u03a0\u039b\u0391\u03a4\u0395\u0399\u0391 \u039a\u0391\u039d\u0399\u0393\u0393\u039f\u03a3 - \u0393\u039a\u03a5\u0396H",
   "Line_Descr_Eng":"PLATEIA KANIGKOS - GKIZI"
   },
   ....
   ]



Response Breakdown
------------------

*Line_Code*: Μεταβαλλόμενη τιμή, Πιθανότατα αντιστοιχεί σε κάθε λεωφορείο εν κίνησή, Επίσης φαίνεται να είναι URI.

*Line_ID*: Unicode formated string Identifier της κάθε γραμμής

*Line_Descr*: Unicode formated string, με τον τίτλο της γραμμής, 'ΠΛΑΤΕΙΑ ΚΑΝΙΓΓΟΣ - ΓΚΥΖH(ΚΥΚΛΙΚΗ)'

*Line_Descr_Eng*: Ίδιο με το line_descr αλλά ascii formated
