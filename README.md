Atividade da Disciplina Tecnicas de programação do Curso de Licenciatura em Computação.
-
Problema fictício
-
O IFPI Zona Sul deseja implementar uma cobrança simbólica de R$ 2,00 para que seus servidores tenham acesso ao refeitório. Para isso, o diretor solicitou aos alunos do curso de Computação que desenvolvessem um sistema para realizar esse controle.

Após uma reunião, ficou definido que o sistema funcionará de forma semelhante a uma conta bancária, permitindo que o servidor:

• Cadastre-se no sistema;

• Adicione créditos;

• Consulte o saldo;

• Acesse o refeitório (com desconto automático de R$ 2,00);

• Liste todos os servidores cadastrados.

Funcionalidades do Sistema
-
**Cadastrar usuário**
- O sistema solicita o nome do servidor. Ao informar o nome, ele é adicionado à lista nomes e, simultaneamente, também é criado um elemento na lista contas com saldo inicial de R$ 0,00.

**Listar usuários**
- Exibe todos os nomes cadastrados na lista nomes.

**Adicionar crédito**
- O sistema solicita o código do servidor e o valor a ser creditado. O valor informado é somado ao saldo existente na conta correspondente. Ou seja, na lista contas o valor informado é incrementado ao código(indice).

**Verificar saldo**
- O sistema solicita o código do servidor e exibe o saldo atual da conta vinculada a esse código. Ou seja, o sistema exibe o valor que exite na lista contas no código informado

**Acessar refeitório**
- O sistema solicita o código do servidor e verifica se o saldo é maior ou igual a R$ 2,00. Ou seja, se no indice da lista contas o valor é maior ou igual à R$ 2.00

- Se houver saldo suficiente, o sistema desconta R$ 2,00 e exibe a mensagem "Acesso liberado".

- Caso contrário, exibe a mensagem "Acesso negado".