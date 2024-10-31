# Author: Ashton Lee
# Github User: ashton01L
# Date: 10/30/2024
# Description: Write a class named NeighborhoodPets that has methods for adding a pet, deleting a pet, searching for the
# owner of a pet, saving data to a JSON file, loading data from a JSON file, and getting a set of all pet species.
import json

class DuplicateNameError(Exception):
    """Exception raised when a pet with the same name already exists."""
    pass

class NeighborhoodPets:
    """
    A class to represent NeighborhoodPets
    """
    def __init__(self):
        """
        Initializes a method for pets
        """
        self.__pets = {}

    def add_pet(self, name, species, owner):
        """
        Adds a pet

        :param name: adds a name
        :param species: adds a species
        :param owner: adds an owner
        :return: name, species, owner
        """
        if name in self.__pets:
            raise DuplicateNameError(f"A pet named '{name}' already exists.")
        self.__pets[name] = {
            "species": species,
            "owner": owner
        }

    def delete_pet(self, name):
        """
        Deletes a pet

        :param name:
        :return: deleting a pet
        """
        if name in self.__pets:
            del self.__pets[name]

    def get_owner(self, name):
        """
        Gets the owner of the pet

        :param name:
        :return: owner name
        """
        if name in self.__pets:
            return self.__pets[name]["owner"]
        return None

    def save_as_json(self, filename):
        """
        Saves as a JSON file

        :param filename: json.file
        :return: json file
        """
        with open(filename, 'w') as json_file:
            json.dump(self.__pets, json_file)

    def read_json(self, filename):
        """
        Reads from the JSON file

        :param filename: json.file
        :return: json file
        """
        with open(filename, 'r') as json_file:
            self.__pets = json.load(json_file)

    def get_all_species(self):
        """
        Gets all species of pets

        :return: pet species
        """
        return set(pet["species"] for pet in self.__pets.values())
