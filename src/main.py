import data_investigation
import data_loader
from src.data_investigation import Explore
from src.data_loader import DataLoader

dl = DataLoader("../data/tweets_dataset.csv")
dl = dl.convert_to_data_frame()
df = Explore(dl,'Text','Biased')
result = {}
result["total_tweets"] = df.number_of_tweets()
result["average_length"] = df.length_of_tweets()
result["longest_3_tweets"] = df.three_longest_tweets()
result["common_words"] = df.ten_most_common_words()
result["uppercase_words"] = df.number_of_capital_letters()
print(result)