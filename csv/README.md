# work-at-lucrorural-dev
Apply for a job at LucroRural Development Team

[Lucro Rural](https://lucrorural.com.br/) é uma plataforma que atua em três grandes áreas: Comercial, Financeiro e Tributário para gerar mais lucro para pequenos e médios Produtores Rurais de todo o Brasil além de revolucionar a integração dos Produtores Rurais com o Escritório de Contabilidade Agro :seedling::ear_of_rice:

A equipe de desenvolvimento da Lucro Rural tem um [guia (leia!)](https://github.com/lucrorural/guia-da-engenharia) com boas práticas para desenvolver a equipe e a qualidade de software.

Estamos sempre à procura de pessoas engajadas no nosso propósito e damos preferência a pequenas equipes com profissionais qualificados em detrimento de grandes equipes com profissionais médios.

Este repositório contém um problema usado para avaliar as habilidades dos candidatos. Observe que a resolução do problema é apenas uma parte do que será avaliado, levaremos em conta as melhores práticas de codificação, a documentação e os testes.


## Como participar

* Crie um repositório público no Github, se você não puder criar um repositório público, crie um privado, e dê acesso de leitura para: [lucrorural-dev](https://github.com/lucrorural-dev).

* Siga as instruções da seção `Especificação` dessa página no desenvolvimento do desafio.

* Hospede sua aplicação em um serviço na nuvem.

* Verifique as recomendações ao final desta página.

* Se candidate a uma das vagas disponíveis no Linkedin (https://www.linkedin.com/company/lucrorural/jobs/) e inclua o seu Linkedin, o link do repositório e o link da aplicação disponível na nuvem.


## Especificação

* Utilize os dois arquivos CSV desse repositório com dados de Fornecedores e Notas Fiscais para Importar para o banco de dados.

* Construa o modelo do `Fornecedor` com os campos que vierem do CSV:
    ```
    id (type uuid)
    nome do fornecedor (type string)
    cnpj (type numerico)
    telefone (type string)
    ```

* E o modelo da `Nota Fiscal` com os campos que vierem do CSV:
    ```
    id (type uuid) auto-gerado
    numero da nota (type int)
    fornecedor (fk com fornecedor)
    data de emissao da nota (type date)
    nome do produto (type string)
    categoria do produto (type string)
    quantidade (type decimal com 2 casas decimais)
    valor total (type decimal com 2 casas decimais)
    ```

* Importação de dados

    * Se você utilizar o framework Django, você pode fazer algo nesse sentido:
        ```
        python manage.py import_fornecedor fornecedor.csv
        python manage.py import_notafiscal notafiscal.csv
        ```
    * Obs.: Não esqueça de ofuscar o conteúdo do campo `telefone` do fornecedor ao gravar no banco de dados.
    * Obs 2: Faça um algoritmo ou utilize uma biblioteca que faça a criptografia para gravar o campo no banco de dados e descriptografe ao mostrar o conteúdo para o usuário.


* Crie o cadastro de Contas a Pagar
    * Ter as opções de criar, editar e excluir

    * O cadastro deve conter os campos:
        ```
        id (type uuid) auto-gerado
        fornecedor (fk do fornecedor)
        data de vencimento (type date)
        pago (type boolean)
        ids de notas fiscais (deve ser possível associar várias notas fiscais a uma conta a pagar)
        ```

    * Para criar a conta a pagar você terá algo como o json abaixo:
        ```
        {
            "fornecedor": "2feb560c-e52c-4e56-ad33-7f5c05817bea",
            "data_vencimento": "2022-01-01",
            "pago": false,
            "notas_fiscais": [
                "c19075d2-a744-476d-b155-bc31e1f8efde",
                "2b2a5bfe-eee9-4051-9012-d570b22c0f03",
                "ac9e47b3-3f1b-4bcb-a2a5-78c2effca1bc"
            ]
        }
        ```


    * Regras de negócio obrigatórias no Backend:
        * Ofuscar o conteúdo do campo `Telefone` do Fornecedor no banco de dados durante a importação do CSV.
        * Vincular as Notas Fiscais a uma Conta a Pagar desde que sejam do mesmo Fornecedor.
        * Não permitir excluir Contas a Pagar se houver Nota Fiscal vinculada.


* Os dados para listar as contas a pagar são:
    * Nome do Fornecedor
    * CNPJ do Fornecedor com a máscara (ex: 00.000.000/0000-00)
    * Telefone (com a informação não ofuscada)
    * Data de Vencimento
    * Pago (sim ou não)
    * Valor Total das Notas Fiscais

    * Filtrar por um dos campos abaixo (os filtros são opcionais):
        * Data de vencimento inicial e final
        * Nome do Fornecedor


## Requisitos:

* Construa o projeto em Python e React.
* Escolha o framework que se sentir mais confortável em desenvolver (Em Python: Django/DRF, Flask, FastAPI e em React: Next.js, ChakraUI, Ant Design, Material-UI, etc.)
* Bibliotecas de terceiros são aceitas.
* Utilize banco de dados Postgres.
* Construa o projeto com base em uma API REST.
* Hospede sua aplicação em um serviço na nuvem, por exemplo, [Heroku](https://www.heroku.com/), [DigitalOcean](https://www.digitalocean.com/), [AWS](https://aws.amazon.com/pt/), [Google Cloud](https://cloud.google.com/), [Azure](https://azure.microsoft.com/pt-br/), etc.


## Recomendações

* Leia atentamente a especificação para entender todo o problema, caso não entenda algo nos avise.
* Valorizamos a simplicidade, então crie uma boa configuração de projeto que nos ajude na sua avaliação.
* Escreva uma boa documentação e faça testes.
* Use boas práticas de programação como Clean Code, SOLID, Design Patterns.
* Escreva mensagens claras e objetivas no [git](https://www.git-tower.com/learn/git/ebook/en/command-line/appendix/best-practices).
* Se estiver confortável escreva em Inglês mas pode escrever em português também (isso não influenciará na sua avaliação).
* Utilize o máximo do conceito do [12 Factor-App](http://12factor.net).
* Tenha esmero com o seu projeto.

**Happy coding and go ahead! :rocket:**
