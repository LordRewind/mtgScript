import json
import re

cardList = {}
cardList['count'] = []
cardList['cards'] = []
cardCount = 0

targetLength = input("Target Card Length: ")
with open('AllCards.json', encoding="utf8") as json_file:
    data = json.load(json_file)
    print('Cards found:\n')
    for key, value in data.items():
        if 'Planeswalker' not in data[key]['types'] and 'Conspiracy' not in data[key]['types'] and 'Vanguard' not in data[key]['types']:
            if 'commander' in data[key]['legalities']:
                defaultRules = ''
                try:
                    rules = data[key]['text']
                except KeyError:
                    rules = ''
                rules = re.sub("\(.*\)","", rules)
                ruleLen = len(rules)
                if ruleLen > int(targetLength):
                    cardList['cards'].append({
                        'name': key,
                        'rules': rules,
                        'rulesLength': ruleLen
                    })
                    cardCount += 1
                    print(key)

print("Final Count: ", cardCount)

cardList['count'].append({
    'totalCards': cardCount
})

with open('LongRules.json', 'w') as outfile:
    json.dump(cardList,outfile)