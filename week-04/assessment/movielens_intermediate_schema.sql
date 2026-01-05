drop database if exists movielens;
create database movielens;
use movielens;

create table movie (
	movie_id int primary key auto_increment,
    title varchar(512) not null,
    release_year int not null
);

create table movie_rating(
	rating_id int primary key auto_increment,
    user_id int not null,
    movie_id int not null,
    rating decimal(2,1) not null,
    rating_date datetime not null,
    foreign key (movie_id) references movie(movie_id)
);

create table genre(
	genre_id int primary key auto_increment,
    name varchar(128) not null
);

create table movie_genre(
	movie_id int not null,
    genre_id int not null,
    primary key(movie_id, genre_id),
    foreign key (movie_id) references movie(movie_id),
    foreign key (genre_id) references genre(genre_id)
);