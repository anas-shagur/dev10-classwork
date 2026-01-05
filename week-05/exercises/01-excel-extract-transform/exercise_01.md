# Excel Extract, Transform, and Load

1. Open `palmerpenguins.xlsx` in our `01-excel-extract-transform` directory.

2. In our _Data_ tab, click the _Get Data (Power Query)_.

3. Select CSV as our data source and choose `penguins_raw.csv`.

4. Click _Transform Data_.

5. Our data automatically promotes headers and changes column types.

6. Remove the "studyName", "Sample Number", "Region", "Stage", "Individual ID", "Clutch Completion", "Delta 15 N (o/oo)", "Delta 13 C (o/oo)", and "Comments" columns.

7. Rename columns:

    - "Culmen Length (mm)": "bill_length_mm"
    - "Culmen Depth (mm)": "bill_depth_mm"
    - "Flipper Length (mm)": "flipper_length_mm"
    - "Body Mass (g)": "body_mass_g"
    - "Island": "island"
    - "Sex": "sex"
    - "Species": "species"
    - "Date Egg": "year"

8. Transform columns: use `Text.Lower` to lower case the "sex" column, but ignore "NA" values.

9. Transform columns: use `Text.BeforeDelimiter` to grab the first word in the "species" column.

10. Transform columns: use `Date.Year` to translate a date into a "year".

11. Reorder columns: "species", "island", "bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g", "sex", "year".

12. Filter rows: remove "NA" "bill_length_mm".

13. Change all numeric text to numbers: "bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g".