getSchedLines
=============
Μας επιστρέφει τους χρόνους come και go που φαντάζομαι αντιστοιχούν στην αφετηρία και τέρμα.

Χρειαζόμαστε **mlcode** , **lineCode** τα οποία μπορούμε να τα βρούμε από το
webGetLinesWithML και **sdcCode** το οποίο μπορούμε να βρούμε από getScheduleDaysMasterline.


Api Endpoint
------------

``http://telematics.oasa.gr/api/?act=getSchedLines&p1=mlCode&p2=sdcCode&p3=lineCode``


Response
--------

``για http://telematics.oasa.gr/api/?act=getSchedLines&p1=177&p2=93&p3=1079``

.. code-block:: python

   {"come":[{
        "line_id":"11",
        "sde_code":"816784",
        "sdc_code":"93",
        "sds_code":"1292",
        "sde_aa":"7",
        "sde_line1":"1079",
        "sde_kp1":"0",
        "sde_start1":"1900-01-01 23:15:00",
        "sde_end1":"1900-01-02 00:00:00",
        "sde_line2":"1079",
        "sde_kp2":"0",
        "sde_start2":"1900-01-02 00:00:00",
        "sde_end2":"1900-01-02 00:45:00",
        "sde_sort":"980",
        "sde_descr2":null,
        "line_circle":"0",
        "line_descr":"\u0391\u039d\u03a9 \u03a0\u0391\u03a4\u0397\u03a3\u0399\u0391 - \u039d.       \u03a0\u0391\u0393\u039a\u03a1\u0391\u03a4\u0399 - \u039d. \u0395\u039b\u0392\u0395\u03a4\u0399\u0391",
        "line_descr_eng":"ANO PATISIA - N. PAGKRATI - N. ELVETIA"
    },...],
    "go":[{
        "line_id":"11",
        "sde_code":"816763",
        "sdc_code":"93",
        "sds_code":"1290",
        "sde_aa":"13",
        "sde_line1":"1079",
        "sde_kp1":"0",
        "sde_start1":"1900-01-02 00:35:00",
        "sde_end1":"1900-01-02 01:20:00",
        "sde_line2":"1079",
        "sde_kp2":"0",
        "sde_start2":"1900-01-02 01:20:00",
        "sde_end2":"1900-01-02 02:05:00",
        "sde_sort":"1",
        "sde_descr1":null,
        "line_circle":"0",
        "line_descr":"\u0391\u039d\u03a9 \u03a0\u0391\u03a4\u0397\u03a3\u0399\u0391 - \u039d. \u03a0\u0391\u0393\u039a\u03a1\u0391\u03a4\u0399 - \u039d. \u0395\u039b\u0392\u0395\u03a4\u0399\u0391",
        "line_descr_eng":"ANO PATISIA - N. PAGKRATI - N. ELVETIA"
    },...]
    }
