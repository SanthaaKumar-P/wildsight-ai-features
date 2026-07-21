taxonomy_database = {

    "tiger": {
        "scientificName": "Panthera tigris",
        "kingdom": "Animalia",
        "phylum": "Chordata",
        "class": "Mammalia",
        "order": "Carnivora",
        "family": "Felidae",
        "genus": "Panthera"
    },

    "lion": {
        "scientificName": "Panthera leo",
        "kingdom": "Animalia",
        "phylum": "Chordata",
        "class": "Mammalia",
        "order": "Carnivora",
        "family": "Felidae",
        "genus": "Panthera"
    },

    "leopard": {
        "scientificName": "Panthera pardus",
        "kingdom": "Animalia",
        "phylum": "Chordata",
        "class": "Mammalia",
        "order": "Carnivora",
        "family": "Felidae",
        "genus": "Panthera"
    },

    "cheetah": {
        "scientificName": "Acinonyx jubatus",
        "kingdom": "Animalia",
        "phylum": "Chordata",
        "class": "Mammalia",
        "order": "Carnivora",
        "family": "Felidae",
        "genus": "Acinonyx"
    },

    "wolf": {
        "scientificName": "Canis lupus",
        "kingdom": "Animalia",
        "phylum": "Chordata",
        "class": "Mammalia",
        "order": "Carnivora",
        "family": "Canidae",
        "genus": "Canis"
    },

    "fox": {
        "scientificName": "Vulpes vulpes",
        "kingdom": "Animalia",
        "phylum": "Chordata",
        "class": "Mammalia",
        "order": "Carnivora",
        "family": "Canidae",
        "genus": "Vulpes"
    },

    "elephant": {
        "scientificName": "Elephas maximus",
        "kingdom": "Animalia",
        "phylum": "Chordata",
        "class": "Mammalia",
        "order": "Proboscidea",
        "family": "Elephantidae",
        "genus": "Elephas"
    },

    "rhino": {
        "scientificName": "Rhinoceros unicornis",
        "kingdom": "Animalia",
        "phylum": "Chordata",
        "class": "Mammalia",
        "order": "Perissodactyla",
        "family": "Rhinocerotidae",
        "genus": "Rhinoceros"
    },

    "hippopotamus": {
        "scientificName": "Hippopotamus amphibius",
        "kingdom": "Animalia",
        "phylum": "Chordata",
        "class": "Mammalia",
        "order": "Artiodactyla",
        "family": "Hippopotamidae",
        "genus": "Hippopotamus"
    },

    "zebra": {
        "scientificName": "Equus quagga",
        "kingdom": "Animalia",
        "phylum": "Chordata",
        "class": "Mammalia",
        "order": "Perissodactyla",
        "family": "Equidae",
        "genus": "Equus"
    },

    "giraffe": {
        "scientificName": "Giraffa camelopardalis",
        "kingdom": "Animalia",
        "phylum": "Chordata",
        "class": "Mammalia",
        "order": "Artiodactyla",
        "family": "Giraffidae",
        "genus": "Giraffa"
    },

    "deer": {
        "scientificName": "Cervus elaphus",
        "kingdom": "Animalia",
        "phylum": "Chordata",
        "class": "Mammalia",
        "order": "Artiodactyla",
        "family": "Cervidae",
        "genus": "Cervus"
    },

    "bear": {
        "scientificName": "Ursus arctos",
        "kingdom": "Animalia",
        "phylum": "Chordata",
        "class": "Mammalia",
        "order": "Carnivora",
        "family": "Ursidae",
        "genus": "Ursus"
    },

    "monkey": {
        "scientificName": "Macaca mulatta",
        "kingdom": "Animalia",
        "phylum": "Chordata",
        "class": "Mammalia",
        "order": "Primates",
        "family": "Cercopithecidae",
        "genus": "Macaca"
    },

    "chimpanzee": {
        "scientificName": "Pan troglodytes",
        "kingdom": "Animalia",
        "phylum": "Chordata",
        "class": "Mammalia",
        "order": "Primates",
        "family": "Hominidae",
        "genus": "Pan"
    },

    "gorilla": {
        "scientificName": "Gorilla gorilla",
        "kingdom": "Animalia",
        "phylum": "Chordata",
        "class": "Mammalia",
        "order": "Primates",
        "family": "Hominidae",
        "genus": "Gorilla"
    },

    "kangaroo": {
        "scientificName": "Macropus giganteus",
        "kingdom": "Animalia",
        "phylum": "Chordata",
        "class": "Mammalia",
        "order": "Diprotodontia",
        "family": "Macropodidae",
        "genus": "Macropus"
    },

    "camel": {
        "scientificName": "Camelus dromedarius",
        "kingdom": "Animalia",
        "phylum": "Chordata",
        "class": "Mammalia",
        "order": "Artiodactyla",
        "family": "Camelidae",
        "genus": "Camelus"
    },

    "buffalo": {
        "scientificName": "Bubalus bubalis",
        "kingdom": "Animalia",
        "phylum": "Chordata",
        "class": "Mammalia",
        "order": "Artiodactyla",
        "family": "Bovidae",
        "genus": "Bubalus"
    },

    "cow": {
        "scientificName": "Bos taurus",
        "kingdom": "Animalia",
        "phylum": "Chordata",
        "class": "Mammalia",
        "order": "Artiodactyla",
        "family": "Bovidae",
        "genus": "Bos"
    }
}


def get_taxonomy(species):

    return taxonomy_database.get(
        species.lower(),
        {
            "scientificName": "Unknown",
            "kingdom": "Animalia",
            "phylum": "Chordata",
            "class": "Unknown",
            "order": "Unknown",
            "family": "Unknown",
            "genus": "Unknown"
        }
    )