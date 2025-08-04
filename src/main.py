from src.data_cleaner import Cleaner
from src.data_investigation import Explore
from src.data_loader import DataLoader
from src.data_exporter import ExporterCsv,ExporterJson

dl = DataLoader("../data/tweets_dataset.csv")
df = dl.convert_to_data_frame()

explore = Explore(df,'Text','Biased')
result = {}
result["total_tweets"] = explore.number_of_tweets()
result["average_length"] = explore.length_of_tweets()
result["longest_3_tweets"] = explore.three_longest_tweets()
result["common_words"] = explore.ten_most_common_words()
result["uppercase_words"] = explore.number_of_capital_letters()

export_result = ExporterJson(result,"../results/results.json")
export_result.export_to_json()

cleaner = Cleaner(df,'Text','Biased')
cleaned_df = cleaner.drop_columns().clean_text().convert_to_lower().remove_unclassified().get_clean_df()

export_cleaned_data = ExporterCsv(cleaned_df,"../results/tweets_dataset_cleaned.csv")
export_cleaned_data.export_to_csv()
