exit
python manage.py dbshell
show tables;

select * from django_migrations;
select * from django_migrations where id > 17;

 delete from django_migrations where id > 17;