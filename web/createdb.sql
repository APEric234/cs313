CREATE TABLE users(
 user_id  INT primary key
, fname   varchar(20)
, email  varchar(20));

create table characters(
 character_id  INT primary key
, fname   varchar(20)
,users_id int, agil  int,stre  int,wisd  int,intel  int,grace  int,
 foreign key (users_id) references users(user_id));
 
create table equipment(
 equip_id  INT primary key
, fname   varchar(20)
,characters_id int, agiBuff  int,streBuff  int,wisBuff  int,intelBuff  int,graceBuff  int,
 Special varchar(30), foreign key (characters_id) references characters(character_id));
