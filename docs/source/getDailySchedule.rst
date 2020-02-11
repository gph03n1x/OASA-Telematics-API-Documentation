getDailySchedule
================

Μας επιστρέφει τους χρόνους των καθημερινών δρομολογίων (δηλαδή του ημερήσιου προγραμματισμού) come και go που αντιστοιχούν στην αφετηρία και τέρμα.

Σε αντίθεση με το getSchedLines, χρειαζόμαστε μόνο **lineCode**.

Api Endpoint
------------

``http://telematics.oasa.gr/api/?act=getDailySchedule&line_code=lineCode``

Response
--------

``για http://telematics.oasa.gr/api/?act=getDailySchedule&line_code=1079``

.. code-block:: python

  {"come":[{
    "line_id":"218",
    "sdd_code":"15743899",
    "sdc_code":"54",
    "sds_code":"3285",
    "sdd_aa":"2",
    "sdd_line1":null,
    "sdd_kp1":"0",
    "sdd_start1":null,
    "sde_start1":null,
    "sde_end1":null,
    "sdd_line2":"1035",
    "sdd_kp2":"0",
    "sde_start2":"1900-01-01 05:00:00",
    "sde_end2":"1900-01-01 05:45:00",
    "sdd_sort":"1",
    "line_circle":"0",
    "line_descr":"\u03a0\u0395\u0399\u03a1\u0391\u0399\u0391\u03a3 - \u03a3\u03a4. \u0394\u0391\u03a6\u039d\u0397",
    "line_descr_eng":"PEIRAIAS - ST. DAFNI",
    "remarks":null
  },...],
  "go":[{
    "line_id":"218",
    "sdd_code":"15743895",
    "sdc_code":"54",
    "sds_code":"3284",
    "sdd_aa":"2",
    "sdd_line1":"1035",
    "sdd_kp1":"0",
    "sdd_start1":"Jan 1 1900 05:00:00:000AM",
    "sde_start1":"1900-01-01 05:00:00",
    "sde_end1":"1900-01-01 05:50:00",
    "sdd_line2":"1035",
    "sdd_kp2":"0",
    "sde_start2":"1900-01-01 05:55:00",
    "sde_end2":"1900-01-01 06:44:00",
    "sdd_sort":"1",
    "line_circle":"0",
    "line_descr":"\u03a0\u0395\u0399\u03a1\u0391\u0399\u0391\u03a3 - \u03a3\u03a4. \u0394\u0391\u03a6\u039d\u0397",
    "line_descr_eng":"PEIRAIAS - ST. DAFNI",
    "remarks":null
  },...]
  }
