import argparse

parser = argparse.ArgumentParser(description="Convert vcf to bed file format.")
parser.add_argument("--input_vcf",required=True,help="Input the path to the vcf file")
parser.add_argument("--output_bed",required=True,help="Input the path to the output file")

args = parser.parse_args()

outfile = open(args.output_bed, "w")

with open(args.input_vcf, "r") as f:
    for line in f:
        if not line.startswith("#"):
            items = line.rstrip("\n").split("\t")
            out = [items[0], str(int(items[1])-1), items[1]]
            print("\t".join(out), file=outfile)