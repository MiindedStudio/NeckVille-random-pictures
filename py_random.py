import os
import json
import random
from shutil import copyfile

dirJson = "./json"
dirRandomised = "./recreated"
dirIPFS = "QmT4cWPD7ChP9sDTwSQDorjA4enHut4nEP6GB5dkAUtWpx"
metadata = os.listdir(dirJson)

# stats 
stats = {"total":0}

# function to recreate json file
def recreate(id, to):
    with open(f"{dirJson}/{id}.json") as f:
        data = json.load(f)
        
    newJson = {
        "name": f"NeckVille #{to}",
        "description": "NeckVille is home to 5,555 different inhabitants known as NeckVillians who go about their lives working, playing, and exploring the first living town within the MetaVerse.",
        "image": f"ipfs://{dirIPFS}/{id}.png",
        "dna": data["dna"],
        "edition": data["edition"],
        "date": data["date"],
        "attributes": data["attributes"],
        "compiler": data["compiler"],
    }
    
    tier = data["attributes"][0]["value"]
    
    if tier not in stats:
        stats[tier] = 0
        
    stats[tier] += 1
    stats["total"] += 1
    
    with open(f"{dirRandomised}/{to}", 'w') as outfile:
        json.dump(newJson, outfile, indent=2)
    

# before random: 
#   check tiers 6 pictures: #903, #2560, #2810, #5029, #2683, #2815, #2906, #5281, #3230, #4089
#   Mayor has to be a tier 6: the picture #903 will be the Mayor #1

# recreate the #903 to be Mayor #1
recreate(903, 1)

# remove the #903 in the json files list
metadata.remove("903.json")

# run random
random.seed(20220111) # the seed is the reveal date
random.shuffle(metadata) # run random on metadata

tokenId = 2 #start from #2 to skip Mayor #1

for data in metadata:

    # get previous id
    id = int(data.replace(".json",""))
    
    # recreate the new json file
    recreate(id, tokenId)
    
    tokenId += 1
    
    
print(stats)