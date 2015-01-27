#! /usr/bin/python

my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
length = len(my_dna)
a_count = my_dna.count('A')
t_count = my_dna.count('T')

at_content = (1.0 * a_count + t_count) / length
print("AT content is " + str(at_content))
