import sys
import os

def read_movies(movies_file):
    """Reads the movie file.

    Args:
        movies_file: Path of the input text file.

    Returns:
        A list of the movie titles.
    """

    movies = []
    with open(movies_file , 'r') as lines:
        for line in lines:
            movie = line.strip()
            if movie:
                movies.append(movie)

    return movies

def read_ratings(ratings_file):
    """Reads the ratings_file and builds the ratings dictionary.

    Args:
        ratings_file: Path of the input ratings text file.

    Returns:
      A dictionary as {username: [(movie_index, rate), ....]}
    """

    ratings = {}

    with open(ratings_file, 'r') as lines:
        for line in lines:
            line = line.strip()

            if not line:
                continue

            username, movie_index, rating = line.split(',')

            username = username.strip()
            movie_index = int(movie_index)
            rating = int(rating)

            if username not in ratings:
                ratings[username] = []

            ratings[username].append((movie_index, rating))

    return ratings

def similarity_calculation(list1, list2):
    """
    Calculates the similarity score between two users.
    Two ratings are similar if and only if they differ by at most 1 point.

    Args:
        list1: (movie_index, rating) tuples of the first user.
        list2: (movie_index, rating) tuples of the second user.

    Returns:
        Similar ratings divided by cmmon movies.
        0.0 if no common movies.
    """

    common_movies = 0
    similar_ratings = 0

    for (movie1, rating1) in list1:
        for (movie2, rating2) in list2:
            if movie1 == movie2:
                common_movies += 1

                if abs(rating1-rating2) <= 1:
                    similar_ratings += 1

    if common_movies == 0:
        return 0.0
    
    return (similar_ratings/common_movies)

def similarity_matrix(ratings):
    """
    Calculates the similarity of every user pair tuple once.

    Args:
        ratings: Dictionary in the form {usernmae: [(movie_index, rating)], ...}

    Returns: 
        A dictionary as {(user1, user2): score}.
    """

    similarities = {}
    names = list(ratings.keys())

    for i in range(len(names)):
        for j in range(i+1 ,  len(names)):
            user1 = names[i]
            user2 = names[j]

            similarities[(user1,user2)] = similarity_calculation(ratings[user1], ratings[user2])

    return similarities

def get_similarity(similarities, user1, user2):
    """
    Helper Function: Returns the similarity of two users, whatever the order of names.

    Args:
        similarities: Dictionary in the form {(user1, user2): score}.
        user1: Name of the first user.
        user2: Name of the second user.

    Returns:
        The stored similarity score, or 0.0 if the pair is not found.

    """

    if (user1, user2) in similarities:
        return similarities[(user1, user2)]
    
    if (user2, user1) in similarities:
        return similarities[(user2, user1)]

    return 0.0

def recommendation(user, movies, ratings, similarities):
    """Creates the sorted movie recommendations for a user.

    Only unwatched movies that at least one similar user (similarity >= 0.7) rated 4 or higher are recommended.

    Args:
        user: Name of the user who gets the recommendations.
        movies: List of movie titles (the index is the movie index).
        ratings: Dictionary in the form {username: [(movie_index, rating), ...]}.
        similarities: Dictionary in the form {(user1, user2): score}.

    Returns:
        A list of [highest_rating, number_of_users, title, names] lists.
        It is sorted by highest rating and number of users (both descending), then by title (alphabetical). 
        names holds only the similar users who gave the highest rating, in alphabetical order.
    """

    similarity_threshold = 0.7
    rating_threshold = 4

    similar = [] 

    for other in ratings:
        if other != user and get_similarity(similarities, user, other) >= similarity_threshold:
            similar.append(other)

    watched = []
    for (movie_index, rating) in ratings[user]:
        watched.append(movie_index)

    recoms = []
    for m in range(len(movies)):
        if m in watched:
            continue

        user_names = []
        user_ratings = []

        for other in similar:
            for (movie_index, rating) in ratings[other]:
                if movie_index == m and rating >= rating_threshold:
                    user_names.append(other)
                    user_ratings.append(rating)

        if len(user_names) == 0:
            continue

        highest = 0

        for r in user_ratings:
            if r > highest:
                highest = r

        names = []

        for k in range(len(user_names)):
            if user_ratings[k] == highest:
                names.append(user_names[k])

        names.sort() #alphabetical order is default 

        recoms.append([highest, len(user_names), movies[m], names ])

    recoms.sort(key = lambda x: (-x[0], -x[1], x[2])) #for 0th and 1st indices decending order is required, hence -x used
    return recoms



def main():
    """Reads the files given on the command line and writes the recommendations to the output file.

    Command line arguments (in order): movies_file, ratings_file, output_file. 
    The output file is saved in the program's directory.
    """

    if len(sys.argv) != 4:
            print("ERROR! Not enough argumnets.\nCorrect Run Format: python main_p2.py <movies_file> <ratings_file> <output_file>")
            return
    
    movies_file = sys.argv[1]
    ratings_file = sys.argv[2]
    output_file = sys.argv[3]
    
    main_dir = os.path.dirname(os.path.abspath(__file__))
    movies_path = os.path.join(main_dir, movies_file)
    ratings_path = os.path.join(main_dir, ratings_file)
    output_path = os.path.join(main_dir, output_file)

    movies = read_movies(movies_path)
    ratings = read_ratings(ratings_path)
    similarities = similarity_matrix(ratings)

    with open(output_path, 'w') as out:

        for user in ratings:
            out.write("Recommendations for " + user + ":\n")

            recoms = recommendation(user, movies, ratings, similarities)

            for i in range(len(recoms)):
                best = recoms[i][0]
                title = recoms[i][2]
                names = recoms[i][3]

                out.write(f"{i + 1}. {title} (rated {best}/5 by similar users: {', '.join(names)})\n")

            out.write("\n")
    
    out.close()

if __name__ == "__main__":
    main()
