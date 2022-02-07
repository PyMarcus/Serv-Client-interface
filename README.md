# Serv-Client-interface
Arquitetura básica de cliente e servidor para testar o módulo Argparser


### como executar:<br>
Abra dois terminais:<br>
$ python Basics.py -o IP -p PORT Servidor<br>
No outro:<br>
$ python Basics.py -o IP_servidor -p PORT_Servidor Cliente<br>


<br><br>
PS C:\ python .\Basics.py servidor<br>
('127.0.0.1', 7777)<br>
Listen at 127.0.0.1:7777...<br>
Receiving connection from ('127.0.0.1', 50302)<br>
('127.0.0.1', 50302) said: client: Client connecting at serv...<br>
Client socket, ('127.0.0.1', 50302) has closed!<br>
Receiving connection from ('127.0.0.1', 50303)<br>
('127.0.0.1', 50303) said: client: Client connecting at serv...<br>
Client socket, ('127.0.0.1', 50303) has closed!<br>














### obs:<br>
futuras melhorias como transformar em deamon etc...
