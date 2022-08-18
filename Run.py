#***** Example script to run EXCALIBUR *****#


'''Download main isotopologue of NO from ExoMol'''

from excalibur.core import summon

species = 'NO'
database = 'ExoMol'

summon(database=database, species = species)  # Download line list

from excalibur.core import compute_cross_section

'''Compute cross section for both isotopologues'''

P = 1  # Pressure in bars
T = 1000  # Temperature in Kelvin
input_directory = './input/' # Top level directory containing line lists


nu, sigma = compute_cross_section(species = species, database = database, temperature = T, input_dir = input_directory,
                      pressure = P)












'''
species = 'H2O'
database = 'HITEMP'

# Download line list
summon(database=database, species = species)


diff_isotopologue = '15N-16O'
linelist = 'NOname'

summon(database=database, species = species, isotope = diff_isotopologue, linelist = linelist)

P = 1  # Pressure in bars
T = 1000  # Temperature in Kelvin
input_directory = './input/' # Top level directory containing line lists


nu, sigma = compute_cross_section(species = species, database = database, temperature = T, input_dir = input_directory,
                      pressure = P)

nu2, sigma2 = compute_cross_section(species = species, database = database, temperature = T, input_dir = input_directory,
                      pressure = P)

cross_sections = cross_section_collection(nu, sigma)
cross_sections = cross_section_collection(nu2, sigma2, cross_sections)

plot_cross_section(collection = cross_sections, labels = ['14N-16O', '15N-16O'], filename = 'Different_Isotopologues')
'''
