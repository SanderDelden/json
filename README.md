# JSON

This repository contains JSON files and schemas for playing around with
validating network device configurations.

Two JSON files are present, one containing valid data (`device.json`) and one
containing invalid data (`bad_device.json`). The invalid data is meant to
demonstrate schema validation failures, currently it fails because the `enabled`
field of interface `Ethernet1` is set to `"true"` instead of a boolean value.

> [!NOTE]
> The command examples in this README make use of
> [uv](https://docs.astral.sh/uv/#installation).

## Validating with JSON Schema

You can validate the JSON files against the provided schemas with the CLI tool
[`check-jsonschema`](https://github.com/python-jsonschema/check-jsonschema)
using the following commands:

```bash
uvx check-jsonschema --schemafile schemas/device.schema.json device.json
uvx check-jsonschema --schemafile schemas/device.schema.json bad_device.json
```

It is also possible to use the
[`jsonschema`](https://github.com/python-jsonschema/jsonschema) library directly
in a Python script:

```bash
uv run --with jsonschema validate.py
```

> [!TIP]
> Edit `validate.py` to specify the JSON file you want to validate.
