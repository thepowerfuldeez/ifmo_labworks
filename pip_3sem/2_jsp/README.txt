s257847@helios:/opt/glassfish3/glassfish/bin$ ./asadmin create-domain --domaindir ~/domains/
s257847@helios:/opt/glassfish3/glassfish/bin$ ./asadmin start-domain --domaindir ~/domains/ default4
s257847@helios:/opt/glassfish3/glassfish/bin$ ./asadmin deploy ~/../lab3/

Admin console
ssh -L 9999:localhost:41933 s257847@helios.cs.ifmo.ru -p 2222
App
ssh -L 9998:localhost:8080 s257847@helios.cs.ifmo.ru -p 2222


psql -h pg -d ucheb