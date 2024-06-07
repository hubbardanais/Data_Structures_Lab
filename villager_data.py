"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    file = open(filename)

    species_set = set()

    for line in file:
        line = line.rstrip()
        species = line.split('|')[1]

        species_set.add(species)


    # TODO: replace this with your code

    return species_set

# result = all_species("villagers.csv")
# print(result)



def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []

    file = open(filename)
    
    for line in file:
        line = line.rstrip()
        name = line.split("|")[0]
        species = line.split("|")[1]
        
        if search_string == "All":
            villagers.append(name)
        else:
            if search_string == species:
                villagers.append(name)
        
    return sorted(villagers)

# result = get_villagers_by_species("villagers.csv", "bear")
# print(result)

def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []

    file = open(filename)
        
    for line in file:
        line = line.rstrip()
        name = line.split("|")[0]
        hobby = line.split("|")[3]

        if hobby == "Fitness":
            fitness.append(name)
            
        if hobby == "Nature":
            nature.append(name)

        if hobby == "Education":
            education.append(name)

        if hobby == "Music":
            music.append(name)

        if hobby == "Fashion":
            fashion.append(name)

        if hobby == "Play":
            play.append(name)
    
    return [(sorted(fitness)),(sorted(nature)), (sorted(education)), (sorted(music)), (sorted(fashion)), (sorted(play))]

# result = all_names_by_hobby("villagers.csv")
# print(result)

def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    file = open(filename)
    
    for line in file:
        line = line.rstrip()
        name = line.split("|")[0]
        species = line.split("|")[1]
        personality = line.split("|")[2]
        hobby = line.split("|")[3]
        motto = line.split("|")[4]

        villager_data = (name, species, personality, hobby, motto)
        all_data.append(villager_data)

    return all_data

result = all_data("villagers.csv")
print(result)

def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
