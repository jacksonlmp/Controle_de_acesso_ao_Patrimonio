# Controle_de_acesso_ao_Patrimonio

O controle de acesso ao patrimônio da UAG/UFRPE, tais como chaves de laboratórios e projetores, é registrado em papel. Assim, é possível ter o registro sobre qual professor está com um determinado patrimônio em um determinado momento. Embora funcional, esse modelo manual impede uma análise mais completa e robusta dos dados sobre a utilização do patrimônio da UAG/UFRPE. Sendo assim, você foi convidado para escrever um programa em linguagem Python que deverá implementar as seguintes funcionalidades:

Armazenar um cadastro persistente de todo o patrimônio da UAG/UFRPE no arquivo de texto “patrimonio.txt”. O arquivo deverá conter as seguintes informações: a. Descrição do patrimônio b. Número do patrimônio

Armazenar o cadastro persiste dos professores da UAG/UFRPE no arquivo de texto “professores.txt”. O arquivo deverá conter as seguintes informações: a. Nome do professor b. Chave de acesso criptografada c. Matrícula

Armazenar o cadastro persistente do acesso ao patrimônio da UAG/UFRPE no arquivo de texto “acesso.txt”. O arquivo deverá conter as seguintes informações: a. Matrícula do professor b. Número do patrimônio c. Tipo de acesso: recebimento ou devolução d. Data do acesso (DD/MM/AAAA) e. Hora do acesso (HH:MM)

Além das funcionalidades básicas para cadastrar um novo patrimônio e um novo professor; o programa deverá permitir:

O registro de um novo recebimento/retirada do patrimônio mediante uso de senha pessoal do professor;
Listagem dos patrimônios aguardando devolução. Deve-se imprimir na tela a matrícula e o nome do professor responsável;
Listagem dos patrimônios disponíveis para retirada;
Listagem dos professores que ficaram com o patrimônio por mais de X horas nos últimos Y dias;
Listagem dos patrimônios mais utilizados nos últimos Y dias; Seu programa deverá exibir menus de opções para o usuário, permitindo que o mesmo navegue entre todas as opções disponíveis.
