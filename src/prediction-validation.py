import argparse

import numpy as np
import pandas as pd


def main(window_size, actual_price, predicted_price, output_error):
    #read in window size from input file
    window_size = with open(window_size_file, 'r')
                  as file: window_size = int(file.read())

    #read in actual and predicted price files as dataframes
    actual_df = pd.read_csv(actual_price, delimiter='|', header=None, index_col=['hour','ID'],
                            names=['hour','ID','price'], skip_blank_lines=True, float_precistion='high')
    predicted_df = pd.read_csv(predicted_price, delimiter='|', header=None, index_col=['hour','ID'],
                            names=['hour','ID','price'], skip_blank_lines=True, float_precistion='high')

    #join datasets and calculate rolling average error between model and actual prices
    combined_df = actual_df.join(predicted_df, how='left', lsuffix='_actual',rsuffix='_predicted')
    combined_df['abs_error'] =  np.abs(combined_df['price_actual'] - combined_df['price_predicted'])
    combined_df['rolling_error'] = combined_df['abs_error'].rolling(window_size, min_periods=1).avg()

    #create output data and save to to csv
    output_df = combined_df[['hour','avg_err']].set_index('hour')
    output_df['end_hour'] = output_df['hour'] + window_size -1
    output_df[['time', 'end_time', 'avg_error']].to_csv(output_file,delimiter='|',header=None,na_rep='NA',float_format='%.2f')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--window', '-w',
        metavar='WINDOW_SIZE', help='window size', required=True)
    parser.add_argument('--actual', '-a',
        metavar='ACTUAL_PRICE', help='actual price', required=True)
    parser.add_argument('--predicted', '-p',
        metavar='PREDICITED_PRICE_FILE', help='predicted price', required=True)
    parser.add_argument('--output', '-o',
        metavar='OUTPUT_FILE', help='comparison avg error output', default='.')
    args = parser.parse_args()
    main(args.window, args.predicted, args.actual, args.output)
