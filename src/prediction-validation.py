import argparse

import numpy as np
import pandas as pd


def main(window_size, actual_price, predicted_price, output_error):
    #read in window size from input file
    window_size = with open(window_size_file, 'r')
                  as file: window_size = int(file.read())

    #read in actual and predicted price files as dataframes
    actual_df = pd.read_csv(actual_price, delimiter='|', header=None,
                            names=['hour','ID','price'], skip_blank_lines=True, float_precistion='high')
    predicted_df = pd.read_csv(predicted_price, delimiter='|', header=None,
                            names=['hour','ID','price'], skip_blank_lines=True, float_precistion='high')

    #calculate rolling average error between model and actual prices
    

if __name__ == '__main__':
    args = build_argparser().parse_args()
    compile_files(
        args.file_or_directory,
        output_type=args.output_type,
    )
