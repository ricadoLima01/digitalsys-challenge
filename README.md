# 📋 Documentação sobre a API

- 🛠️ Implementar uma API ou interface em Django para gerenciar os currículos.

1.**📦 Models**:

    - 👤**Dados Pessoais**: `id`, `nome`, `data de nascimento`.

    - 📞**Contato**: `id`, `email`, `telefone`, `endereço`.

    - 💼**Experiência Profissional**: `dadosPessoaisKey`, `ContatoKey`, `id` (cargo, empresa, período, descrição).

    - 🎓**Formação Acadêmica**: `id`, `instituição`, `curso`, `período`.

    - 📑**Currículo**: `id`, `DadosPessoais`, `Contato`, `ExperiênciaProfissional`, `FormaçãoAcadêmica`, `generatePDF`.

2.**Controllers**:

    - 👤**Dados Pessoais**:

    ```json

    {

    "id": 1,

    "nome": "João Silva",

    "data_de_nascimento": "1990-01-01"

    }

    ```

    - 📞

    -
