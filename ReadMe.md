# Movie Recommendation System (NLP-MOVIES)

This project builds a movie recommendation system based on word vector similarity using spaCy. It recommends which movie a user might watch next based on the description of a given movie.

## Requirements

- Python 3.6 or higher
- spaCy
- spaCy language model (`en_core_web_md`)

## Installation

1. **Clone the Repository**: (Assuming you have the project files)
2. **Navigate to the Project Directory**:
   ```sh
    cd path/to/project-directory
   ```
## Install spaCy and the Required Language Model:
   ```sh
    pip install spacy
    python -m spacy download en_core_web_md
   ```
## Project Structure
**. movies.txt: A text file containing descriptions of different movies, with each line representing a separate movie description.**

**. movies.py: The main script containing functions to read movie descriptions and recommend a movie based on the similarity of descriptions.**
## Usage
**. Ensure movies.txt file is in the project directory.**

**. Each line in movies.txt file  should be a description of a different movie.**

**. Execute movies.py to find the most similar movie to a given description.**
