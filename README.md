# Σκάκι

**Βιβλιοθήκες**

* re build-in library
* [python-chess](https://python-chess.readthedocs.io/en/latest/index.html)
  * Εγκατάσταση της βιβλιοθήκης python-chess
    ```
    $ pip install chess
    ```

**Σχετικός κώδικας στο Internet**

* https://github.com/renatopp/pgnparser - PGN Parser - A simple Python PGN parser
* https://github.com/matteson/parse-pgn-files 
* https://github.com/johncheetham/jcchess - A chess GUI to play against chess engines
* https://github.com/liudmil-mitev/Simple-Python-Chess
* https://github.com/TheRazorace/Python-Chess-Engine


**PGN format**

* https://www.chess.com/terms/chess-notation
* [Αναλυτική προδιαγραφή του PGN](http://www.saremba.de/chessgml/standards/pgn/pgn-complete.htm)

<!-- * https://www.chessclub.com/help/PGN-spec -->

**PGN Games**

* [19921104-r29-fischer-spassky.pgn](./game1.pgn) game from https://en.wikipedia.org/wiki/Portable_Game_Notation
* https://theweekinchess.com/twic
* https://github.com/rozim/ChessData
* http://www.pgnmentor.com/files.html

**Πτυχιακές εργασίες**

* [ΑΝΑΠΤΥΞΗ ΣΚΑΚΙΣΤΙΚΗΣ ΜΗΧΑΝΗΣ - Δασούλας, 2021](https://nemertes.library.upatras.gr/jspui/bitstream/10889/15302/1/%CE%94%CE%B9%CF%80%CE%BB%CF%89%CE%BC%CE%B1%CF%84%CE%B9%CE%BA%CE%AE%20%CE%95%CF%81%CE%B3%CE%B1%CF%83%CE%AF%CE%B1%20-%20%CE%94%CE%B1%CF%83%CE%BF%CF%8D%CE%BB%CE%B1%CF%82%20%CE%99%CF%89%CE%AC%CE%BD%CE%BD%CE%B7%CF%82.pdf)
* [Document Digitization for Chess Scorecards - Béla Horváth, Colin Dreher, 2020](https://www.zhaw.ch/storage/engineering/institute-zentren/cai/BA20_Digitization_of_Chess_Scorecards_Horvath_Dreher.pdf)

**chess board**

* [How to Code a Simple Chess Game in Python](https://medium.com/codex/how-to-code-a-simple-chess-game-in-python-9a9cb584f57)
  * https://github.com/xsanon/chess
* [Making Chess in Python](https://levelup.gitconnected.com/chess-python-ca4532c7f5a4) με το pygame

**Συζητήσεις σε forums**

* https://chess.stackexchange.com/questions/28870/render-a-chessboard-from-a-pgn-file


**Ενδιαφέροντα**

* http://www.picochess.org/


## Αποσπάσματα κώδικα

* [snippet1.py](./snippet1.py) - ανάγνωση αρχείου pgn, εντοπισμός πληροφοριών π.χ. παίκτες, κινήσεις
* [snippet2.py](./snippet2.py) - parse κινήσεων με το re, εύρεση πλήθους κινήσεων παιχνιδιού
* [snippet3.py](./snippet3.py) - ανάγνωση αρχείου pgn με το module python-chess, εμφάνιση στοιχείων αγώνα και εξέλιξης του ταμπλό στη γραμμή εντολών
* [snippet4.py](./snippet4.py) - ανάγνωση αρχείου pgn με το module python-chess, αποθήκευση του τελικού ταμπλό του αγώνα ως αρχείο svg
* [nb1.ipynb](./nb1.ipynb) - jupyter notebook με αποσπάσματα κώδικα (python-chess)
* [nb2.ipynb](./nb2.ipynb) - jupyter notebook με διάφορα αποσπάσματα κώδικα (ανάγνωση αρχείου και re)
* [5_1_sol_oop.py](./5_1_sol_oop.py) - παράδειγμα λίστας με scrollbar 

---

* [model.py](./model.py) - module που περιέχει τον ορισμό της κλάσης PgnGame
* [utils.py](./utils.py) - module με βοηθητικές συναρτήσεις για ανάγνωση αρχείων pgn
* [main.py](./main.py) - πειραματισμοί (κάθε πείραμα μπορεί να κλήθεί περνώντας κατάλληλο όρισμα εκτέλεσης)
  * Τοποθέτηση σε μια λίστα όλων των κινήσεων ενός παιχνιδιού
    ```
    $ python main.py 1
    ['games\\19921104-r29-fischer-spassky.pgn', 'games\\2003.pgn', 'games\\2004.pgn', 'games\\2005.pgn', 'games\\2006.pgn', 'games\\2007.pgn', 'games\\2008.pgn', 'games\\2009.pgn', 'games\\2010.pgn']
    GAME:  "Wijk aan Zee I" White: "Kramnik" Black: "Ivanchuk" Result: "1/2-1/2"
    MOVES:  [('1', 'e4', 'c5'), ('2', 'Nf3', 'd6'), ('3', 'd4', 'cxd4'), ('4', 'Nxd4', 'Nf6'), ('5', 'Nc3', 'Nc6'), ('6', 'Bg5', 'e6'), ('7', 'Qd2', 'a6'), ('8', 'O-O-O', 'Bd7'), ('9', 'f3', 'Be7'), ('10', 'Kb1', 'b5'), ('11', 'Nxc6', 'Bxc6'), ('12', 'Bxf6', 'Bxf6'), ('13', 'Qxd6', 'Qxd6'), ('14', 'Rxd6', 'Rc8'), ('15', 'Ne2', 'Ke7'), ('16', 'Rd3', 'Rhd8'), ('17', 'Nc1', 'a5'), ('18', 'a3', 'b4'), ('19', 'axb4', 'axb4'), ('20', 'Rxd8', 'Rxd8'), ('21', 'Be2', 'h5'), ('22', 'Nd3', 'Rd4'), ('23', 'h4', 'Bb5'), ('24', 'g3', 'b3'), ('25', 'Re1', 'Bxd3'), ('26', 'Bxd3', 'Be5'), ('27', 'f4', 'Bd6'), ('28', 'Re3', 'bxc2+'), ('29', 'Kxc2', 'Bc5'), ('30', 'Rf3', 'Ra4'), ('31', 'e5', 'Bd4'), ('32', 'Be2', 'g6'), ('33', 'Rb3', 'Bf2'), ('34', 'Rf3', 'Be1'), ('35', 'Bd3', 'Kf8'), ('36', 'Re3', 'Bf2'), ('37', 'Rf3', 'Be1'), ('38', 'Kd1', 'Ra1+'), ('39', 'Ke2', 'Bb4'), ('40', 'Bb5', 'Ra2'), 
    ('41', 'Rb3', 'Ba3')]
    ```
  * Αλληλεπίδραση με το χρήστη για επιλογή ένός αρχείου pgn, επιλογή ενός παιχνιδιού μέσα σε αυτό και παρακολούθηση των κινήσεων του παιχνιδιού μια προς μια.
    ```
    $ python main.py 2
    1. games\19921104-r29-fischer-spassky.pgn
    2. games\2003.pgn
    3. games\2004.pgn
    4. games\2005.pgn
    5. games\2006.pgn
    6. games\2007.pgn
    7. games\2008.pgn
    8. games\2009.pgn
    9. games\2010.pgn
    Select pgn file: 2
    1. "Wijk aan Zee I" White: "Ponomariov" Black: "Bareev" Result: "0-1"
    2. "Wijk aan Zee I" White: "Kramnik" Black: "Ivanchuk" Result: "1/2-1/2"
    3. "Wijk aan Zee I" White: "Krasenkow" Black: "Karpov" Result: "0-1"
    4. "Wijk aan Zee I" White: "Shirov" Black: "Timman" Result: "1/2-1/2"
    5. "Wijk aan Zee I" White: "Grischuk" Black: "Van Wely" Result: "1/2-1/2"
    ...
    1.   "Wijk aan Zee III" White: "Bu" Black: "Cebalo" Result: "1-0"
    2.   "Wijk aan Zee III" White: "Peek" Black: "Cherniaev" Result: "1/2-1/2"
    3.   "Wijk aan Zee III" White: "Cherniaev" Black: "Janssen" Result: "1-0"
    4.   "Wijk aan Zee III" White: "Cebalo" Black: "Peek" Result: "1-0"
    5.   "Wijk aan Zee III" White: "Boom" Black: "Bu" Result: "0-1"
    6.   "Wijk aan Zee III" White: "Lobron" Black: "L'Ami" Result: "1-0"
    7.   "Wijk aan Zee III" White: "Erwich" Black: "Strating" Result: "1/2-1/2"
    Select game: 2
    GAME:  "Wijk aan Zee I" White: "Kramnik" Black: "Ivanchuk" Result: "1/2-1/2"
    1 move, white: e4, black: c5
    Press Enter to continue...
    2 move, white: Nf3, black: d6
    Press Enter to continue...
    3 move, white: d4, black: cxd4
    Press Enter to continue...
    ...
    39 move, white: Ke2, black: Bb4
    Press Enter to continue...
    40 move, white: Bb5, black: Ra2
    Press Enter to continue...
    41 move, white: Rb3, black: Ba3
    Press Enter to continue...
    ```
  * Αλληλεπίδραση με το χρήστη για επιλογή ένός αρχείου pgn, επιλογή ενός παιχνιδιού μέσα σε αυτό και παρακολούθηση των κινήσεων του παιχνιδιού μια προς μια και απεικόνιση του ταμπλό με το python-chess
    ```
    $ python main.py 3
    1. games\19921104-r29-fischer-spassky.pgn
    2. games\2003.pgn
    3. games\2004.pgn
    4. games\2005.pgn
    5. games\2006.pgn
    6. games\2007.pgn
    7. games\2008.pgn
    8. games\2009.pgn
    9. games\2010.pgn
    Select pgn file: 2
    1. "Wijk aan Zee I" White: "Ponomariov" Black: "Bareev" Result: "0-1"
    2. "Wijk aan Zee I" White: "Kramnik" Black: "Ivanchuk" Result: "1/2-1/2"
    3. "Wijk aan Zee I" White: "Krasenkow" Black: "Karpov" Result: "0-1"
    4. "Wijk aan Zee I" White: "Shirov" Black: "Timman" Result: "1/2-1/2"
    5. "Wijk aan Zee I" White: "Grischuk" Black: "Van Wely" Result: "1/2-1/2"
    ...
    1.   "Wijk aan Zee III" White: "Bu" Black: "Cebalo" Result: "1-0"
    2.   "Wijk aan Zee III" White: "Peek" Black: "Cherniaev" Result: "1/2-1/2"
    3.   "Wijk aan Zee III" White: "Cherniaev" Black: "Janssen" Result: "1-0"
    4.   "Wijk aan Zee III" White: "Cebalo" Black: "Peek" Result: "1-0"
    5.   "Wijk aan Zee III" White: "Boom" Black: "Bu" Result: "0-1"
    6.   "Wijk aan Zee III" White: "Lobron" Black: "L'Ami" Result: "1-0"
    7.   "Wijk aan Zee III" White: "Erwich" Black: "Strating" Result: "1/2-1/2"
    Select game: 2
    GAME:  "Wijk aan Zee I" White: "Kramnik" Black: "Ivanchuk" Result: "1/2-1/2"
    r n b q k b n r
    p p p p p p p p
    . . . . . . . .
    . . . . . . . .
    . . . . . . . .
    . . . . . . . .
    P P P P P P P P
    R N B Q K B N R
    1 move, white: e4, black: c5
    r n b q k b n r
    p p . p p p p p
    . . . . . . . .
    . . p . . . . .
    . . . . P . . .
    . . . . . . . .
    P P P P . P P P
    R N B Q K B N R
    Press Enter to continue...
    ...
    Press Enter to continue...
    39 move, white: Ke2, black: Bb4
    . . . . . k . .
    . . . . . p . .
    . . . . p . p .
    . . . . P . . p
    . b . . . P . P
    . . . B . R P .
    . P . . K . . .
    r . . . . . . .
    Press Enter to continue...
    40 move, white: Bb5, black: Ra2
    . . . . . k . .
    . . . . . p . .
    . . . . p . p .
    . B . . P . . p
    . b . . . P . P
    . . . . . R P .
    r P . . K . . .
    . . . . . . . .
    Press Enter to continue...
    41 move, white: Rb3, black: Ba3
    . . . . . k . .
    . . . . . p . .
    . . . . p . p .
    . B . . P . . p
    . . . . . P . P
    b R . . . . P .
    r P . . K . . .
    . . . . . . . .
    Press Enter to continue...
    ```