import gzip
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Compare the number of variants between two vcfs.")
    parser.add_argument("--vcf1",required=True,help="Input the path to the first VCF file.")
    parser.add_argument("--vcf2",required=True,help="Input the path to the second VCF file.")

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
    vcf1_variants_set = set()
    vcf1_open_func, vcf1_mode = file_test(vcf_file=args.input_vcf1)
    with vcf1_open_func(args.input_vcf1, vcf1_mode) as f:
        for line in f:
            if not line.startswith('#'):
                items = line.rstrip('\n').split('\t')
                vcf1_variants_set.add(items[1])

    vcf2_variants_set = set()
    vcf2_open_func, vcf2_mode = file_test(vcf_file=args.input_vcf2)
    with vcf2_open_func(args.input_vcf2, vcf2_mode) as f:
        for line in f:
            if not line.startswith('#'):
                items = line.rstrip('\n').split('\t')
                vcf2_variants_set.add(items[1])

    out = [str(len(vcf1_variants_set.intersection(vcf2_variants_set))), str(len(vcf1_variants_set-vcf2_variants_set)), str(len(vcf2_variants_set-vcf1_variants_set))]
    print('\t'.join(out))

if __name__ == '__main__':
    main()
