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

insert into users(user_id,fname,email) values (1,'Adam','heaven@rocks.com');
insert into users(user_id,fname,email) values (2,'Eve','heaven@humble.com');
insert into users(user_id,fname,email) values (0,'Jesus','love@rocks.com');

insert into characters(character_id,fname,users_id,agil,stre,wisd,intel,grace) values (0,'BibleMan',0,1,9,1,9,1);
insert into characters(character_id,fname,users_id,agil,stre,wisd,intel,grace) values (1,'PriestMan',1,7,4,6,9,7);
insert into characters(character_id,fname,users_id,agil,stre,wisd,intel,grace) values (2,'Temptress',2,5,5,12,2,100);

insert into equipment(equip_id,fname,characters_id,agiBuff) values(1,'Sword of Truth',1,2);

insert into equipment(equip_id,fname,characters_id,agiBuff) values(2,'Sword of Justice',0,3);

insert into equipment(equip_id,fname,characters_id,streBuff) values(3,'Sword of Vengeance',0,4);

insert into equipment(equip_id,fname,characters_id,graceBuff) values(1,'Helm of Angels',2,2);