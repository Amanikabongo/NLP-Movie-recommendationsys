import spacy

# Load spaCy's medium-sized language model
nlp = spacy.load('en_core_web_md')


def read_movie_descriptions(file_path):
    """
    Reads movie descriptions from a specified file.

    Parameters:
    file_path (str): Path to the file containing movie descriptions.

    Returns:
    list: A list of movie descriptions.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            movie_descriptions = file.readlines()
        return [desc.strip() for desc in movie_descriptions]
    except FileNotFoundError:
        raise ValueError(f"File not found: {file_path}")
    except Exception as e:
        raise ValueError(f"An error occurred while reading the file: {e}")


def recommend_movie(description, movie_descriptions):
    """
    Recommends the most similar movie based on a given description.

    Parameters:
    description (str): Description of the movie to compare.
    movie_descriptions (list): List of movie descriptions to compare against.

    Returns:
    tuple: Index of the most similar movie and the similarity score.
    """
    if not isinstance(description, str) or not isinstance(movie_descriptions,
                                                          list):
        raise ValueError(
            "Invalid input types. 'description' should be a string and 'movie_descriptions' should be a list of strings.")

    # Convert the input description to a spaCy object
    input_desc = nlp(description)

    # Initialize variables to store the best match
    max_similarity = -1
    best_match = None

    # Iterate through the movie descriptions to find the most similar one
    for idx, movie_desc in enumerate(movie_descriptions):
        movie_desc_nlp = nlp(movie_desc)
        similarity = input_desc.similarity(movie_desc_nlp)

        if similarity > max_similarity:
            max_similarity = similarity
            best_match = idx

    if best_match is None:
        raise ValueError("No similar movie found.")

    return best_match, max_similarity


# Path to the movies.txt file
file_path = 'C:/Users/amans/Desktop/NLP-Movies/movies.txt'

try:
    # Read the movie descriptions from the file
    movie_descriptions = read_movie_descriptions(file_path)

    # Description of 'Planet Hulk'
    planet_hulk_desc = (
        "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, "
        "the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. "
        "Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
    )

    # Get the recommended movie
    recommended_movie_idx, similarity_score = recommend_movie(planet_hulk_desc,
                                                              movie_descriptions)

    print(f"Recommended movie : {recommended_movie_idx}")
    print(f"Similarity score: {similarity_score:.2f}")
    print(
        f"Recommended movie description: {movie_descriptions[recommended_movie_idx]}")

except ValueError as e:
    print(e)


