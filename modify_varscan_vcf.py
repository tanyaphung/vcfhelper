import argparse
import gzip

def parse_args():
    """
    Parse command-line arguments
    """
    parser = argparse.ArgumentParser(description="Modify varscan vcf to contain just the genotypes for tumor only")

    parser.add_argument(
        "--in_vcf", required=True,
        help="REQUIRED. Input the path to the input vcf file.")

    parser.add_argument(
        "--out_vcf", required=True,
        help="REQUIRED. Input the path to the output vcf file.")

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

    outfile = open(args.out_vcf, "w")

    open_func, mode = file_test(args.in_vcf)
    with open_func(args.in_vcf, mode) as f:
        for line in f:
            if line.startswith("#CHROM"):
                items = line.rstrip("\n").split("\t")
                print("\t".join(items.pop(9)), file=outfile)
            elif line.startswith("chr"):
                items = line.rstrip("\n").split("\t")
                print("\t".join(items.pop(9)), file=outfile)
            else:
                print(line.rstrip("\n"), file=outfile)

if __name__ == '__main__':
    main()