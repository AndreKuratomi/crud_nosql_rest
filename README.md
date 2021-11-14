CRUD NoSQL Rest!

Você irá desenvolver uma API REST que realiza operações CRUD para publicações de um blog. No final sua API deve ser capaz de:

Registrar uma nova publicação;

Ler uma publicação específica ou todas de uma só vez;

Atualizar uma publicação;

Deletar uma publicação.

(Caso trave em alguma etapa do projeto, mude para algo que tenha mais clareza de como fazer, para retomar a produtividade e recuperar a confiança, acontece com todos.)

Requisitos:

Aplicação organizada em arquitetura MVC;

Utilizar o padrão de projeto Factory;

CLASSE!

Uma model (classe) chamada Post que armazena as seguintes informações:

Um id único para cada post, que inicia em 1 e incrementa automaticamente após a inserção de um novo post;

created_at (um objeto de data que representa o momento da criação do post). Consultar a documentação do pymongo para verificar como salvar uma data;

updated_at (um objeto de data que representa o momento da última atualização do post);

title (titulo do post);

author (nome do autor do post);

tags (lista de strings que representam tags do post). As tags podem ser qualquer string;

content (texto da publicação).

ROTAS!

Rota para criar um novo post, passando as informações necessárias;

Rota para obter todos os posts;

Rota para obter um post específico pelo id (passado via url conforme o padrão rest);

Rota para alterar um post;

Rota para deletar um post;

Seguir o máximo possível as restrições do padrão REST;

ERROS!

Tratar os seguintes erros:
Dados para criação do post inválidos. (Dados faltando, chaves erradas, etc.);
Dados para alteração do post inválidos. (Chaves erradas, etc.);
Post que não existe tentando ser obtido, excluído ou editado.

Regras e observações:

O nome do db deve ser kenzie e o nome da collection posts;

Analise e implemente a classe usando os métodos com os decorators que mais fizerem sentido. (métodos estáticos, de instância e de classe). Utilize também os métodos especiais quando necessário;

Manter as boas práticas no repositório (requirements.txt, gitignore, .env de exemplo, readme).
