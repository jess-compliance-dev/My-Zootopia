import json


def load_data(file_path):
    """Loads a JSON file and returns its content as a Python object."""
    with open(file_path, "r") as animal_file:
        data = json.load(animal_file)
    return data


def main():
    """
    Reads 'animals_data.json' and generates an HTML string with the animals’ data:
        - Name
        - Scientific name
        - First location
        - Lifespan (replaces weird characters with '-')
        - Temperament
        - Weight
        - Diet
    Replaces the placeholder in the template and writes the final HTML to 'animals.html'
    """
    animals_data = load_data("animals_data.json")

    animals_output = []

    for animal in animals_data:
        name = animal.get("name", "Unknown")
        name = name.replace("â€™", "’").replace("ï¿½", "’")

        scientific_name = animal.get("taxonomy", {}).get("scientific_name", "Unknown")

        type_ = animal.get("characteristics", {}).get("type", "Unknown").capitalize()

        locations = animal.get("locations", [])
        first_location = locations[0] if locations else "Unknown"

        lifespan = animal.get("characteristics", {}).get("lifespan", "Unknown")
        if lifespan != "Unknown":
            lifespan = (
                lifespan.replace("â€“", "-").replace("–", "-").replace("—", "-").replace(" to ", "-")
            )

        temperament = animal.get("characteristics", {}).get("temperament", "Unknown")
        temperament = temperament.replace("â€™", "’")

        weight = animal.get("characteristics", {}).get("weight", "Unknown")

        diet = animal.get("characteristics", {}).get("diet", "Unknown")

        animals_output.append('<li class="cards__item">\n')
        animals_output.append(f'  <div class="card__title">{name}</div>\n')
        animals_output.append('  <div class="card__text">\n')
        animals_output.append(f'      <div><strong>Scientific name:</strong> {scientific_name}</div>\n')
        animals_output.append(f'      <div><strong>Type:</strong> {type_}</div>\n')
        animals_output.append(f'      <div><strong>First location:</strong> {first_location}</div>\n')
        animals_output.append(f'      <div><strong>Lifespan:</strong> {lifespan}</div>\n')
        animals_output.append(f'      <div><strong>Temperament:</strong> {temperament}</div>\n')
        animals_output.append(f'      <div><strong>Weight:</strong> {weight}</div>\n')
        animals_output.append(f'      <div><strong>Diet:</strong> {diet}</div>\n')
        animals_output.append('  </div>\n')
        animals_output.append('</li>\n\n')

    animals_output = "".join(animals_output)

    with open("animals_template.html", "r") as file:
        template_content = file.read()

    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_output)

    with open("animals.html", "w") as file:
        file.write(final_html)


if __name__ == "__main__":
    main()
