FROM mysql

ENV MYSQL_DATABASE=mysqlsampledatabase \
	MYSQL_ROOT_PASSWORD=root_password

ADD bdd.sql /docker-entreypoint-initdb.d

EXPOSE 3306