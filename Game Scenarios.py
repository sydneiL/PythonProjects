#Define player instructions

gameplay_instructions={

#You need to stay as close to 0 as possible on the survival gauge.
"health":#stay strong and good
"thirst":#must gather food and useful items
"hunger":#same concept as hunger and health
"heat":100,#stay warm and secure in winter and days of bad weather
"security":100, #keep yourself and your campsite safe from predators during both day and night
"step":1,#step one completed
},
print("In this story, you are left in a mysterious forest because your camping group got lost trying to find an ancient cave full of treasure."),
print("In this scenario, you hope you and your friends survive to link up and find your way back to the site entrance to the road."),
print("You have to search for your friends alongside your two dogs and learn if your friends are still alive and looking for help")
#Describe available options

options={ 
    #In this scenario you need to complete tasks to survive in the forest until help arrives
    #You must hunt and forage for food, water, and build shelter to protect from predators and the elements
    #Use dogs to guard from dangerous animals
    #Relax but keep your eyes open for danger
    1:"Forage for food.",
    2:"Gather water from brook.",
    3:"Build makeshift shelter",
    4:"Protect from predators",
    5:"Relax",
    6:"Quit",
},
#Define possible events and results
events={
"Forage for food":#crafting weapon for hunting small game and foraging for wild plants for the night
"success":"Your game hunt was successful!. Your hunger is gone.",
"failure":"Hunt failed! Prey was too swift.",
},
"Collect water from stream":{#All campers must have clean water to drink for hydration
"success":"Clean brook found!",
"failure":"You failed at drawing water, and you endured dehydration.",
"affect":{"security":25, "health":-10},
},
"Construct shelter":{#Shelter will protect you from the rain and snow as well as apex predators
  "success":"Shelter built! You will be warm all night in the rain.",
  "failure":"You failed to build a shelter. You will endure the cold rain.",
  "affect":{"security":50,"health":40},
},
