import argparse
import gzip


def parse_args():
    """
    Parse command-line arguments
    """
    parser = argparse.ArgumentParser(description="Calculate the number of sites in a vcf file")

    parser.add_argument(
        "--vcf", required=True,
        help="REQUIRED. Input the path to the vcf file.")

    parser.add_argument(
        "--id", required=True,
        help="REQUIRED. Input the id of the file")

    args = parser.parse_args()
    return args


def file_test(vcf_file):
    """
    This function checks if the input VCF file is gzip or not.
    """
    if vcf_file.endswith('.gz'):
        return gzip.open, 'rb'
    else:
        return open, 'rb'


def main():
    args = parse_args()

    open_func, mode = file_test(args.vcf)
    with open_func(args.vcf, mode) as f:
        out = [args.id, str(sum([1 for line in f if not line.startswith(b'#')]))]
        print (','.join(out))


main()
