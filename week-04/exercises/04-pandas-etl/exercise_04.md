# Transformer.transform

Use individual methods to transform. This will be useful while testing.

1. Drop NA project_ids, customer_ids, and totals.

2. Replace NA proj_desc with an empty string.

3. Convert project_id and customer_id from `float` to `int`.

4. Remove duplicates.

5. _Enrich_ our data. Add a column that counts projects per customer.

## ETLProcessor.load

1. Load the `DataFrame`to a CSV file.