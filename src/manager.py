import data_investigation
import data_loader
from src.data_investigation import Explore
from src.data_loader import DataLoader

dl = DataLoader("../data/tweets_dataset.csv")
dl = dl.convert_to_data_frame()
print(dl.head())
df = Explore(dl,'Text','Biased')
print(df.number_of_tweets())
print(df.length_of_tweets())
