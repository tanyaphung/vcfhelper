import argparse
import gzip

def parse_args():
	"""
	Parse command-line arguments
	"""
	parser = argparse.ArgumentParser(description="Calculate the number of individuals in a vcf file")

	parser.add_argument(
            "--vcf", required=True,
            help="REQUIRED. Input the path to the vcf file.")

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
		for line in f:
			if line.startswith(b'#CHROM'):
				print (len(line.split(b'\t')[9:]))
				break
main()