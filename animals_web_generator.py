import json


def load_data(file_path):
    """Loads a JSON file and returns its content as a Python object."""
    with open(file_path, "r") as animal_file:
        data = json.load(animal_file)
    return data


def main():
    """
    Reads 'animals_data.json' and generates a string with the animals’ data:
        - Name
        - Scientific name
        - First location
        - Lifespan (replaces weird characters with '-')
        - Temperament
        - Weight
        - Diet
    """
    animals_data = load_data("animals_data.json")

    animals_output = ""

    for animal in animals_data:
        name = animal.get("name", "Unknown")
        animals_output += f"Name: {name}\n"

        scientific_name = animal.get("taxonomy", {}).get("scientific_name", "Unknown")
        animals_output += f"Scientific Name: {scientific_name}\n"

        locations = animal.get("locations", [])
        first_location = locations[0] if locations else "Unknown"
        animals_output += f"Location: {first_location}\n"

        lifespan = animal.get("characteristics", {}).get("lifespan", "Unknown")
        if lifespan != "Unknown":
            lifespan = lifespan.replace("â€“", "-").replace(" – ", "-").replace(" - ", "-").replace("to", "-")
        animals_output += f"Lifespan: {lifespan}\n"

        temperament = animal.get("characteristics", {}).get("temperament", "Unknown")
        animals_output += f"Temperament: {temperament}\n"

        weight = animal.get("characteristics", {}).get("weight", "Unknown")
        animals_output += f"Weight: {weight}\n"

        diet = animal.get("characteristics", {}).get("diet", "Unknown")
        animals_output += f"Diet: {diet}\n"

        animals_output += "\n"  # Add a blank line between animals


    with open("animals_template.html", "r") as file:
        template_content = file.read()
