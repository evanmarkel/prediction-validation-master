import argparse

import numpy as np
import pandas as pd


def main(window_size, actual_price, predicted_price, error_output):
    return 0

if __name__ == '__main__':
    args = build_argparser().parse_args()
    compile_files(
        args.file_or_directory,
        output_type=args.output_type,
    )
