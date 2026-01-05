# Fetch a GET request

1. In our `main.py` module, import `requests`.

2. Execute `requests.get` with the `API_URL` and assign it to a response.

3. Print the `response.json()` content. It should like similar to:

    ```js
    [
        {
            "order": "Coleoptera",
            "common_name": "Beetles",
            "insects": [
                {
                    "latin_name": "Coccinella septempunctata",
                    "common_name": "Seven-Spotted Ladybug"
                },
                {
                    "latin_name": "Harmonia axyridis",
                    "common_name": "Harlequin Ladybird"
                }
                // ...
            ]
        },
        {
            "order": "Hymenoptera",
            "common_name": "Ants, Bees, Wasps",
            "insects": [
                {
                    "latin_name": "Apis mellifera",
                    "common_name": "Western Honeybee"
                }
                // ...
            ]
        },
        {
            "order": "Diptera",
            "common_name": "Flies",
            "insects": [
                {
                    "latin_name": "Drosophila melanogaster",
                    "common_name": "Common Fruit Fly"
                }
                // ...
            ]
        }
    ]
    ```