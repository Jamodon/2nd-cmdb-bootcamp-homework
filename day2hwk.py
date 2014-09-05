#!/usr/bin/env python

# Day 2 Homework

# 1. Make boxplot
import pandas as pd
import matplotlib.pyplot as plt

cufflinks_output = "/Users/cmdb/data/results/SRR072893_clout/genes.fpkm_tracking"
df = pd.read_table(cufflinks_output)

cufflinks_output2 = "/Users/cmdb/data/results/SRR072915_clout/genes.fpkm_tracking"
df2 = pd.read_table(cufflinks_output2)



#print df.describe()

#values for FPKM on df
# 1/3: ~0.0
# 2/3 ~1.0

# FPKM df variables
bottom_third1 = df[df["FPKM"] == 0]
middle_third1 = df[df[df["FPKM"] < 1] > 0]
top_third1    = df[df["FPKM"] >= 1]

#print df2.describe()
bottom_third2 = df2[df2["FPKM"] == 0]
middle_third2 = df2[df2[df2[["FPKM"] < 2] > 0 ]
#middle_third2 = middle_third2["FPKM"] > 0
top_third2    = df[df2["FPKM"] >= 2]


# bottom_2_3 = df2[ df["FPKM"] < 1]
# middle_1_3 = ten_thousand[ ten_thousand["FPKM"] > 0]

#female = [bottom_third2, middle_third2, top_third2]
male_female = pd.DataFrame({"male bottom": bottom_third1, "male middle": middle_third1, "male top": top_third1, "female bottom": bottom_third2, "female middle": middle_third2, "female top": top_third2})

plt.boxplot(male_female)
plt.show()
plt.savefig ("boxplot.png")


#2. 
for file in genelist:
cufflinks_output_893 = "/Users/cmdb/data/results/SRR072893_clout/genes.fpkm_tracking"
df1 = pd.read_table(cufflinks_output_893)

cufflinks_output_894 = "/Users/cmdb/data/results/SRR072894_clout/genes.fpkm_tracking"
df2 = pd.read_table(cufflinks_output_894)

cufflinks_output_895 = "/Users/cmdb/data/results/SRR072895_clout/genes.fpkm_tracking"
df3 = pd.read_table(cufflinks_output_895)

cufflinks_output_896 = "/Users/cmdb/data/results/SRR072893_clout/genes.fpkm_tracking"
df4 = pd.read_table(cufflinks_output_896)

cufflinks_output_897 = "/Users/cmdb/data/results/SRR072897_clout/genes.fpkm_tracking"
df5 = pd.read_table(cufflinks_output_897)

cufflinks_output_898 = "/Users/cmdb/data/results/SRR072898_clout/genes.fpkm_tracking"
df6 = pd.read_table(cufflinks_output_898)

cufflinks_output_899 = "/Users/cmdb/data/results/SRR072899_clout/genes.fpkm_tracking"
df7 = pd.read_table(cufflinks_output_899)

cufflinks_output_900 = "/Users/cmdb/data/results/SRR072900_clout/genes.fpkm_tracking"
df8 = pd.read_table(cufflinks_output_900)

cufflinks_output_901 = "/Users/cmdb/data/results/SRR072901_clout/genes.fpkm_tracking"
df9 = pd.read_table(cufflinks_output_901)

cufflinks_output_902 = "/Users/cmdb/data/results/SRR072902_clout/genes.fpkm_tracking"
df10 = pd.read_table(cufflinks_output_902)

cufflinks_output_903 = "/Users/cmdb/data/results/SRR072903_clout/genes.fpkm_tracking"
df11 = pd.read_table(cufflinks_output_903)

cufflinks_output_904 = "/Users/cmdb/data/results/SRR072904_clout/genes.fpkm_tracking"
df12 = pd.read_table(cufflinks_output_904)

columns_of_interest = ["FPKM", "gene_short_name"]
df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12.to_samples.csv("sxk.csv", sep="\t", index=false)


#3
for i (905:915):
    cufflinks_output + str(i) = filename
    cufflinks_output + str(i) = "/Users/cmdb/data/results/SRR072" + str(i) + "_clout/genes.fpkm_tracking"
    #append to list
    filename.append(all_files)
#all_files = [cufflinks_output + str(i), ...]

FPKM_level = []
for file in all_files
    f = open(i)
    while True:
        line = f.readline()
        if "Sxl" in line:
            fields = line.rstrip("\r\n").split("\t")
            FPKM_level.appends(fields[9])
            break

plt.figure()
plt.plot(FPKM_level)
plt.savefig("FPKM_levels")


