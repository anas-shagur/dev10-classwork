drop database if exists movielens;
create database movielens;
use movielens;

create table movie (
	movie_id int primary key auto_increment,
    title varchar(512) not null
);

create table movie_rating(
	rating_id int primary key auto_increment,
    user_id int not null,
    movie_id int not null,
    rating decimal(2,1) not null,
    foreign key (movie_id) references movie(movie_id)
);