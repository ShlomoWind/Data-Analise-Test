from src.data_cleaner import Cleaner
from src.data_investigation import Explore
from src.data_loader import DataLoader
from src.data_exporter import ExporterCsv,ExporterJson

file_path = "../results"  #Setting the path of the files to save
dl = DataLoader("../data/tweets_dataset.csv")  #Creating an instance of the data loader
df = dl.convert_to_data_frame()  #Creating the data frame

#Data exploration and activation of all exploration functionality
explore = Explore(df,'Text','Biased')
result = {}
result["total_tweets"] = explore.number_of_tweets()
result["average_length"] = explore.length_of_tweets()
result["longest_3_tweets"] = explore.three_longest_tweets()
result["common_words"] = explore.ten_most_common_words()
result["uppercase_words"] = explore.number_of_capital_letters()

#Data exploration and activation of all exploration functionality
export_result = ExporterJson(result,f"{file_path}/results.json")
export_result.export_to_json()

#Clearing the data and enabling all cleaning functionality
cleaner = Cleaner(df,'Text','Biased')
cleaned_df = cleaner.drop_columns().clean_text().convert_to_lower().remove_unclassified().get_clean_df()

#Export the clean data to a csv file
export_cleaned_data = ExporterCsv(cleaned_df,f"{file_path}/tweets_dataset_cleaned.csv")
export_cleaned_data.export_to_csv()
