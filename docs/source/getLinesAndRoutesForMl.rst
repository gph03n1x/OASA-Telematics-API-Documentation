getLinesAndRoutesForMl
======================

Επιστρέφει τις διαδρομές/δρομολόγια(lines) που αντιστιχουν σε μια γραμμή(masterline).
Για να χρησιμοποιηθεί χρειαζόμαστε και την παράμετρο *mlcode* που μπορούμε να
την βρούμε αν φιλτράρουμε τον αριθμό του λεωφορείου που χρειαζόμαστε από τη
δράση webGetLinesWithMLInfo

**Api Endpoint:**

``http://telematics.oasa.gr/api/?act=getLinesAndRoutesForMl&p1=mlcode``


Απ ότι φαίνεται, κάθε line/δρομολόγιο/*γραμμή* αντιστοιχεί σε ένα masterline/ml identifier, 
ωστόσο αυτό που το κάνει διαφορετικό απ τα υπόλοιπα lines(lines!=γραμμές, lines~=δρομολόγια),
είναι ότι τα masterlines μπορούν να έχουν παραπάνω από ένα child line/δρομολόγιο.

**Παράδειγμα, Αν κάνουμε το έξεις request:**

``http://telematics.oasa.gr/api/?act=getLinesAndRoutesForMl&p1=163``

**θα πάρουμε πίσω:**

.. code-block:: python

    [{
    'afetiria': 'ΑΝΩ ΝΕΑ ΣΜΥΡΝΗ ',
    'afetiria_en': 'ANO NEA SMIRNI',
    'line_code': '1030',
    'line_descr': 'ΑΝΩ Ν. ΣΜΥΡΝΗ Α - ΣΤ. ΣΥΓΓΡΟΥ ΦΙΞ (ΚΥΚΛΙΚΗ)',
    'line_descr_eng': 'ANO N. SMYRNI A - ST. SYGGROY FIX ',
    'line_id': '137',
    'line_id_gr': '137',
    'sdc_code': '97',
    'terma': 'ΑΝΩ ΝΕΑ ΣΜΥΡΝΗ ',
    'terma_en': 'ANO NEA SMIRNI'},
    {
    'afetiria': 'ΑΝΩ ΝΕΑ ΣΜΥΡΝΗ ',
    'afetiria_en': 'ANO NEA SMIRNI',
    'line_code': '1031',
    'line_descr': 'ΑΝΩ Ν. ΣΜΥΡΝΗ Β - ΣΤ. ΣΥΓΓΡΟΥ ΦΙΞ (ΚΥΚΛΙΚΗ)',
    'line_descr_eng': 'ANO N. SMYRNI V - ST. SYGGROY FIX ',
    'line_id': '136',
    'line_id_gr': '136',
    'sdc_code': '97',
    'terma': 'ΑΝΩ ΝΕΑ ΣΜΥΡΝΗ ',
    'terma_en': 'ANO NEA SMIRNI'}]

Παρ ότι έχουν ίδια αφετηρία και τέρμα, έχουν διαφορετικό line_id, άλλα ίδιο ml_code.
Αυτό συμβαίνει γιατί πιθανότατα ακολουθούν διαφορετική διαδρομή. (confirmation needed)
