import json
from analyzer import analyze_organization

print("1. Start")

with open(
    "sample_joint.txt",
    "r",
    encoding="utf-8"
) as file:

    content = file.read()

print("2. File loaded")

result = analyze_organization(content)

print("3. Response received")

print(
    json.dumps(
        result,
        ensure_ascii=False,
        indent=2
    )
)

print("4. Saving file")

with open(
    "organization_profile.json",
    "w",
    encoding="utf-8"
) as output:

    json.dump(
        result,
        output,
        ensure_ascii=False,
        indent=2
    )

print("5. Done")