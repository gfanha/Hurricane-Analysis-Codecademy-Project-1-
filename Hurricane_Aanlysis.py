## Hurricane_Aanlysis
## Gonçalo Fanha - gfanha13@gmail.com 
## v1.0 - November 2021

##DATA COLLECTION
# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

## UPDATE DAMAGES LIST 
def update_damages(damages):
    conversion = {"M": 1000000, "B": 1000000000}
    # Initialize damages_updated_list
    damages_updated_list = []
    # Go through all the entries in damages list
    for item in damages:        
        if('M' in item) == True:
            item = float((item.replace('M',''))) * conversion['M']
        elif ('B' in item) == True:
            item = float((item.replace('B',''))) * conversion['B']
        # insert result in the updated list
        damages_updated_list.append(item)
    # return the created list to outside the function
    return damages_updated_list

damages_updated_list = update_damages(damages)

## CREATE DICTIONARY WITH ALL THE DATA
def collecting_data(names, months, years, max_sustained_winds, areas_affected , damages_updated_list, deaths):
    # Initialize variables
    all_data = []
    collected_data = {}
    # Go through every data point
    for num in range(len(names)):
        # Initialize individual dictionary for each data point
        individual_data = {}
        # Fill dictionary 
        individual_data['Name'] = names[num]
        individual_data['Month'] = months[num]
        individual_data['Year'] = years[num]
        individual_data['Max Sustained Wind'] = max_sustained_winds[num]
        individual_data['Areas Affected'] = areas_affected[num]
        individual_data['Damages'] = damages_updated_list[num]
        individual_data['Deaths'] = deaths[num]
        # Assign individual dictionary as value to key in overall dictionary
        collected_data[names[num]] = individual_data
    return collected_data

collected_data = collecting_data(names, months, years, max_sustained_winds, areas_affected , damages_updated_list, deaths)

## ORGANIZE DATA BY YEAR
def organize_by_year(collected_data, years, names):
    # Initialize variables
    data_by_year = {}
    #Find year window
    max_year = max(years)
    min_year = min(years)
    #Go through every year to find occurences
    for year in range(min_year, max_year + 1, 1):
        # create intermidiate variable to group occurences in the same year
        collected_data_updated = []   
        # search for hurricanes in each year
        for num in range(len(collected_data)):
            if collected_data[names[num]]['Year'] == year:
                # Append to list every occurence in each list
                collected_data_updated.append(collected_data[names[num]])
                # For every key: year corresponds the list with every occurence for that year
                data_by_year[year] = collected_data_updated
    return data_by_year

data_by_year = organize_by_year(collected_data, years, names)

## ORGANIZE DATA BY AREA AFFECTED 

def count_affected_areas(areas_affected):
    #Initialize variables
    data_by_area = {}
    sorted_data_by_area = {}
    sorted_keys = []
    # Create dictionary with all the affected areas and the number of occurences in each area (key = Area Value = no. occurences)
    for event in areas_affected:
        for area in event:
            # if the area isn't created it will assign 1 occurence, if it already exists it will sum 1 occurence to the current count
            if (area in data_by_area) == False:
                data_by_area[area] = 1 
            else:
                data_by_area[area] +=1
    #sort the dictionary so that the order goes from the most to the least affected area (OPTIONAL)
    sorted_keys = sorted(data_by_area, key=data_by_area.get, reverse =True)
    for num in sorted_keys:
        sorted_data_by_area[num] = data_by_area[num]
    #return sorted dictionary
    return sorted_data_by_area

sorted_data_by_area = count_affected_areas(areas_affected)

## FIND THE MOST AFFECTED AREA

def most_affected_area(sorted_data_by_area):
    # As the dictionary is sorted, the area that was hit the most is the first entry in the dictionary
    # Get the area from the 1st key of the dictionary
    most_affected = list(sorted_data_by_area.keys())[0]
    # Get the number of occurences for the area
    no_occurences = list(sorted_data_by_area.values())[0]
    # print information
    print('The most affected area was ' + most_affected + ' and it was hit ' + str(no_occurences) + ' times.')

most_affected_area(sorted_data_by_area)

# fIND THE DEADLIEST HURRICANE 

def deadliest_hurricane(names,deaths):
    index = deaths.index(max(deaths))
    no_deaths = max(deaths)
    hurricane = names[index]
    print(hurricane + ' was the deadliest hurricane and it caused ' + str(no_deaths) + ' casualties')

deadliest_hurricane(names,deaths)

## RANK HURRICANES BY DEATH RATE

