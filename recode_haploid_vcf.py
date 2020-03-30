import argparse
import gzip

parser = argparse.ArgumentParser(description='Recode haploid vcf file.')
parser.add_argument('--input_vcf',required=True,help='Input the path to the vcf file.')
parser.add_argument('--output_vcf_recode',required=True,help='Input the path to the recoded vcf file.')

args = parser.parse_args()

outfile = open(args.output_vcf_recode, 'w')

with gzip.open(args.input_vcf, 'rt') as f:
    for line in f:
        if line.startswith('#'):
            print (line.rstrip('\n'), file=outfile)
        else:
            items = line.rstrip('\n').split('\t')
            new_line = items[:9]
            for i in items[9:]:
                if i[0] == '1':
                    new_line.append('1/1' + i[1:])
                elif i[0] == '0':
                    new_line.append('0/0' + i[1:])
                elif i[0] == '.':
                    new_line.append('./.' + i[1:])
            print ('\t'.join(new_line), file=outfile)


