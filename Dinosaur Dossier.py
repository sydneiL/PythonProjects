#Dinosaur Dossier
#A database file full of information about the various theropod and sauropod dinosaur species that thrived from the Triassic to Cretaceous eras
#Built for CSC235@UAT
#Made by Sydnei Lang
#Data Generated from ChatGPT


import random
import pygame as pg

#Dino Discoveries
#Learn diverse species of bipedal theropod carnivores and quadrapedal sauropod herbivores!

import json

# Create the dinosaur database
dinosaur_database = {


#List of dinosaurs categorized by era and species


#Triassic Theropods & Sauropods, the blueprint of the newly born dinosaur species of the Mesozoic Era
    'Triassic': {
        'Theropods': [
            {'Species': 'Herrerasaurus', 'Family': 'Herrerasauridae', 'Length': '3 meters', 'Fossils': 12},
            {'Species': 'Eoraptor', 'Family': 'Eoraptoridae', 'Length': '1 meter', 'Fossils': 18}
        ],
        'Sauropods': [
            {'Species': 'Plateosaurus', 'Family': 'Plateosauridae', 'Length': '8 meters', 'Fossils': 24}
        ]
    },

#Jurassic Theropods & Sauropods, the second geological period of prehistory to flourish after the Triassic-Jurassic extinction
    'Jurassic': {
        'Theropods': [
            {'Species': 'Allosaurus', 'Family': 'Allosauridae', 'Length': '12 meters', 'Fossils': 32},
            {'Species': 'Dilophosaurus', 'Family': 'Dilophosauridae', 'Length': '6 meters', 'Fossils': 19}
        ],
        'Sauropods': [
            {'Species': 'Brachiosaurus', 'Family': 'Sauropodidae', 'Length': '23 meters', 'Fossils': 45},
            {'Species': 'Diplodocus', 'Family': 'Diplodocidae', 'Length': '27 meters', 'Fossils': 38}
        ]
    },
#Cretaceous Theropods & Sauropods, the third and longest gelogicsl period of prehistory featuring the most iconic dinosaurs known to modern paleontology
    'Cretaceous': {
        'Theropods': [
            {'Species': 'Tyrannosaurus Rex', 'Family': 'Tyrannosauridae', 'Length': '12 meters', 'Fossils': 62},
            {'Species': 'Spinosaurus', 'Family': 'Spinosauridae', 'Length': '16 meters', 'Fossils': 57}
        ],
        'Sauropods': [
            {'Species': 'Argentinosaurus', 'Family': 'Titanosauridae', 'Length': '30 meters', 'Fossils': 48},
            {'Species': 'Apatosaurus', 'Family': 'Diplodocidae', 'Length': '23 meters', 'Fossils': 41}
        ]
    }
}
#End of Dinosaur Dossier

# Write the dinosaur database to a file
def write_dinosaur_database_to_file(database, file_path):
    with open(file_path, 'w') as file:
        json.dump(database, file, indent=4)

# Read the dinosaur database from a file
def read_dinosaur_database_from_file(file_path):
    with open(file_path, 'r') as file:
        database = json.load(file)
    return database

#Find the species with the most excavated fossils!
def find_dinosaur_with_most_fossils(database):
    most_fossils_count = 0
    most_fossils_species = ''

    for era, groups in database.items():
        for group, species_list in groups.items():
            for species_data in species_list:
                fossils = species_data['Fossils']
                if fossils > most_fossils_count:
                    most_fossils_count = fossils
                    most_fossils_species = species_data['Species']

    return most_fossils_species, most_fossils_count

# Usage to write the database to file
write_dinosaur_database_to_file(dinosaur_database, 'dinosaur_data.json')

# Usage to read the database from file
read_dinosaur_data = read_dinosaur_database_from_file('dinosaur_data.json')

# Results of finding the species with the most excavated fossils!
most_fossils_species, most_fossils_count = find_dinosaur_with_most_fossils(read_dinosaur_data)
print(f"The species with the most excavated fossils is {most_fossils_species} with {most_fossils_count} fossils.")

