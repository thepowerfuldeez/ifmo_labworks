select man_1.Имя, man_2.Имя, Покемоны.Имя from Сражения 
	join (select ИД, Люди_ИД from Тренер_покемонов) as trener_1 on Сражения.Участник_1 = trener_1.ИД 
	join (select ИД, Люди_ИД from Тренер_покемонов) as trener_2 on Сражения.Участник_2 = trener_2.ИД 
	join (select ИД, Имя, Локация from Люди) as man_1 on trener_1.Люди_ИД = man_1.ИД 
	join (select ИД, Имя, Локация from Люди) as man_2 on trener_2.Люди_ИД = man_2.ИД 
	join (select ИД, Город from Регионы) as reg_1 on man_1.Локация = reg_1.ИД
	join (select ИД, Город from Регионы) as reg_2 on man_2.Локация = reg_2.ИД 
	join (select ИД, Название from Город) as city_1 on reg_1.Город = city_1.ИД 
	join (select ИД, Название from Город) as city_2 on reg_2.Город = city_2.ИД 
	join (select ИД, Город from Регионы) as reg_3 on Сражения.Локация = reg_3.ИД
	join (select ИД, Название from Город) as city_3 on reg_3.Город = city_3.ИД 
	join (select ИД, Человек_1 from Отношения_между_людьми) as relat_1 on man_1.ИД = relat_1.Человек_1 
	join (select ИД, Человек_2 from Отношения_между_людьми) as relat_2 on man_2.ИД = relat_2.Человек_2 
	join Способности on Сражения.Последняя_способность = Способности.ИД
	join Покемон_способности on Способности.ИД = Покемон_способности.Способности_ИД
	join Покемоны on Покемон_способности.Покемон_ИД = Покемоны.ИД
	where city_1.Название !~ city_2.Название 
		and (left(city_3.Название,1) ~ (left(man_1.Имя,1)) or left(city_3.Название,1) ~ (left(man_2.Имя,1)))
		and (select Статус from Отношения_между_людьми where Человек_1 = relat_1.Человек_1 and Человек_2 = relat_2.Человек_2) ~* 'враги';