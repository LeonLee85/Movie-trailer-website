# -*- coding: UTF-8 -*-
import media
import fresh_tomatoes

# AvengersIII
avengersIII_storyline = "It tells the story of the avengers and their superhero Allies who must be willing \
to sacrifice everything to defeat the universe before it destroys it."
avengersIII_image = "https://gss2.bdstatic.com/9fo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike272%2C5%2\
C5%2C272%2C90/sign=06f0367c57b5c9ea76fe0bb1b450dd65/d1a20cf431adcbef44627e71a0af2edda3cc9f76.jpg"

# Avatar
avatar_storyline = "The film focuses on human beings who put on avatar's body and fly to distant planet Pandora \
to extract resources."
avatar_image = "https://gss0.bdstatic.com/94o3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike220%2C5%2C5%2C2\
20%2C73/sign=8983a693612762d09433acedc185639f/eaf81a4c510fd9f9f7454cd9272dd42a2834a42b.jpg"

# Ready Player One
readyplayerone_storyline = "Tells the story of a real-life rootless, addicting games big boy, with in-depth \
analysis of virtual game designers, enough trials to find hidden in cary three keys, successful customs \
clearance games, and also harvested the story of a net to love his girlfriend"
readyplayerone_image = "https://gss1.bdstatic.com/9vo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike272%2C5%2C5%2C2\
72%2C90/sign=ae023e680b0828387c00d446d9f0c264/279759ee3d6d55fb3b86e35161224f4a20a4dd01.jpg"

# Deadpool2
deadpool2_storyline = "Deadpool 2 is the sequel to 20th century fox's 2016 action comedy deadpool."
deadpool2_image = "https://gss0.bdstatic.com/94o3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike150%2C5%2C5%2C15\
0%2C50/sign=bd1f769aa351f3ded7bfb136f5879b7a/4034970a304e251fb5c35aa8ab86c9177f3e53ad.jpg"

# Iron Man 3
ironman3_storyline = "The story takes place at the end of the avengers in New York, and tells the story\
 of Tony stark's life being destroyed by a powerful enemy."
ironman3_image = "https://gss1.bdstatic.com/9vo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike180%2C5%2C5%2C1\
80%2C60/sign=1c830a5c3f01213fdb3e468e358e5db4/ca1349540923dd54c7dd99edd709b3de9d82488c.jpg"

# star war
starwarI_storyline = "Anakin skywalker, a Star Wars start."
starwarI_image = "https://gss1.bdstatic.com/-vo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike116%2C5%2C5%2C116%2C38/sign\
=98778280d3c8a786aa27425c0660a258/d31b0ef41bd5ad6e60ac469083cb39dbb6fd3c76.jpg"

# define instance
avengersIII = media.Movie("The avengersIII", "3", avengersIII_image, "XMzQ2OTMxMTQ4NA",
                          avengersIII_storyline,)
readyplayerone = media.Movie("Ready Player One", "3", readyplayerone_image, "XMzQ3MzcyMzI2NA",
                             avatar_storyline)
deadpool2 = media.Movie("Deadpool 2", "3", deadpool2_image, "XMzU1MDQxOTAwNA", deadpool2_storyline)
ironman3 = media.Movie("Iron Man 3", "3", ironman3_image, "XNTIyNzg1Nzg4",  ironman3_storyline)
avatar = media.Movie("Avatar", "2", avatar_image, "XMzQ2Mjg5NzEzNg", avatar_storyline)
starwarI = media.Movie("Star War I", "1", starwarI_image, "XOTI5MzU2ODAw", starwarI_storyline)

# create movie list and generate website
movies = [avengersIII, avatar, readyplayerone, deadpool2, ironman3, starwarI]

fresh_tomatoes.open_movies_page(movies)
