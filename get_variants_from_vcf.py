import gzip
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Obtain variants in the chr_position format from vcf or vcf-like file")
    parser.add_argument("--vcf",required=True,help="Input the path to the VCF file.")
    parser.add_argument("--outfile",required=True,help="Input the path to the output file.")

    args = parser.parse_args()
    return args

def file_test(vcf_file):
    """
    This function checks if the input VCF file is gzip or not.
    """
    if vcf_file.endswith(".gz"):
        return gzip.open, "rt"
    else:
        return open, "rt"


def main():
    args = parse_args()
    vcf_open_func, vcf_mode = file_test(vcf_file=args.vcf)
    outfile = open(args.outfile, "w")
    with vcf_open_func(args.vcf, vcf_mode) as f:
        for line in f:
            if not line.startswith('#'):
                items = line.rstrip('\n').split('\t')
                variants = items[0] + "_" + items[1]
                print(variants, file=outfile)

if __name__ == '__main__':
    main()
