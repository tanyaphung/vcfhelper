import argparse

def parse_args():
	"""
	Parse command-line arguments
	"""
	parser = argparse.ArgumentParser(description="This script extracts statistics from vcf file.")

	parser.add_argument(
		"statistics", metavar="S", type=str, nargs="+",
		help = "Statistics from the vcf file to be extracted."
	)

	parser.add_argument(
            "--vcf", required=True,
            help="REQUIRED. Path to the vcf file.")

	parser.add_argument(
            "--outfile", required=True,
            help="REQUIRED. Path to the output file.")

	args = parser.parse_args()
	return args

def parse_between(line, start, end):
	try:
		s_idx = line.find(start)+len(start)
		e_idx = line.find(end, s_idx)
		if s_idx == len(start)-1:
			return b'NA'
		return line[s_idx:e_idx]
	except:
		return b'NA'


def stats_from_row(line, stats):
	if line.startswith(b'##'):
		return
	stat_block = line.split(b"\t")[7]
	return [parse_between(line=stat_block, start=s+b'=', end=b';') for s in stats]


def extract_stats (stats, vcf, out):
	with open(vcf, "rb") as vcf:
		stats = list(map(lambda l: stats_from_row(line=l, stats=stats), vcf))
		out.write(b'\n'.join([b'\t'.join(s)for s in stats if s]))

def main():
	args = parse_args()
	out = open(args.outfile, "wb")
	stats = [x.encode() for x in args.statistics]
	out.write(b'\t'.join(stats)+b'\n')
	extract_stats(stats=stats, vcf=args.vcf, out=out)

if __name__ == '__main__':
	main()