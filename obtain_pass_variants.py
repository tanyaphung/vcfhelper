import argparse
import gzip

def parse_args():
    parser = argparse.ArgumentParser(description="Obtain PASS variants from VCF file.")
    parser.add_argument("--input_vcf",required=True,help="Input the path to the vcf file")
    parser.add_argument("--output_vcf",required=True,help="Input the path to the output vcf file")

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
    outfile = open(args.output_vcf, "wt")
    open_func, mode = file_test(vcf_file=args.input_vcf)

    with open_func(args.input_vcf, mode) as f:
        for line in f:
            if line.startswith("#"):
                print(line.rstrip("\n"), file=outfile)
            if not line.startswith("#"):
                items = line.rstrip("\n").split("\t")
                if items[6] == "PASS":
                    print(line.rstrip("\n"), file=outfile)

if __name__ == '__main__':
    main()