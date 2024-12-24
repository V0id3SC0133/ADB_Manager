# ADB_Manager

**Descrição:**

O **ADB Manager** é um script em Python que automatiza tarefas comuns do Android Debug Bridge (ADB), facilitando o trabalho de desenvolvedores e entusiastas ao gerenciar dispositivos Android e emuladores.

## Funcionalidades

- Verificar conexões com dispositivos usando ADB.
- Identificar o tipo de emulador (AVD) em execução.
- Configurar e remover configurações de proxy nos dispositivos.
- Extrair APKs diretamente de emuladores ou dispositivos conectados.
- Instalar APKs em dispositivos de maneira simples.
- Interceptar tráfego de aplicativos Flutter.
- Listar redirecionamentos de porta configurados pelo ADB.

## Como Usar

1. Certifique-se de que o Python 3 está instalado em seu sistema.
2. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/adb-manager.git
   cd adb-manager
   ```

3. Execute o script:

   ```bash
   python3 adb_manager.py
   ```

4. Siga as instruções exibidas no menu interativo.

## Pré-requisitos

- Python 3.6 ou superior.
- Ferramentas ADB instaladas e configuradas no PATH do sistema.
- Dependências adicionais (opcional):
  - [Frida](https://frida.re/) para listar pacotes de aplicativos.

## Estrutura do Código

- **run_command**: Função para executar comandos do sistema.
- **Menu principal**: Navegação interativa para acessar cada funcionalidade.
- **Funções individuais**: Cada opção do menu tem uma função correspondente para realizar a tarefa designada.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias ou correções.

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para mais informações.

## Autor

Criado por [Seu Nome](https://github.com/seu-usuario).
