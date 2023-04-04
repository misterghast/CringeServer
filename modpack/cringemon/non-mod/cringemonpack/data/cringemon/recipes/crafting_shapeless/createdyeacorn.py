colors = ["red", "blue", "yellow", "white", "black", "pink", "green"]
for c in colors:
    file = open("{color}_apricorn_dye.json".format(color = c), 'wt')
    file.writelines("""{{
    "type": "crafting_shapeless",
    "group": "acorn_dye_recipe",
    "ingredients": [
        {{
            "item": "cobblemon:{color}_apricorn"
        }}
    ],
    "result": {{
        "item": "minecraft:{color}_dye"
    }}
}}""".format(color = c))
    file.close()