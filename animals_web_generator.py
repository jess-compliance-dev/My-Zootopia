from data_fetcher import fetch_data


def main():
    animal_name = input("Which animal would you like to learn more about: ").strip()
    animals_data = fetch_data(animal_name)

    if animals_data:
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
    else:
        animals_output = f'<h2 style="color:red; text-align:center;">The animal "{animal_name}" doesn\'t exist.</h2>'

    with open("animals_template.html", "r") as file:
        template_content = file.read()

    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_output)

    with open("animals.html", "w") as file:
        file.write(final_html)

    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()