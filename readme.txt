
This app lets people study Mandarin Chinese vocabulary in a cohesive incremental way.


The app lists characters in order of their usage frequency. Each character links to a page displaying the character's definition and pronunciation as well as all combinations of the character with other characters of equal or higher usage frequency which form words. The image of the character links to a public dictionary of Mandarin for more information. The listed words also link to their corresponding pages with this dictionary site. 

The user is intended build their knowledge of words and characters by starting from the beginning of the list and learning characters and words in order. This way users will learn the most commonly used characters first and knowledge of new characters and new words will always be anchoring to previously known characters. 

The app visually color codes which characters are known by the user to allow quick review. 



==installation==
After pulling the project folders cd to the mandarin_vocab_builder folder and run the following commands

*set up and activate venv*
python3 -m venv testenv
source testenv/bin/activate

*install django*
python -m pip install django

*set up database*
pypython manage.py makemigrations graph_builder
python manage.py migrate

*populate tables. This builds the character and Word dictionaries and may take a minute or two.*
python manage.py shell < scripts/populate_tables.py 


*start server*
python manage.py runserver

== using app == 
*surf to localhost:8000/mandarin-graph/dashboard/*
*click "Login"*
*click "Register" to make a user account and follow directions. Once the user account is created the site will take you back to the dashboard page*
*click "Character Index Page >". You may click on characters to see their pages and set them as known or unknown within the context of the just-created user account*
*each character's page despairs a large image of the character. With Pin1yin1 pronunciation and definition under it. 

T





===technical description===
Characters can be viewed as nodes in a directed graph. Edges connect pairs of characters which form  a word and point from the first character of the word to the second.

This structure is implemented with the Character and Word models. Character has a nonsymmetrical many-to-many relationship to itself through Word. 

Character contains fields for the standard symbol reperesenting a character, an integer representing the usage frequency rank, the definition of the character, and the pin1yin1 pronunciation of the character. 

Word contains fields for the usage frequency rank of a word, the definition of the word and its pin1yin1 pronunciation. 

This app also needs to keep track of which characters a user reports to know. This is implemented as a many-to-many relationship between Character and the Django User model.  

<some character>.known_by.all() is the set of users who know <some character>.
<some user>.character_set.all() is the set of characters known by <some user>






================
===BACKGROUND===
================


Main areas of focus in learning Standard Mandarin Chinese(SMC) are

	1) The phonetic system of SMC
	2) Grammar
	3) The writing system
	4) vocabulary

Each of these can be future subdivided into sub-skills which can be either passive or productive. 




1) The Phonetic System of SMC

	SKILLS
	1.1 - auditory syllable recognition
	1.2 - verbal syllable production
	1.3 - pinyin


---description---
Sounds in SMC can be dived into syllables. Syllables are defined by the values of three parts: a starting component called an initial, an ending component called a final, and the overall tone. 

There are 
	- 22 possible initials
	- 39 finals
	- 4 tones 

Not all combinations of initials and finales are realized or possible in SMC.

Pinyin is the romanization system for SMC used widely in main land China and around the world. Each syllable in SMC can be phonetically written using latin letters in the Pinyin system. The name 'Pinyin' is itself the Pinyin romanization of the system's name in SMC.
-----------------




2) Gramar

	SKILLS
	2.1 - productive skills
	2.2 - passive skills

---description---
The grammar of SMC is simple, often follows sentence templates with interchangeable parts, has no grammatical gender, number, verb conjugation, or verb tense. 

There are also several common features not largely present in Indo-European languages which pose learning challenges.
-----------------




3) The writing system

	SKILLS
	3.1 - knowledge of the radical system
		3.1.1 - ability to recognize all forms of all radicles
		3.1.2 - ability to write all forms of all radicles
	3.2 - vocabulary of SMC characters
		3.2.1 - recognition of SMC characters
			3.2.1.1 - knowledge of possible pronunciation 
			3.2.1.2 - knowledge of meaning 
		3.2.2 - production of SMC characters
			3.2.2.1 - ability to hand write a character from scratch
			3.2.2.2 - ability to type characters

---description---
The writing system of SMC consists a set of around 3000 commonly used logographic characters. 

Each character is built out of smaller meaning baring pieces called radicles. There are 214 radicles. The exact way radicals fit together and are organized to produce a character is unique to each character although there are several common schemas which are typically followed.

Each character phonetically represents a single spoken syllable. 

Some characters represent different syllables in different contexts.

Knowing how to write and read characters demands the intermediate skill of full knowledge of the radical system.
-----------------




4) vocabulary

	SKILLS
	4.1 word recognitin 
		4.1.1 knowledge of meaning and grammatical attributes
	4.2 word production

---description---
Words in SMC have well defined meanings and grammatical attributes. 

Although a word may be composed of any number of characters, the vast majority of words are composed of two characters with a smaller set of common words being composed of one. 
Knowing how to write and read characters demands the intermediate skill of full knowledge of the radical system.
-----------------