def rank_by_deaths(names, months, years, max_sustained_winds, areas_affected , damages_updated_list, deaths):
# Ranking logic
    mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
# Initialize variables 
    rank_by_deaths = {}
    rank_1 = []
    rank_2 =[]
    rank_3 = []
    rank_4 = []
    rank_5 = []
    for num in range(len(names)):
        #Initialuize individual dictionary
        individual_data = {}
        # Assign values to individual dictionary
        individual_data['Name'] = names[num]
        individual_data['Month'] = months[num]
        individual_data['Year'] = years[num]
        individual_data['Max Sustained Wind'] = max_sustained_winds[num]
        individual_data['Areas Affected'] = areas_affected[num]
        individual_data['Damages'] = damages_updated_list[num]
        individual_data['Deaths'] = deaths[num]
        # Rank the hurricanes by death rate
        if deaths[num] < mortality_scale[1] :
            rank_1.append(individual_data)
        elif deaths[num] >= mortality_scale[1] and deaths[num] < mortality_scale[2]:
            rank_2.append(individual_data)
        elif deaths[num] >= mortality_scale[2] and deaths[num] < mortality_scale[3]:
            rank_3.append(individual_data)
        elif deaths[num] >= mortality_scale[3] and deaths[num] < mortality_scale[4]:
            rank_4.append(individual_data)
        elif  deaths[num] > mortality_scale[4]:
            rank_5.append(individual_data)
        # Create new dicitonary with ranking by death rate
        rank_by_deaths = {1: rank_1,
                   2: rank_2,
                   3: rank_3,
                   4: rank_4,
                   5: rank_5}
    return rank_by_deaths

rank_by_deaths = rank_by_deaths(names, months, years, max_sustained_winds, areas_affected , damages_updated_list, deaths)

## GET THE HURRICANE THAT CAUSED THE MOST DAMAGE IN USD

def costly_hurricane(names,damages_updated_list):
    # Change internal damages list to eliminate string 'Damages not recorded' from list so that every entry is float
    # where there was the string 'Damages not recorded' we will put -1
    for num in range(len(names)):
        if damages_updated_list[num] == 'Damages not recorded':
            damages_updated_list[num] = -1     
    # find where maximum damage in list with floats only occurs
    index = damages_updated_list.index(max(damages_updated_list))    
    # get value for max damage 
    max_damage = max(damages_updated_list)
    # get hurricane name for the max damage
    hurricane = names[index]
    # print informations
    print(hurricane + ' was the most costly and it caused ' + str(max_damage) + ' USD in damages')

costly_hurricane(names,damages_updated_list)

## RANK THE HURRICANES BY DAMAGE CAUSED IN USD

def rank_by_damage(names, months, years, max_sustained_winds, areas_affected , damages_updated_list, deaths):
# Ranking logic
    damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
# Initialize variables 
    rank_by_damage = {}
    rank_1 = []
    rank_2 =[]
    rank_3 = []
    rank_4 = []
    rank_5 = []
    for num in range(len(names)):
        #Initialuize individual dictionary
        individual_data = {}
        # Assign values to individual dictionary
        individual_data['Name'] = names[num]
        individual_data['Month'] = months[num]
        individual_data['Year'] = years[num]
        individual_data['Max Sustained Wind'] = max_sustained_winds[num]
        individual_data['Areas Affected'] = areas_affected[num]
        individual_data['Damages'] = damages_updated_list[num]
        individual_data['Deaths'] = deaths[num]
        # Rank the hurricanes by damage costs
        if individual_data['Damages'] < damage_scale[1] :
            individual_data['Damages'] = 'Damages not recorded'
            rank_1.append(individual_data)
        elif individual_data['Damages'] >= damage_scale[1] and individual_data['Damages'] < damage_scale[2]:
            rank_2.append(individual_data)
        elif individual_data['Damages'] >= damage_scale[2] and individual_data['Damages'] < damage_scale[3]:
            rank_3.append(individual_data)
        elif individual_data['Damages'] >= damage_scale[3] and individual_data['Damages'] < damage_scale[4]:
            rank_4.append(individual_data)
        elif  individual_data['Damages'] > damage_scale[4]:
            rank_5.append(individual_data)
            # Create new dicitonary with ranking by damage cost
        rank_by_damage = {1: rank_1,
                   2: rank_2,
                   3: rank_3,
                   4: rank_4,
                   5: rank_5}
    return rank_by_damage

rank_by_damage = rank_by_damage(names, months, years, max_sustained_winds, areas_affected , damages_updated_list, deaths)