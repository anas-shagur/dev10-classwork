drop database if exists movie_review;
create database movie_review;
use movie_review;

create table genre (
    genre_id int primary key auto_increment,
    `name` varchar(50) not null unique
);

create table movie (
    movie_id int primary key auto_increment,
    `name` varchar(100) not null,
    genre_id int not null,
    release_year int not null,
    constraint fk_movie_genre_id
        foreign key (genre_id) 
        references genre(genre_id)
);

create table customer (
    customer_id int primary key auto_increment,
    `name` varchar(100) not null,
    email varchar(256) not null unique
);

create table review (
    review_id int primary key auto_increment,
    movie_id int not null,
    customer_id int not null,
    rating decimal(4,2) not null,
    review_date date not null,
    constraint fk_review_movie_id
        foreign key (movie_id) 
        references movie(movie_id),
    constraint fk_review_customer_id
        foreign key (customer_id) 
        references customer(customer_id)
);

insert into genre (`name`) values 
    ('Action'), ('Comedy'), ('Drama'), ('Horror'), ('Sci-Fi'), ('Thriller'), ('Musical');

insert into movie (`name`, release_year, genre_id) values
    ('Wicked', 2024, 7),
    ('Bridesmaids', 2011, 2),
    ('Nickel Boys', 2024, 3),
    ('The Exorcist', 1973, 4),
    ('Alien: Romulus', 2024, 5),
    ('The Killing of a Sacred Deer', 2017, 6);

insert into customer (`name`, email) values
    ('Omar Podd','opoddbv@delicious.com'),
    ('Benita Adamsky','badamskybw@acquirethisname.com'),
    ('Hobard Sesons','hsesonsbx@reddit.com'),
    ('Sabrina Prinnett','sprinnettby@cargocollective.com'),
    ('Lion Portwain','lportwainbz@slideshare.net'),
    ('Jessi Veld','jveldc0@ucsd.edu'),
    ('Chandra MacRinn','cmacrinnc1@ca.gov'),
    ('Dill Bice','dbicec2@businessinsider.com'),
    ('Rosa Brothers','rbrothersc3@gnu.org'),
    ('Nicolea Setterfield','nsetterfieldc4@engadget.com'),
    ('Crichton Gulk','cgulkc5@hhs.gov'),
    ('Brittani Fife','bfifec6@mail.ru'),
    ('Patten Capner','pcapnerc7@topsy.com'),
    ('Claire Plom','cplomc8@marriott.com'),
    ('Noel Chittey','nchitteyc9@ed.gov'),
    ('Mickie Barense','mbarenseca@macromedia.com'),
    ('Kenton Slimm','kslimmcb@wired.com'),
    ('Mandy Neljes','mneljescc@canalblog.com'),
    ('Alvy Shingfield','ashingfieldce@t.co'),
    ('Helli Suller','hsullercf@marketwatch.com'),
    ('Stesha Lammerich','slammerichcg@imageshack.us'),
    ('Carmencita Tingey','ctingeych@google.co.jp');

-- insert into review (movie_id, customer_id, rating, review_date)
--     select
--         m.movie_id,
--         c.customer_id,
--         round(rand() * 9.0 + 1.0, 2),
--         date_add(curdate(), interval -floor(rand() * 365) day) 
--     from movie m
--     cross join customer c;

