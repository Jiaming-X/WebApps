import webbrowser
import os
import re
import csv

def load_templates(path):
    with open(path, 'r') as content_file:
        return content_file.read()

def get_movies(filename):
    movies = []
    with open(filename, 'rU') as csvfile:
        reader = csv.DictReader(csvfile)
        for movie in reader:
            movies.append(
                Movie(title=movie['name'],
                      image_url=movie['image_url'],
                      youtube_url=movie['youtube_url'],
                      year=movie['year']))
    return movies

class Movie(object):
    # Movie class for basic information of the movies
    def __init__(self, title, image_url, youtube_url, year):
        self.title = title
        self.poster_image_url = image_url
        self.trailer_youtube_url = youtube_url
        self.year = year

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            year=movie.year
        )
    return content

def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)

# Styles and scripting for the page
main_page_head = load_templates('templates/head.html')

# The main page layout and title bar
main_page_content = load_templates('templates/content.html')

# A single movie entry html template
movie_tile_content = load_templates('templates/movie.html')

def main():
    #main function to start the whole process
    movies = get_movies('data/fresh_tomatoes.csv')
    open_movies_page(movies)

if __name__ == '__main__':
    main()



        
