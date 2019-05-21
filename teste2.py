(advogar-web) keline@keline-Vostro-V131:~/advogar-web$ psql -U postgres
psql (10.6 (Ubuntu 10.6-0ubuntu0.18.04.1))
Type "help" for help.

postgres=# \l
                                   List of databases
    Name     |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-------------+----------+----------+-------------+-------------+-----------------------
 advogar-web | postgres | UTF8     | pt_BR.UTF-8 | pt_BR.UTF-8 | 
 bfr         | postgres | UTF8     | pt_BR.UTF-8 | pt_BR.UTF-8 | 
 dvdrental   | postgres | UTF8     | pt_BR.UTF-8 | pt_BR.UTF-8 | 
 postgres    | postgres | UTF8     | pt_BR.UTF-8 | pt_BR.UTF-8 | 
 template0   | postgres | UTF8     | pt_BR.UTF-8 | pt_BR.UTF-8 | =c/postgres          +
             |          |          |             |             | postgres=CTc/postgres
 template1   | postgres | UTF8     | pt_BR.UTF-8 | pt_BR.UTF-8 | =c/postgres          +
             |          |          |             |             | postgres=CTc/postgres
(6 rows)

postgres=# \q
(advogar-web) keline@keline-Vostro-V131:~/advogar-web$ dropdb -U postgres advogar-web
(advogar-web) keline@keline-Vostro-V131:~/advogar-web$ createdb -U postgres advogar-web
(advogar-web) keline@keline-Vostro-V131:~/advogar-web$ find . | grep migrations 
./contratos/migrations
./contratos/migrations/__init__.py
./contratos/migrations/0001_initial.py
./contratos/migrations/0002_contrato_ativo.py
./accounts/migrations
./accounts/migrations/__init__.py
./produtos/migrations
./produtos/migrations/__init__.py
./produtos/migrations/0001_initial.py
./clientes/migrations
./clientes/migrations/0003_cliente_produtos.py
./clientes/migrations/__init__.py
./clientes/migrations/0002_remove_cliente_endereco_cobranca.py
./clientes/migrations/0001_initial.py
./publicacoes/migrations
./publicacoes/migrations/__init__.py
./financeiro/migrations
./financeiro/migrations/__init__.py
(advogar-web) keline@keline-Vostro-V131:~/advogar-web$ find . | grep migrations | grep 00 
./contratos/migrations/0001_initial.py
./contratos/migrations/0002_contrato_ativo.py
./produtos/migrations/0001_initial.py
./clientes/migrations/0003_cliente_produtos.py
./clientes/migrations/0002_remove_cliente_endereco_cobranca.py
./clientes/migrations/0001_initial.py
(advogar-web) keline@keline-Vostro-V131:~/advogar-web$ rm $(find . | grep migrations | grep 00)
(advogar-web) keline@keline-Vostro-V131:~/advogar-web$ 
