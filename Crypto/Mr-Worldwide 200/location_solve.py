from geopy.geocoders import Nominatim
import itertools

coordinates = ["35.028309, 135.753082", "46.469391, 30.740883",
                "39.758949, -84.191605", "41.015137, 28.979530",
                "24.466667, 54.366669", "3.140853, 101.693207",
                "9.005401, 38.763611", "-3.989038, -79.203560",
                "52.377956, 4.897070", "41.085651, -73.858467",
                "57.790001, -152.407227", "31.205753, 29.924526"]
                
en_dict = set(line.strip().upper() for line in open('words_alpha.txt'))

geolocator = Nominatim(user_agent="location_solve")

# Each coordinate group will have a series of comma separated values for the location
# Ex. Seven-Eleven, Motoseiganji-dori, 東町, Kamigyo Ward, Kyoto, Kyoto Prefecture, 602-0953, Japan
# We want to get the first letter of each word in the address
word_lists = []
for c in coordinates:
    location = geolocator.reverse(c, language='en')
    word_list = location.address.split(",")
    word_list = [word.strip()[0] for word in word_list]
    word_lists.append(word_list)

# Since there is an underscore after the 6th character, break it up so we'll have two words
word_one_list = word_lists[0:6]
word_two_list = word_lists[6:]

def get_possibilities(word_list):
    """ 
    Finds all combinations of strings in multiple lists and returns the combinations if
    they are words found in the english dictionary
    """
    word_possibilities = list(itertools.product(*word_list))
    word_possibilities = [''.join(combo) for combo in word_possibilities]
    word_possibilities = set([p for p in word_possibilities if p in en_dict])
    return word_possibilities

word_one_possibilities = get_possibilities(word_one_list)
word_two_possibilities = get_possibilities(word_two_list)   

print(word_one_possibilities)  
print(word_two_possibilities)


