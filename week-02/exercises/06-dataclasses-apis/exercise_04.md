# Map `Order` and `Insect` to the GET response.

1. Our JSON content includes a list of orders and a nested list of insects. `response.json()` is a list of dictionaries. The `insects` key is also a list of dictionaries.

    Create a `list[Order]`, but don't forget about the `list[Insect]`. The `list[Insect]` `Order` initializer is a requirement.

2. Save the data to a CSV file.

    **Example**

    ```csv
    order_name,order_common_name,insect_latin_name,insect_common_name
    Coleoptera,Beetles,Coccinella septempunctata,Seven-Spotted Ladybug
    Coleoptera,Beetles,Harmonia axyridis,Harlequin Ladybird
    Hymenoptera,"Ants, Bees, Wasps",Apis mellifera,Western Honeybee
    ```