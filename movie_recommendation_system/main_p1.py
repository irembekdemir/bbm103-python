import sys
import os

def read_movies(movies_file):
    """Reads the movie file and returns the movie titles as a list.

    The index of a title in the list is its movie index.

    Args:
        movies_file: Path of the movies text file.

    Returns:
        A list of movie titles.
    """

    movies = []
    with open(movies_file , 'r') as lines:
        for line in lines:
            movie = line.strip()
            if movie:
                movies.append(movie)

    return movies

def read_ratings(ratings_file, number_of_movies):
    """Reads the ratings file and build the users list and ratings 2D list.

    A rating of 0 means the user has not rated that movie.

    Args:
        ratings_file: Path of the ratings text file. 
        Each line has the form <user_name>,<movie_index>,<rating>.

        number_of_movies: Number of movies in the movies file.

    Returns:
        A tuple (users, ratings) where users[i] is the name of the i-th user and ratings[i][m] is the i-th user's rating for the m-th movie.
    """

    users = [] # users[i]: name of the ith user
    ratings = [] #ratings[i][m]: ith user's rating for mth movie

    with open(ratings_file, 'r') as lines:
        for line in lines:
            line = line.strip()

            if not line:
                continue

            username, movie_index, rating = line.split(',')

            username = username.strip()
            movie_index = int(movie_index)
            rating = int(rating)

            if username not in users:
                users.append(username)
                ratings.append([0]*number_of_movies)

            ratings[users.index(username)][movie_index]=rating 

    return users , ratings

def similarity_calculation(u1_ratings, u2_ratings):
    """Calculates the similarity score of two users.

    Two ratings for the same movie are similar if they differ by at most 1 point. 
    Movies rated 0 (not rated) are ignored.

    Args:
        u1_ratings: Rating list of the first user (one value per movie).
        u2_ratings: Rating list of the second user (one value per movie).

    Returns:
        Number of similar ratings divided by number of common movies.
        Returns 0.0 if the users have no common movies.
    """

    common_movies = 0
    similar_ratings = 0

    for r1, r2 in zip(u1_ratings,u2_ratings):
        if r1!=0 and r2!=0:
            common_movies += 1
            if abs(r1-r2)<=1:
                similar_ratings += 1

    if common_movies == 0:
        return 0.0
    
    return (similar_ratings/common_movies)

def similarity_matrix(ratings):
    """Calculates the similarity score of every user pair.

    Args:
        ratings: 2D list where ratings[i][m] is the i-th user's rating for the m-th movie.

    Returns:
        A 2D list where matrix[i][j] is the similarity between the i-th and the j-th user. 
        The diagonal (a user with themselves) stays 0.0.
    """

    n = len(ratings)
    matrix = []

    for i in range(0,n):
        row = []
        for j in range(0,n):
            row.append(0.0)
        matrix.append(row)

    for i in range(0,n):
        for j in range(0,n):
            if i != j:
                matrix[i][j] = similarity_calculation(ratings[i], ratings[j])
    
    return matrix

def recommendation(i, users, movies, ratings, simm):
    """Create the sorted movie recommendations for one user.

    Only unwatched movies that at least one similar user (similarity >= 0.7) rated 4 or higher are recommended.

    Args:
        i: Index of the user who gets the recommendations.
        users: List of user names.
        movies: List of movie titles (the index is the movie index).
        ratings: 2D list where ratings[i][m] is the i-th user's rating for the m-th movie.
        simm: 2D list of similarity scores between users.

    Returns:
        A list of [highest_rating, number_of_users, title, names] lists.
        It is sorted by highest rating and number of users (both descending), then by title (alphabetical). 
        names holds only the similar users who gave the highest rating, in alphabetical order.
    """

    similarity_threshold = 0.7
    rating_threshold = 4

    similar = [] 

    for j in range(len(users)):
        if j != i and simm[i][j] >= similarity_threshold:
            similar.append(j)

    recoms = []

    for m in range(len(movies)):
        if ratings[i][m] != 0:
            continue

        user_names = []
        user_ratings = []

        for j in similar:
            if ratings[j][m] >= rating_threshold:
                user_names.append(users[j])
                user_ratings.append(ratings[j][m])

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
    """Reads the files given on the command line and write the recommendations.

    Command line arguments (in order): movies_file, ratings_file, output_file. 
    The output file is saved in the program's directory.
    """

    if len(sys.argv) != 4:
            print("ERROR! Not enough argumnets.\nCorrect Run Format: python main_p1.py <movies_file> <ratings_file> <output_file>")
            return
    
    movies_file = sys.argv[1]
    ratings_file = sys.argv[2]
    output_file = sys.argv[3]
    
    main_dir = os.path.dirname(os.path.abspath(__file__))
    movies_path = os.path.join(main_dir, movies_file)
    ratings_path = os.path.join(main_dir, ratings_file)
    output_path = os.path.join(main_dir, output_file)

    movies = read_movies(movies_path)
    users, ratings = read_ratings(ratings_path, len(movies))
    sim = similarity_matrix(ratings)

    with open(output_path, 'w') as out:

        for i in range(len(users)):
            out.write("Recommendations for " + users[i] + ":\n")

            recoms = recommendation(i, users, movies, ratings, sim)

            for j in range(len(recoms)):
                best = recoms[j][0]
                title = recoms[j][2]
                names = recoms[j][3]

                out.write(f"{j + 1}. {title} (rated {best}/5 by similar users: {', '.join(names)})\n")

            out.write("\n")
    
    out.close()

if __name__ == "__main__":
    main()
