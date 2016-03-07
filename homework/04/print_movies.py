movies = ['Finding Nemo', 'A Beautiful Mind', 'The Prestige', 'Inside Out', 'The Pianist']
movies_len = len(movies)

if movies_len == 1 :
    print "My favorite movie is {0}".format(movies[0])

elif movies_len == 2 :
    print "My two favorite movies are {0} and {1}".format(movies[0])

else :
    print "My {0} favorite movies are".format(movies_len),

    for count in range(0,movies_len) :
        movie = movies[count]

        if count != (movies_len-1) :
            print "{0},".format(movie),
        else :
            print "and {0}".format(movie)

        count = count + 1;
