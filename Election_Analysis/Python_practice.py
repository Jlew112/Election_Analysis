counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

voting_data = []
voting_data.append({"county": "Arapahoe", "registered_voters": 422829})
voting_data.append({"county": "Denver", "registered_voters": 463353})
voting_data.append({"county": "Jefferson", "registered_voters": 432438})


# how many votes did you get?
#my_votes = int(input("How many votes did you get in the election?"))
candidate_votes = int(input("How many votes did the candidate get in the election?"))
# Total Votes in the election
total_votes = int(input("What is the total votes in the election?"))
# Calculate the percentage of votes you received.
#percentage_votes = (my_votes/ total_votes) * 100
#print(f"I received {my_votes/total_votes*100}% of the total votes.")
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes."
    f"The total Number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes/total_votes*100:.2f}% of the total votes.")
print(message_to_candidate)

counties = ["Arapahoe", "Denver", "Jefferson"]
#if counties[1] =='Denver':
    #print(counties[1])


#if "el Paso" in counties:
    #print("El Paso is in the list of counties.")
#else:
    #print('El Paso is not in the list of counties')

#if 'Arapahoe' in counties or 'El Paso' in counties:
    #print("Arapahoe or El Paso are in the list of counties.")    
#else:
    #print("Arapahoe and El Paso is not in the list of counties")

#for county in counties_dict:
    #print(counties_dict[county])
#for county, voters in counties_dict.items():
    #print(f"{county} county has {voters} registered voters.")

#for county_dict in voting_data:
    #for value in county_dict.values():
        #print(value)
    #print(county_dict['registered_voters'])

