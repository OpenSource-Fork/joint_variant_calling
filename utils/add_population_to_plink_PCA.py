import sys, os, glob
import argparse

""" 
Utility script to create the list of section that the genome will be divided in for parallel processing
"""

def main(args):
    samples = {}
    #start by memorising all the samples and their label
    for population_file in args.populations:
        with open(population_file, "r") as POPULATION_FILE:
            for sample_entry in POPULATION_FILE:
                sample_name = sample_entry.split()[0]
                population  = sample_entry.split()[1]
                samples[sample_name] = population
    with open(args.pca, "r") as PCA_FILE:
        for pca_entry in PCA_FILE:
            pca_entry_split = pca_entry.split()
            sys.stdout.write('{} {} '.format(pca_entry_split[0], pca_entry_split[1]))
            if pca_entry_split[0] in samples:
                sys.stdout.write('{} '.format(samples[pca_entry_split[0]]))
            else:
                sys.stdout.write('UNKNOW ')
            for  i in xrange(2,12):
                 sys.stdout.write('{} '.format(pca_entry_split[i]))
            sys.stdout.write('\n')





if __name__ == '__main__':
    parser = argparse.ArgumentParser("""Utility script to add population filed to PCA result file generated by PLINK""")
    parser.add_argument('--populations', help="tab delimeted file, first column sample name, second column is a label", type=str, nargs='+', required=True)
    parser.add_argument('--pca', help="PLINK output", type=str, required=True)
    args = parser.parse_args()
    main(args)
