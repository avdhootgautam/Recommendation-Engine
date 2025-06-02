from utils import count_null_values,count_duplicate_values,preprocessing_on_a_column_genres
import json
class Preprocessing:
    def __init__(self,movie,credit):
        self.preprocess_debug=True
        self.movie=movie
        self.credit=credit

    def start_preprocessing(self):
        if self.preprocess_debug:
            print(f"Shape of movie before merging with credit::\n{self.movie.shape}")
            print(f'Shape of the credit before merging with credit::\n{self.credit.shape}')
        #merging of dataframe 
        self.movie=self.movie.merge(self.credit,on="title")
        if self.preprocess_debug:
            print(f"Shape of movie after merging with the credit::\n{self.movie.shape}")
            print(f"Value counts of the column ,original_language::\n{self.movie['original_language'].value_counts()}")
        #extracting the columns to work on 
        movie_column_to_inherit=['genres','movie_id','keywords','title','overview','cast','crew']
        self.movie=self.movie[movie_column_to_inherit]
        if self.preprocess_debug:
            print(f"This is the column in self.movie::{self.movie.columns}")
        #removing the null values from the column
        if self.preprocess_debug:
            print(f"This is the count of rows before dropping null values::\n{count_null_values(self.movie)}\n")
        self.movie.dropna(inplace=True)#All null values dropped
        if self.preprocess_debug:
            print(f"This is the count of rows after dropping null values::\n{count_null_values(self.movie)}\n")
        if self.preprocess_debug:
            print(f"This is the duplicate values in a movie dataframe::{count_duplicate_values(self.movie)}\n")
        #*Note*:- I have to make a dataframe consisting of the column ['movie_id','title','tags'] .
        #After data preprocessing on the columns except 'movie_id' and 'title',combine it and make a para which will be accumulated by tags

        if self.preprocess_debug:
            print(f"First value of the genres column will be ::{self.movie['genres'][1]} and the type of the genre is {type(self.movie['genres'][1])}")
        self.movie['genres']=self.movie['genres'].apply(preprocessing_on_a_column_genres)
        if self.preprocess_debug:
            print(f"First value after applying 'preprocessing_on_a_column_genres' genres column will be ::{self.movie['genres'][1]} and the type of the genre is {type(self.movie['genres'][1])}")