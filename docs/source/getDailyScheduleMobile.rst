getDailyScheduleMobile
==============

Μας επιστρέφει τους χρόνους των καθημερινών δρομολογίων (δηλαδή του ημερήσιου προγραμματισμού) come και go που αντιστοιχούν στην αφετηρία και τέρμα σε απλή μορφή όπως εμφανίζονται στην εφαρμογή. Στο παράδειγμα εμφανίζεται η απάντηση της γραμμής
Α5 ΑΚΑΔΗΜΙΑ - ΑΓ. ΠΑΡΑΣΚΕΥΗ - ΑΝΘΟΥΣΑ ( **line_code** = 1058 )


Api Endpoint
------------

``http://telematics.oasa.gr/api/?act=getDailyScheduleMobile&line_code=line_code``


Response
--------

.. code-block:: python
  {"come":[{"time":"05:00","msg":null},...],
  "go":[{"time":"05:00","msg":null},...]
  }
