Aqui estão os passos gerais para instalar a cadeia de certificados de um site específico (como o https://safeweb.com.br/repositorio) em um sistema Debian:

Baixe a cadeia de certificados do site. Isso geralmente pode ser feito baixando o arquivo de cadeia de certificados no formato .crt ou .pem

Copie o arquivo de cadeia de certificados para a pasta /usr/local/share/ca-certificates/ no sistema Debian. Esse é o local padrão onde os certificados de confiança são armazenados no Debian.

Atualize o sistema de certificados do sistema operacional. Isso pode ser feito com o comando:

Copy code
sudo update-ca-certificates
Verifique se o certificado foi instalado corretamente. Isso pode ser feito usando o comando:
Copy code
sudo update-ca-certificates --dry-run
Reinicie o serviço da sua aplicação que usa SSL/TLS para carregar as novas cadeias de certificados.
Isso é tudo. Agora, o seu sistema deve confiar no certificado fornecido pelo site e você não deve mais ver mensagens de aviso de certificado inválido ao acessar esse site.