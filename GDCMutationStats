%matplotlib inline
# This module extracts inforation about mutations for a specific cohort

# Import libraries
import requests
import json
import collections
import matplotlib.pyplot as plt
from collections import Counter

def FetchData(Endpoint, Filters, Fields, Size):
    API_URL = 'https://gdc-api.nci.nih.gov/'
    Request = API_URL + Endpoint + '?' + 'filters=' + Filters + '&' + 'fields=' + Fields + '&' + 'size=' + Size
    r = requests.get(Request)
    data = json.loads(r.text)
    return data['data']['hits']

def ExtractTransversions(DNA_Changes):
    transversions=[]
    for dna_change in DNA_Changes:
        loc = dna_change['genomic_dna_change'].find('>') - 1
        if loc > 0:
            transversions.append(dna_change['genomic_dna_change'][loc:])
    return transversions

def ExtractInsertions(DNA_Changes):
    insertions=[]
    for dna_change in DNA_Changes:
        loc = dna_change['genomic_dna_change'].find('ins')
        if loc > 0:
            insertions.append('ins')
    return insertions

def ExtractDeletions(DNA_Changes):
    deletions=[]
    for dna_change in DNA_Changes:
        loc = dna_change['genomic_dna_change'].find('del')
        if loc > 0:
            deletions.append('del')
    return deletions

def ExtractChrPos(DNA_Changes):
    chrpos=[]
    for dna_change in DNA_Changes:
        loc = dna_change['genomic_dna_change'].find(':')
        if loc > 0:
            chrpos.append(dna_change['genomic_dna_change'][0:loc])
    return chrpos

def PlotData(Data):
    Counted_Data = Counter(Data)
    Sorted_Data = collections.OrderedDict(sorted(Counted_Data.items()))
    l = range(len(Sorted_Data))
    plt.bar(l, Sorted_Data.values(), align='center')
    plt.xticks(l, Sorted_Data.keys())
    plt.xticks(rotation=40)
