import json


def load_data(file_path):
    """Loads a JSON file and returns its content as a Python object."""
    with open(file_path, "r") as animal_file:
        data = json.load(animal_file)
    return data


def main():
    """
    Reads 'animals_data.json' and prints for each animal:
        - Name
        - Scientific name
        - First location
        - Lifespan (replaces weird characters with '-')
        - Temperament
        - Weight
        - Diet
    """
    animals_data = load_data("animals_data.json")

    for animal in animals_data:
        name = animal.get("name", "Unknown")
        print("Name:", name)

        scientific_name = animal.get("taxonomy", {}).get("scientific_name", "Unknown")
        print("Scientific Name:", scientific_name)

        locations = animal.get("locations", [])
        first_location = locations[0] if locations else "Unknown"
        print("Location:", first_location)

        lifespan = animal.get("characteristics", {}).get("lifespan", "Unknown")
        if lifespan != "Unknown":
            lifespan = lifespan.replace("â€“", "–").replace(" – ", "–").replace(" - ", "–").replace("to", "–" )
        print("Lifespan:", lifespan)

        temperament = animal.get("characteristics", {}).get("temperament", "Unknown")
        print("Temperament:", temperament)

        weight = animal.get("characteristics", {}).get("weight", "Unknown")
        print("Weight:", weight)

        diet = animal.get("characteristics", {}).get("diet", "Unknown")
        print("Diet:", diet)

        print()


main()

# Step 1: Read the content of the template
with open("animals_template.html", "r") as file:
    template_content = file.read()