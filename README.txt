README

Esse é meu trabalho de conclusão do curso de 135h de Python.

...

Esse sistema foi feito utilizando a linguagem Python em conjunto da ferramenta Flask. Foram utilizados ainda os recursos HTML e CSS para templates e static, afim de estrutrar e aplicar algum design nas páginas da aplicação. O banco de dados foi montado e editado com sqlite3.


obs. é necesário gerar as tabelas do arquivo banco.py e um novo usuário no cadastro sempre que a aplicação for aberta no VScode


O aplicativo propõe de maneira simples o funcionamento de 3 páginas:


1 - Cadastro

é cadastrado um usuário padrão. Esse é armazenado no banco com email, usuario e senha, esses dados são utilizados para validar o login e acessar a lista de bicicletas disponíveis no banco.

2 - página de login:

.Acesso Padrão

Com o usuário e senha cadastrados no processo anterior, basta efetuar o login para acessar as bikes disponíveis, quando feito o aluguel é gerada uma senha para desbloqueio e uma mensagem de aluguel realizado! - com o estoque zerado não é possível alugar, e deixei sessionado o acesso, de modo que é possível alugar apenas uma bicicleta por login.


.Acesso Admin

já foi configurado um acesso separado para administrador, com user : admin e senha : admin: 123. Esse login da acesso ao conteudo do banco, onde é possível aumentar e diminuir o estoque, cadastrar e excluir bikes de acordo com o código id de cada uma.


3 - Edição do banco de dados Bikes.db

Essa rota foi configurada para editar os produtos que estão no banco, bem como para excluí - los de maneira externa. Com o acesso do admin, é possível realizar essas manutenções. 