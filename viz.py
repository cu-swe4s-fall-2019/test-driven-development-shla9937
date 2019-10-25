import sys
import argparse
import get_data
import data_viz


parser = argparse.ArgumentParser(
           description='Parsing operator.')

parser.add_argument('--plot_type',
                    type=str,
                    help='Type of plot',
                    required=True)

parser.add_argument('--output_file',
                    type=str,
                    help='Output file name',
                    required=True)

args = parser.parse_args()


def main():
    L = sys.stdin
    out_file = args.output_file
    plot = args.plot_type
    if plot == 'boxplot':
        data_viz.boxplot(L, out_file)
    if plot == 'histogram':
        data_viz.histogram(L, out_file)
    if plot == 'combo':
        data_viz.combo(L, out_file)


if __name__ == '__main__':
    main()
