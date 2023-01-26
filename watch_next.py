# The objective of this program is to create a movie recommendation algorithm
# that works by using spaCy to compare the description of a recently watched
# movie to those of other movies stored in a database (a text file).

# Import spaCy.
import spacy

# Specify the model to be used.
nlp = spacy.load('en_core_web_md')


# Define the description to be used for comparison.
just_watched = '''Will He Save Their World Or Destroy It? When the Hulk
               becomes too dangerous for the Earth,the Illuminati trick 
               Hulk into a shuttle and launch him into space to a planet 
               where the Hulk can live in peace. Unfortunately, Hulk lands 
               on the planet Sakaar where he is sold into slavery and 
               trained as a gladiator.'''

# Define a function that takes in a movie description as parameter and returns
# the most similar movie in 'movies.txt' using spacy.similarity.
def watch_next(description):
    # Read in 'movies.txt' lines.
    with open("movies.txt", "r") as films:
        movies = films.readlines()

    # Set the reference sentence.
        model_sentence = nlp(description)

        # Initiate helper variables.
        highest_similarity = 0
        similar_movie = ''

        # Loop through all the movies to find the most similar description.
        for movie in movies:
            similarity = nlp(movie[9:]).similarity(model_sentence)
            if similarity >= highest_similarity:
                highest_similarity = similarity
                similar_movie = movie
    return (f'''You may like '{similar_movie[:7]}' with a similarity index of
{highest_similarity} and the following description: \n  {similar_movie[9:]}''')
    

print()
print("________________Movie List_________________________")

# Read in 'movies.txt' lines.
# Loop through all the movies and print out the details for easy reference.
with open("movies.txt", "r") as movies:
    for line in movies:
        title = line[0:7]
        synopsis = (line[9:])
        print(f"{title} = {synopsis}")

print()
print("________________Watch Next Suggestion_________________________")

# Call the watch_next() function with just_watched as parameter.
print(watch_next(just_watched))


