CREATE TABLE users(
 user_id  INT primary key
, fname   varchar(20)
, email  varchar(20));

create table characters(
 character_id  INT primary key
, fname   varchar(20)
,users_id int, agi  int,str  int,wis  int,intel  int,charisma  int,
 foreign key (users_id) references users(user_id));
 
create table equipment(
 character_id  INT primary key
, fname   varchar(20)
,users_id int, agi  int,str  int,wis  int,intel  int,charisma  int,
 foreign key (users_id) references users(user_id));