insert into review (movie_id, customer_id, rating, review_date) values
(2,19,9.41,'2024-12-17'),
(2,2,4.55,'2024-03-27'),
(2,12,4.67,'2024-12-24'),
(2,11,1.67,'2024-01-30'),
(2,7,4.49,'2024-12-07'),
(2,14,8.14,'2024-04-08'),
(2,22,2.87,'2024-04-10'),
(2,8,8.03,'2024-06-26'),
(2,6,9.99,'2024-10-24'),
(2,17,4.05,'2024-10-22'),
(2,5,8.00,'2024-09-12'),
(2,16,9.22,'2024-07-17'),
(2,10,4.21,'2024-07-22'),
(2,1,9.65,'2025-01-10'),
(2,13,6.64,'2024-05-03'),
(2,9,4.55,'2024-09-03'),
(2,21,4.07,'2024-04-21'),
(2,4,5.63,'2024-05-18'),
(3,2,4.70,'2024-04-21'),
(3,12,8.73,'2024-01-13'),
(3,7,5.04,'2024-01-31'),
(3,14,9.65,'2024-04-17'),
(3,22,5.81,'2024-04-07'),
(3,8,4.47,'2024-03-29'),
(3,20,8.44,'2024-11-12'),
(3,6,2.91,'2024-02-07'),
(3,5,1.47,'2024-11-03'),
(3,16,3.67,'2024-09-01'),
(3,18,9.97,'2024-12-12'),
(3,15,7.76,'2024-11-20'),
(3,10,2.49,'2024-04-04'),
(3,1,7.14,'2024-06-05'),
(3,13,2.33,'2024-03-19'),
(3,9,2.89,'2024-10-28'),
(3,21,2.89,'2024-01-14'),
(3,4,5.07,'2024-01-21'),
(4,19,8.87,'2024-10-31'),
(4,2,9.42,'2024-08-02'),
(4,12,8.91,'2024-12-05'),
(4,11,2.91,'2024-01-23'),
(4,7,3.15,'2024-08-05'),
(4,8,1.54,'2024-04-25'),
(4,20,1.37,'2024-01-15'),
(4,6,6.04,'2024-08-25'),
(4,17,6.06,'2024-05-08'),
(4,5,4.22,'2025-01-01'),
(4,18,3.53,'2024-01-23'),
(4,15,6.83,'2024-06-28'),
(4,1,9.01,'2024-10-04'),
(4,13,8.18,'2024-09-20'),
(4,4,3.07,'2024-08-07'),
(5,2,5.37,'2024-12-13'),
(5,12,1.85,'2024-08-06'),
(5,11,6.83,'2024-12-30'),
(5,22,1.57,'2024-07-19'),
(5,8,5.75,'2024-07-01'),
(5,3,4.61,'2024-03-25'),
(5,20,7.96,'2024-12-15'),
(5,6,6.42,'2024-07-22'),
(5,17,4.98,'2024-08-26'),
(5,18,5.35,'2024-11-18'),
(5,15,4.56,'2024-06-18'),
(5,10,1.61,'2024-02-24'),
(5,13,1.02,'2024-06-20'),
(5,9,3.81,'2024-04-10'),
(5,4,8.92,'2024-06-15'),
(6,12,3.91,'2025-01-06'),
(6,11,6.10,'2024-12-16'),
(6,7,3.50,'2024-12-12'),
(6,22,8.99,'2024-01-31'),
(6,8,8.97,'2024-12-28'),
(6,3,1.84,'2024-04-17'),
(6,20,2.65,'2024-10-06'),
(6,6,7.89,'2024-11-06'),
(6,17,4.84,'2024-02-01'),
(6,5,6.08,'2024-06-30'),
(6,16,1.12,'2024-09-28'),
(6,18,8.91,'2024-08-09'),
(6,10,2.08,'2024-07-17'),
(6,13,6.24,'2024-11-17'),
(6,9,4.09,'2024-10-05'),
(6,21,8.45,'2024-08-31'),
(6,4,3.49,'2024-02-02'),
(1,19,8.89,'2024-09-19'),
(1,12,8.04,'2024-06-30'),
(1,11,1.11,'2024-02-09'),
(1,7,5.71,'2024-04-05'),
(1,3,4.37,'2024-10-14'),
(1,20,7.72,'2024-02-23'),
(1,6,8.94,'2024-02-23'),
(1,17,1.67,'2024-04-19'),
(1,5,1.76,'2024-04-07'),
(1,16,3.85,'2024-06-08'),
(1,18,7.21,'2024-01-15'),
(1,15,8.53,'2024-04-14'),
(1,10,7.22,'2024-12-27'),
(1,1,3.66,'2024-12-20'),
(1,13,2.06,'2024-06-10'),
(1,9,6.20,'2024-03-19'),
(1,21,6.39,'2024-02-08');
