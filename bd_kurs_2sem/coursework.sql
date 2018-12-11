create table Дом (
  Ид_дома           serial primary key,
  Ид_крыши          integer references Крыши not null,
  Наличие_лифта     integer,
  Количество_этажей integer,
  Год_постройки     integer
);
create table Дом_локация (
  Ид_дома  serial primary key,
  Адрес    text,
  Ид_метро integer references Метро,
  Ид_район integer references Район
);
create table Метро (
  Ид_метро serial primary key,
  Название text not null,
  Ид_ветка integer
);
create table Крыши (
  Ид_крыши  serial primary key,
  Ид_замка  integer references Замки,
  Тип_крыши integer,
  Наклон    integer
);
create table Район (
  Ид_район  serial primary key,
  Название  text    not null,
  Население integer not null,
  check (Население > 0)
);
create table Замки (
  Ид_замка         serial primary key,
  Тип_замка        integer  not null,
  Сложность_взлома smallint not null,
  Материал         text,
  check (Тип_замка in (1, 2, 3))
);
create table Особенности_крыши (
  Ид_крыши       serial references Крыши,
  Сложность_залаза integer,
  Актуальность_информации timestamp,
  Количество_полиц_пунктов integer,
  check (Количество_полиц_пунктов >= 0)
);
create table Несчастные_случаи (
  Ид_случая             serial primary key,
  Ид_полиц_пункта       integer references Полицейские_пункты,
  Тип           text not null,
  Описание text not null
);
create table Крыша_несчастные_случаи (
  Ид_крыши serial references Крыши,
  Количество_несчастных_случаев integer
);
create table Полицейские_пункты (
  Ид_полиц_пункта           serial primary key,
  Ид_район    integer references Район on delete cascade,
  Ид_метро integer references Метро not null,
  Название       text,
  Адрес_пункта text
);

create index locks
  on Замки
  using btree (Тип_замка);
create index subway
  on Метро
  using btree (Ид_ветка);

insert into Замки (Тип_замка, Сложность_взлома, Материал)
values (1, 2, 'Металл'), (1, 3, 'Картон');
insert into Крыши (Ид_замка, Тип_крыши, Наклон)
values (1, 1, 1), (1, 1, 1), (1, 1, 2);
insert into Дом (Ид_крыши, Наличие_лифта, Количество_этажей, Год_постройки)
values (1, 0, 5, 1898), (2, 1, 19, 2009), (3, 1, 9, 1990);
insert into Метро (Название, Ид_ветка)
values ('Невский проспект', 2), ('Приморская', 3);
insert into Район (Название, Население)
values ('Приморский', 480000), ('Центральный', 200000);
insert into Дом_локация (Адрес, Ид_метро, Ид_район)
values ('ул. Рылеева 15', 1, 2), ('ул. Кораблестроителей 29/3', 2, 1);
insert into Особенности_крыши (Ид_крыши, Сложность_залаза, Актуальность_информации, Количество_полиц_пунктов)
values (1, 3, '2016-06-22 19:10:25-07', 0), (2, 9, '2018-06-22 19:10:25-07', 8);
insert into Полицейские_пункты (Ид_район, Ид_метро, Название, Адрес_пункта)
values (2, 1, 'Центральный ПП', 'Невский проспект 1'), (1, 2, 'Приморский ПП', 'ул. Кораблестроителей 18');
insert into Несчастные_случаи (Ид_полиц_пункта, Тип, Описание)
values (2, 'Падение', 'Упал с крыши'), (2, 'Ранение', 'Порезался об замок');
insert into Крыша_несчастные_случаи (Ид_крыши, Количество_несчастных_случаев)
values (2, 8);

-- create or replace function update_evolve()
--   returns trigger as $$
-- declare
--   home_id   integer;
--   subway_id integer;
--   region_id integer;
-- begin
--   home_id = new.Ид_дома;
--   select Ид_дома
--   into subway_id
--   from Дом_локация
--   where Ид_дома = home_id;
--   if ((select Ид_дома
--        from Дом
--        where ИД = new.Эволюция)
--       > (select Стадия
--          from Эволюция
--          where ИД = old.Эволюция))
--   then
--     update Покемоны
--     set Имя = (select Название
--                from Эволюция
--                where ИД = new.Эволюция)
--     where ИД = home_id;
--     select ИД
--     into region_id
--     from Способности
--     where Урон > (select Урон
--                   from Способности
--                   where ИД = subway_id
--                   order by Урон)
--     limit 1;
--     delete from Покемон_способности
--     where Покемон_ИД = home_id;
--     insert into Покемон_способности values (home_id, region_id);
--   else update Покемоны
--   set Имя = (select Название
--              from Эволюция
--              where ИД = new.Эволюция)
--   where ИД = home_id;
--     select ИД
--     into region_id
--     from Способности
--     where Урон < (select Урон
--                   from Способности
--                   where ИД = subway_id
--                   order by Урон)
--     limit 1;
--     delete from Покемон_способности
--     where Покемон_ИД = home_id;
--     insert into Покемон_способности values (home_id, region_id);
--   end if;
--   return null;
-- end;
-- $$
-- language plpgsql;
--
-- create trigger check_evolve
--   after update
--   on Покемоны
--   for each row
--   when (new.Эволюция != old.Эволюция)
-- execute procedure update_evolve();