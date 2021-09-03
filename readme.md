## Description
Most Mandarin words are two characters long. Because of this characters can be viewed as nodes in a directed graph with words defining the edges. Learning vocabulary can then be understood as exploring this directed graph. One learning strategy is to start at the most frequently used character and add new characters to your vocabulary in order of frequency. Each time a new character is learned the words connecting it to the previously known subgraph are also learned. 

This approach to vocabulary building is explicitly followed by this app. Each character's page displays a list of all words connecting the character to the set of previously learned characters which is assumed to consist of the set of characters with usage frequency less than or equal to the character in question. The character's definition and pronunciation are also displayed.

## Internals 

The list of characters, the relationships between them defined by words, and additional information such as definitions and pronunciation for characters and words, are handled by the Character and Word models. Character has a non-symmetrical many-to-many relationship to itself through Word and contains additional fields to store a character's standard symbol, the character's usage frequency rank, the definition of the character, and its pin1yin1 pronunciation. Word contains fields for the usage frequency rank of a word, the definition of the word, and its pin1yin1 pronunciation.

The app also tracks which characters a user reports to have successfully learned. This is implemented as a many-to-many relationship between Character and the Django User model and is displayed to the user through color coding of known and unknown characters throughout the app.

```sh
<some character>.known_by.all()
```
is the set of users who know a character and
```sh
<some user>.character_set.all() 
```
is the set of characters known by a user.

## Installation
After pulling the project folders cd into the mandarin_vocab_builder folder and run the following commands:

*set up and activate venv*
```sh
python3 -m venv testenv
source testenv/bin/activate
```
*install django*
```sh
python -m pip install django
```
*set up database*
```sh
python manage.py makemigrations graph_builder
python manage.py migrate
```
*populate tables -- may take minute or two*
```sh
python manage.py shell < scripts/populate_tables.py 
```
*start server*
```sh
python manage.py runserver
```

## Using App
- Surf to localhost:8000/mandarin-graph/dashboard/
- Click "Login"
- Click "Register" to make a user account and follow directions. Once the user account is created the site will take you back to the dashboard page 
- Click "Character Index Page >". You may click on characters to see their pages and set them as known or unknown within the context of the just-created user account. 
- Each character's character page has a clickable large image of the character which links to the characgter's purpleculter page for more info. The links, desplayed as arrows "- ->" are also clickable at take you to the corosponding word's purplecutler page for a defintion and more information. 



