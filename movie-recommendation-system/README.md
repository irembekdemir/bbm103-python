# Movie Recommendation System (Python CLI Project)

A command-line movie recommendation system built in Python.
It reads a list of movies and user ratings, finds users with similar taste, and recommends unwatched movies to each user.

The project has two parts that solve the same problem with different data structures:

- **Part 1:** lists and 2D lists
- **Part 2:** dictionaries and tuples

## ✨ Features
- Reads movies and user ratings from text files
- Calculates a similarity score between every pair of users
- Finds similar users using a similarity threshold
- Recommends only unwatched movies that similar users rated highly
- Shows the highest rating and which similar users gave it
- Sorts recommendations by rating, number of recommending users, and title
- Writes the results to an output file in the program's directory

## 📂 Input Format

`movies.txt` has one movie title per line. The line order gives the movie index (starting from 0):
```
The Shawshank Redemption
The Godfather
The Dark Knight
Pulp Fiction
Fight Club
Forrest Gump
The Matrix
Goodfellas
Inception
The Silence of the Lambs
```

`ratings.txt` has one rating per line in the form `<user_name>,<movie_index>,<rating>`. Ratings are integers between 1 and 5:
```
alice,0,5
alice,1,4
alice,2,5
alice,4,3
bob,0,4
bob,2,5
bob,3,5
bob,5,4
eve,4,5
eve,5,5
eve,6,4
eve,8,3
eve,9,5
```

## 🧠 How It Works

**1. Similarity calculation**
- Find the movies rated by both users.
- If there are no common movies, the similarity is `0`.
- Two ratings are similar if they differ by at most 1 point.
- Similarity = similar ratings / common movies (a value between 0 and 1).

**2. Finding similar users**
- A user is similar if the similarity score is `>= 0.7`.

**3. Generating recommendations**
- Only movies the user has not rated are considered.
- Only ratings of `4` or higher from similar users count.
- The output shows the highest rating and only the users who gave that rating, in alphabetical order.

**4. Sorting**
1. Highest rating (descending)
2. Number of similar users who recommended the movie (descending)
3. Movie title (alphabetical)

## 🧱 Data Structures

**Part 1 (lists and 2D lists)**
```python
users = ["alice", "bob", "eve"]          # users[i] -> name of the i-th user
ratings[i][m]                            # i-th user's rating for the m-th movie (0 = not rated)
sim[i][j]                                # similarity between the i-th and j-th user
```

**Part 2 (dictionaries and tuples)**
```python
ratings = {
    "alice": [(0, 5), (1, 4), (2, 5), (4, 3)],
    "bob":   [(0, 4), (2, 5), (3, 5), (5, 4)]
}

similarities = {
    ("alice", "bob"): 1.0,
    ("alice", "eve"): 0.0,
    ("bob", "eve"): 1.0
}
```
- Each rating is a `(movie_index, rating)` tuple.
- Each user pair is stored only once. `get_similarity()` returns the score whatever the order of the names.

## 🛠️ Functions

| Function | Purpose |
|---|---|
| `read_movies()` | Reads the movie titles into a list |
| `read_ratings()` | Reads the ratings file (2D list in Part 1, dictionary in Part 2) |
| `similarity_calculation()` | Calculates the similarity score of two users |
| `similarity_matrix()` | Calculates the similarity of every user pair |
| `get_similarity()` | Returns a pair's score in any name order (Part 2) |
| `recommendation()` | Builds the sorted recommendations of one user |
| `main()` | Reads the command line arguments and writes the output file |

## 🚀 How to Run

Arguments, in order: movies file, ratings file, output file.

```bash
# Part 1
python main_p1.py movies.txt ratings.txt output.txt

# Part 2
python main_p2.py movies.txt ratings.txt output.txt
```

The input files are read from, and the output file is saved in, the same directory as the program.

## 📄 Example Output

```
Recommendations for alice:
1. Pulp Fiction (rated 5/5 by similar users: bob)
2. Forrest Gump (rated 4/5 by similar users: bob)

Recommendations for bob:
1. Fight Club (rated 5/5 by similar users: eve)
2. The Silence of the Lambs (rated 5/5 by similar users: eve)
3. The Godfather (rated 4/5 by similar users: alice)
4. The Matrix (rated 4/5 by similar users: eve)

Recommendations for eve:
1. Pulp Fiction (rated 5/5 by similar users: bob)
2. The Dark Knight (rated 5/5 by similar users: bob)
3. The Shawshank Redemption (rated 4/5 by similar users: bob)
```

## 🎯 Learning Goals

This project demonstrates:

- Lists and 2D lists (Part 1)
- Dictionaries and tuples (Part 2)
- File reading and writing
- Command line arguments
- Custom sorting with multiple criteria
- Writing docstrings and modular functions

## 📝 Notes
- This is a console-based project (no GUI)
- Thresholds are constants: similarity `0.7`, rating `4`
- A user with no recommendations gets only the header line

## 👨‍💻 Author
 [irem bekdemir](https://github.com/irembekdemir)
