pip-lab3

### Prerequestities:
- Download JDK8
- Download glassfish5
- Create table Results:
- In IDEA run once to create war archive

`psql -h pg -d studs`
```
CREATE TABLE Results (ID numeric not null, X numeric not null, Y numeric not null, R numeric not null, Included numeric);

ALTER TABLE Results ADD CONSTRAINT dept_pk PRIMARY KEY (ID);

CREATE SEQUENCE Results_seq START WITH 1;
```

`export JAVA_HOME="jdk8"`
`export JRE_HOME=$JAVA_HOME/jre`
`export PATH=$JAVA_HOME/bin:$JRE_HOME/bin:$PATH`
`cd glassfish5/bin/`
`./asadmin create-domain --domaindir ~/domains default3`
`./asadmin start-domain --domaindir ~/domains default3`
`./asadmin deploy ./target/Lab3.war`

Open terminal
`ssh -N -L 5353:localhost:8080 helios`

Open browser
http://localhost:5353/Lab3
