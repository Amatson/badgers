'''
This script opens two files, reference numbers and bank transactions,
and searches if there is a transaction with a given reference number.
'''

import sys

def main(argv):

    with open(argv[0], 'r') as numfile:
        refnums = [''.join(line.split()) for line in numfile]
    with open(argv[1], 'r') as bankfile:
        transactions = [line.strip().replace('\t', ' ') for line in bankfile]
    transactions = list(filter(None, transactions))     # removing empty list elements
    unfound = []

    for refnum in refnums:
        found = False
        for transaction in transactions:
            if transaction.find(refnum) > 0:
                print(transaction)
                found = True
        if not found:
            unfound.append(refnum)
    print('\nUnfound:')
    for element in unfound:
        print(element)


if __name__ == '__main__':
    main(sys.argv[1:])