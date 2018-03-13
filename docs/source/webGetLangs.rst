webGetLangs
===========

Επιστρέφει strings τα οποία χρησιμοποιούνται για localization από την σελίδα του OASA.

Api Endpoint
------------

``http://telematics.oasa.gr/api/?act=webGetLangs``

Response
--------

.. code-block:: python

   [
   {
   "lang_id":"1",
   "el":"\u03a0\u03bb\u03b7\u03c1\u03bf\u03c6\u03bf\u03c1\u03af\u03b5\u03c2 \u0393\u03c1\u03b1\u03bc\u03bc\u03ae\u03c2",
   "en":"Line Information"
   }
   ....
   ]


Response Breakdown
------------------

*lang_id* : Το id του string
*el* : το string με ελληνικούς χαρακτήρες (unicode)
*en* : το string με αγγλικούς χαρακτήρες (ascii)