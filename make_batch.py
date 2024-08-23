
import json

counter = 0 
batch = dict(runs=[])
for x in range(100):
    for y in range(5):
        batch['runs'].append(
            dict(cmd=f"python script.py {x} {y}")
        )
        counter += 1
with open("batch.json", "w+") as f:
    json.dump(batch, f)
