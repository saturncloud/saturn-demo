
import json

counter = 0 
batch = dict(runs=[])
for x in range(1):
    for y in range(5):
        batch['runs'].append(
            dict(cmd="jupyter nbconvert notebook.ipynb --output-dir ${SATURN_RESULTS_DIR} --to notebook  --execute")
        )
        counter += 1
with open("batch.json", "w+") as f:
    json.dump(batch, f)

