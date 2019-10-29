#this will extract the sequence of only listed contigs from the whole list of transcripts (e.g. Trinity result)
#noted that the result fasta file has to be converted into csv first
#transcript_list could be either csv or txt. doesnt matter as long as the name is matched with those in db list
#output does not have delimiters too, so txt or csv does not really matter. 
#noted that if your output name has no ">" its not fasta, txttofa.unix could be used.

import numpy as np
import csv
import matplotlib.pyplot as plt

with open("/path/to/transcript_list", 'r') as f1:
     with open("/path/to/database", 'r') as f2:
            with open("/path/to/output", 'w') as f3:
                reader1 = csv.reader(f1)
                reader2 = csv.reader(f2)
                writer = csv.writer(f3, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                header1 = next(reader1)
                header2 = next(reader2)
                line2 = next(reader2)
                for line1 in reader1:
                    while line1[0] != line2[0][0:len(line1[0])]:
                        line2 = next(reader2)   
                    writer.writerow(line2)
                    
