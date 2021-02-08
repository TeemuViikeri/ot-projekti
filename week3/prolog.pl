fish(_).
dog(odie).
cat(garfield).
human(liz).
human(jon).
animal(X) :- cat(X); dog(X); human(X); fish(X).
tail_color(garfield, orange).
tail_color(odie, black).
has_tail(X) :- tail_color(X,_).
has_tail(unix).
first_likes_second(odie, garfield).
first_likes_second(jon, garfield).
first_likes_second(jon, odie).
first_likes_second(jon, liz).
first_likes_second(jon, fish).