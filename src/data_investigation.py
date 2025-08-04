import pandas as pd

class Explore:
    def __init__(self, data_frame,tweets_column,biased_column):
        self.df = data_frame
        self.tweets_column = tweets_column
        self.biased_column = biased_column
        self.antisemitic = self.df[self.df['Biased'] == 1].copy()
        self.non_antisemitic = self.df[self.df['Biased'] == 0].copy()

#tweets counter by category and total
    def number_of_tweets(self):
        count = self.df[self.biased_column].value_counts()
        return {"antisemitic":int(count.get(1,0)),
                "non_antisemitic":int(count.get(0,0)),
                "total":len(self.df),
                "unspecified":len(self.df) - int(count.get(1,0)) - int(count.get(0,0))}

#the mean length of tweets by each category and total
    def length_of_tweets(self):
        total_avg = self.df[self.tweets_column].apply(lambda x: len(str(x))).mean()
        anti_avg = self.antisemitic[self.tweets_column].apply(lambda x: len(str(x))).mean()
        non_anti_avg = self.non_antisemitic[self.tweets_column].apply(lambda x: len(str(x))).mean()
        return {"antisemitic": float(anti_avg),
                "non_antisemitic": float(non_anti_avg),
                "total":float(total_avg)}

#the three longest tweets by each category
    def three_longest_tweets(self):
        pass

#the ten most common words in all tweets
    def ten_most_common_words(self):
        pass

#how many words in capital letters by each category and total
    def number_of_capital_letters(self):
        pass