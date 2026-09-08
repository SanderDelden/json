import json

from jsonschema import Draft202012Validator, ValidationError, validate

with open("schemas/device.schema.json") as f:
    schema = json.load(f)
with open("device.json") as f:
    instance = json.load(f)

try:
    validate(instance=instance, schema=schema, cls=Draft202012Validator)
except ValidationError as e:
    print(f"Invalid: {e.message} at {list(e.path)}")
else:
    print("JSON is valid")
