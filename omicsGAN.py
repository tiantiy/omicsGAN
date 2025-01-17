import os
import sys
import pandas as pd 
import numpy as np 
import argparse
from omics1 import omics1
from omics2 import omics2

total_update = int(sys.argv[1])
omics1_name = sys.argv[2]
omics2_name = sys.argv[3]
adj_file = sys.argv[4]

omics1_result = []
omics2_result = []
for i in range(1, total_update+1):
	omics1_result.append(omics1(i,omics1_name,omics2_name,adj_file))
	omics2_result.append(omics2(i,omics1_name,omics2_name,adj_file))

omics1_result = np.array(omics1_result)
omics2_result = np.array(omics2_result)

keep_mRNA = (np.argsort(np.mean(omics1_result,axis=1))[::-1][0])+1
keep_miRNA = (np.argsort(np.mean(omics2_result,axis=1))[::-1][0])+1

print('Best prediction for omics1: ',omics1_result[keep_mRNA])
print('Best update for omics1: ',keep_mRNA)
print('Best prediction for omics2: ',omics2_result[keep_miRNA])
print('Best update for omics2: ',keep_miRNA)

for i in range(1, total_update+1):
	if i!=keep_mRNA:
		os.remove("omics1_"+str(i)+".csv") 

	if i!=keep_miRNA:
		os.remove("omics2_"+str(i)+".csv")


