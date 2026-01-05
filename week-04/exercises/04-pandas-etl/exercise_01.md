# Gravel Family

We will use the `gravel_family` schema.

If you removed that schema, re-add it by executing `week-03/exercises/gravel-family-schema-data.sql` in MySQL Workbench.

1. Open MySQL Workbench and execute this query.

    ```sql
    use gravel_family;

    select
        p.project_id,
        p.customer_id,
        substr(p.description, instr(p.description, '--') + 3) proj_desc, -- ignore customer name
        sum(i.price_per_unit * pri.quantity) total
    from project p
    inner join project_item pri on p.project_id = pri.project_id
    inner join item i on pri.item_id = i.item_id
    group by p.project_id;
    ```

    This generates data for a specific project and customer, and sums our total.

2. In `04-pandas-etl/.env`, set your local MySQL credentials to the appropriate values.

3. Run `main.py` and confirm that we get connected to our `employee` table and write the first row.