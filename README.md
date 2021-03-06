﻿# Musescore-Stats

Python script to gather statistics about a user and his/her music sheets on [Musescore](https://musescore.com). 

It needs `selenium` and `prettytable` extensions in order to work ; all requirements are stored in `requirements.txt` you can install them using `pip` :

```
pip install -r requirements.txt
```
Now, either you have a customized Musescore URL of the form `https://musescore.com/[username]`, or you have to locate the user ID (you can find it in a profile )
Just put the HTML under the name `musescore.html` in the same directory, and then you can run the script

Example of execution :

```
  __  __                                                      ____   _          _
 |  \/  | _   _  ___   ___  ___   ___  ___   _ __  ___       / ___| | |_  __ _ | |_  ___
 | |\/| || | | |/ __| / _ \/ __| / __|/ _ \ | '__|/ _ \ _____\___ \ | __|/ _` || __|/ __|
 | |  | || |_| |\__ \|  __/\__ \| (__| (_) || |  |  __/|_____|___) || |_| (_| || |_ \__ |
 |_|  |_| \__,_||___/ \___||___/ \___|\___/ |_|   \___|      |____/  \__|\__,_| \__||___/

Developped by Clément Sicard


Setting things up...
Everything is ok!

Please enter a valid Musescore username/ID :
> clementsicard 
```

```
************************************* Clément Sicard *************************************
FOLLOWERS:             54
FOLLOWING:              1
NUMBER OF SCORES:      19

Total views:       12,010
Total favorites:      323

"Scylla & Sofiane Pamart - Le monde est à mes pieds" is the most viewed sheet with 3,505 views.
"Scylla & Sofiane Pamart - Le monde est à mes pieds" is the most favorited sheet with 46 favorites.


 Most viewed sheets :

+----+----------------------------------------------------+------------+-----------------+
|    |                     SHEET NAME                     | VIEW COUNT | FAVORITES COUNT |
+----+----------------------------------------------------+------------+-----------------+
| 1  | Scylla & Sofiane Pamart - Le monde est à mes pieds |   3,505    |        46       |
| 2  |        Sofiane Pamart - Le Caire (reupload)        |   1,204    |        35       |
| 3  |              Sofiane Pamart - Planet               |   1,055    |        27       |
| 4  |      Frank Ocean - Self Control (Piano, easy)      |    716     |        34       |
| 5  |         Scylla & Sofiane Pamart - Solitude         |    711     |        25       |
| 6  |         Scylla & Sofiane Pamart - Olympia          |    594     |        18       |
| 7  |               Sofiane Pamart - Paris               |    568     |        16       |
| 8  |             Sofiane Pamart - Carthage              |    554     |        17       |
| 9  |      Scylla & Sofiane Pamart - Constellations      |    548     |        15       |
| 10 |     Scylla & Sofiane Pamart - Seul sur la lune     |    519     |        12       |
| 11 |         Scylla & Sofiane Pamart - Sauvage          |    439     |        9        |
| 12 |    Scylla & Sofiane Pamart - L'enfant et la mer    |    330     |        13       |
| 13 |   Scylla & Sofiane Pamart - Château dans le ciel   |    312     |        12       |
| 14 |              Sofiane Pamart - Alaska               |    265     |        15       |
| 15 | Yann Tiersen - Comptine d'un autre été : La Démarc |    178     |        8        |
| 16 |       Scylla & Sofiane Pamart - Aigle Royal        |    177     |        8        |
| 17 |              Yann Tiersen - La Chute               |    130     |        5        |
| 18 |              Yann Tiersen - La Corde               |    112     |        6        |
| 19 |           Yann Tiersen - Atlantique Nord           |     93     |        2        |
+----+----------------------------------------------------+------------+-----------------+

 Most favorited sheets :

+----+----------------------------------------------------+-----------------+------------+
|    |                     SHEET NAME                     | FAVORITES COUNT | VIEW COUNT |
+----+----------------------------------------------------+-----------------+------------+
| 1  | Scylla & Sofiane Pamart - Le monde est à mes pieds |        46       |   3,505    |
| 2  |        Sofiane Pamart - Le Caire (reupload)        |        35       |   1,204    |
| 3  |      Frank Ocean - Self Control (Piano, easy)      |        34       |    716     |
| 4  |              Sofiane Pamart - Planet               |        27       |   1,055    |
| 5  |         Scylla & Sofiane Pamart - Solitude         |        25       |    711     |
| 6  |         Scylla & Sofiane Pamart - Olympia          |        18       |    594     |
| 7  |             Sofiane Pamart - Carthage              |        17       |    554     |
| 8  |               Sofiane Pamart - Paris               |        16       |    568     |
| 9  |              Sofiane Pamart - Alaska               |        15       |    265     |
| 10 |      Scylla & Sofiane Pamart - Constellations      |        15       |    548     |
| 11 |    Scylla & Sofiane Pamart - L'enfant et la mer    |        13       |    330     |
| 12 |   Scylla & Sofiane Pamart - Château dans le ciel   |        12       |    312     |
| 13 |     Scylla & Sofiane Pamart - Seul sur la lune     |        12       |    519     |
| 14 |         Scylla & Sofiane Pamart - Sauvage          |        9        |    439     |
| 15 | Yann Tiersen - Comptine d'un autre été : La Démarc |        8        |    178     |
| 16 |       Scylla & Sofiane Pamart - Aigle Royal        |        8        |    177     |
| 17 |              Yann Tiersen - La Corde               |        6        |    112     |
| 18 |              Yann Tiersen - La Chute               |        5        |    130     |
| 19 |           Yann Tiersen - Atlantique Nord           |        2        |     93     |
+----+----------------------------------------------------+-----------------+------------+

Press [ENTER] to see stats for another user, [Q] to exit
>
```
