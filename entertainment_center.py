# -*- coding: UTF-8 -*-
import media
import fresh_tomatoes

# Avengers 4
avengers4_storyline = "- I am inevitable! - I am Iron Man!!!"
avengers4_image = "https://bkimg.cdn.bcebos.com/pic/2cf5e0fe9925bc31a5ffa7e950df8db1cb137025?\
x-bce-process=image/watermark,g_7,image_d2F0ZXIvYmFpa2UyNzI=,xp_5,yp_5"

# Avatar
avatar_storyline = "The film focuses on human beings who put on avatar's \
body and fly to distant planet Pandora to extract resources."
avatar_image = "https://gss0.bdstatic.com/94o3dSag_xI4khGkpoWK1HF6hhy/bai\
ke/c0%3Dbaike220%2C5%2C5%2C220%2C73/sign=8983a693612762d09433acedc185639\
f/eaf81a4c510fd9f9f7454cd9272dd42a2834a42b.jpg"

# Ready Player One
readyplayerone_storyline = "Tells the story of a real-life rootless, addicting \
games big boy, with in-depth analysis of virtual game designers, enough \
trials to find hidden in cary three keys, successful customs clearance \
games, and also harvested the story of a net to love his girlfriend"
readyplayerone_image = "https://gss1.bdstatic.com/9vo3dSag_xI4khGkpoWK1HF6hh\
y/baike/c0%3Dbaike272%2C5%2C5%2C272%2C90/sign=ae023e680b0828387c00d446d9f0c2\
64/279759ee3d6d55fb3b86e35161224f4a20a4dd01.jpg"

# Deadpool2
deadpool2_storyline = "Deadpool 2 is the sequel to 20th century fox's 2016 \
action comedy deadpool."
deadpool2_image = "https://gss0.bdstatic.com/94o3dSag_xI4khGkpoWK1HF6hhy/ba\
ike/c0%3Dbaike150%2C5%2C5%2C150%2C50/sign=bd1f769aa351f3ded7bfb136f5879b7a/40\
34970a304e251fb5c35aa8ab86c9177f3e53ad.jpg"

# Iron Man 3
ironman3_storyline = "The story takes place at the end of the avengers in \
New York, and tells the story of Tony stark's life being destroyed by a \
powerful enemy."
ironman3_image = "https://gss1.bdstatic.com/9vo3dSag_xI4khGkpoWK1HF6hhy/ba\
ike/c0%3Dbaike180%2C5%2C5%2C180%2C60/sign=1c830a5c3f01213fdb3e468e358e5db4/ca\
1349540923dd54c7dd99edd709b3de9d82488c.jpg"

# star war
starwarI_storyline = "Anakin skywalker, a Star Wars start."
starwarI_image = "https://gss1.bdstatic.com/-vo3dSag_xI4khGkpoWK1HF6hhy/ba\
ike/c0%3Dbaike116%2C5%2C5%2C116%2C38/sign=98778280d3c8a786aa27425c0660a258/d3\
1b0ef41bd5ad6e60ac469083cb39dbb6fd3c76.jpg"

# define instance
avengers4 = media.Movie("The Avengers 4", "3", avengers4_image,
                          "XMzk1NDI4OTc3Ng", avengers4_storyline,)
readyplayerone = media.Movie("Ready Player One", "3", readyplayerone_image,
                             "XMzQ3MzcyMzI2NA", avatar_storyline)
deadpool2 = media.Movie("Deadpool 2", "3", deadpool2_image,
                        "XMzU1MDQxOTAwNA", deadpool2_storyline)
ironman3 = media.Movie("Iron Man 3", "3", ironman3_image,
                       "XNTIyNzg1Nzg4",  ironman3_storyline)
avatar = media.Movie("Avatar", "2", avatar_image,
                     "XMzQ2Mjg5NzEzNg", avatar_storyline)
starwarI = media.Movie("Star Wars Episode I", "1", starwarI_image,
                       "XOTI5MzU2ODAw", starwarI_storyline)

# create movie list and generate website
movies = [avengers4, avatar, readyplayerone, deadpool2, ironman3, starwarI]

fresh_tomatoes.open_movies_page(movies)
