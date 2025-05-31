class Preprocessing:
    def __init__(self,movie,credit):
        self.preprocess_debug=True
        self.movie=movie
        self.credit=credit
    def info_dataset(self):
        pass
    def start_preprocessing(self):
        self.movie=self.movie.merge(credits,on="title")