class Cleaner:
    def __init__(self,data_frame,tweets_column,biased_column):
        self.df = data_frame
        self.tweets_column = tweets_column
        self.biased_column = biased_column

    def drop_columns(self):
        self.df = self.df[[self.tweets_column,self.biased_column]]
        return self.df

    def clean_text(self):
        self.df[self.tweets_column] = self.df[self.tweets_column].str.replace(r'[^\w\s]', '', regex=True)
        return self.df

    def convert_to_lower(self):
        self.df[self.tweets_column] = self.df[self.tweets_column].str.lower()
        return self.df

    def remove_unclassified(self):
        self.df = self.df[self.df[self.biased_column].isin([1,0])]
        return self.df