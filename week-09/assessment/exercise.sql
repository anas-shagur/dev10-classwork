use role sysadmin;
use database demo_db;

create or replace schema exercise;
use schema exercise;

create or replace stage exercise_stage;
show stages;

list @exercise_stage;

create or replace file format EXERCISE_CSV
type = 'CSV'
skip_header = 1
FIELD_OPTIONALLY_ENCLOSED_BY = '"';

create or replace table raw_exercise (
    first_name string,
    exercise_class string,
    quantity int,
    reps_or_minutes string,
    equipment string
);

copy into raw_exercise
from (
    select
        $1::string,
        $2::string,
        $3::int,
        $4::string,
        $5::string
    from @exercise_stage/exercises.csv
    (file_format => EXERCISE_CSV)
);

select * from raw_exercise;

create or replace table person (
    person_id int autoincrement(1,1),
    first_name string,
    primary key (person_id)
);

create or replace table exercise (
    exercise_id int autoincrement(1,1),
    name string,
    primary key (exercise_id)
);

create or replace table equipment (
    equipment_id int autoincrement(1,1),
    name string,
    primary key (equipment_id)
);

create or replace table person_exercise (
    person_id int,
    exercise_id int,
    quantity int,
    reps_or_minutes string,
    primary key (person_id, exercise_id)
);

create or replace table exercise_equipment (
    exercise_id int,
    equipment_id int,
    primary key (exercise_id, equipment_id)
);

merge into person p
using (
    select distinct first_name
    from raw_exercise
) tbl
on p.first_name = tbl.first_name
when not matched then
insert (first_name)
values (tbl.first_name);

merge into exercise e
using (
    select distinct exercise_class
    from raw_exercise
) tbl
on e.name = tbl.exercise_class
when not matched then
insert (name)
values (tbl.exercise_class);

insert into equipment (name)
select distinct
    eq.value::string
from raw_exercise r,
lateral flatten(input => split(r.equipment,';')) eq;

insert into person_exercise
select
    p.person_id,
    e.exercise_id,
    r.quantity,
    r.reps_or_minutes
from raw_exercise r
join person p on r.first_name = p.first_name
join exercise e on r.exercise_class = e.name;

insert into exercise_equipment
select distinct
    e.exercise_id,
    eq.equipment_id
from raw_exercise r
join exercise e on r.exercise_class = e.name,
lateral flatten(input => split(r.equipment,';')) f
join equipment eq on f.value::string = eq.name;

create or replace file format EXERCISE_JSON
type = 'JSON'
allow_duplicate = true
strip_outer_array = true;

create or replace table raw_exercise_json (
    src variant
);

copy into raw_exercise_json
from (
    select
        $1
    from @exercise_stage/exercises.json
    (file_format => EXERCISE_JSON)
);

select * from raw_exercise_json;

select
    src:first_name,
    src:exercise_class,
    src:quantity
from raw_exercise_json;

create or replace view exercise_view as
select
    src:first_name::string first_name,
    src:exercise_class::string exercise_class,
    src:quantity::int quantity,
    src:reps_or_minutes::string reps_or_minutes,
    eq.value::string equipment
from raw_exercise_json,
lateral flatten(input => src:equipment) eq;

select * from exercise_view;