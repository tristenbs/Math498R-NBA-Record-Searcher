import pandas as pd
import numpy as np
from searcher import Searcher
from data_processor import DataProcessor

################################################################
## Main file to run everything in
################################################################

def main():
    data = pd.read_csv('/home/tristen/MATH498R/Math498R-NBA-Record-Searcher/data/NBA Player Box Score Stats(1950 - 2022).csv')
    data_processor = DataProcessor(data)
    searcher = Searcher(data)
    # print(searcher.search_max_score(1963))
    print(searcher.get_most_stl_in1game_in_range('2000', '2022'))
    # print(searcher.get_most_fgm_in1game_in_range('2000', '2022'))
    print(searcher.get_num_times_ftm_achieved_in_range(10, '2000', '2022'))

if __name__ == "__main__":
    main()


