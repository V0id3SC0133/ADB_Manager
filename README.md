# ADB Manager

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
   git clone https://github.com/ESC0133/adb-manager.git
   cd adb-manager
   ```

3. Execute o script:

   ```bash
   python3 adb_manager.py
   ```

4. Siga as instruções exibidas no menu interativo.

![image](https://github.com/user-attachments/assets/a018a982-d9f3-45d7-bf81-4abc1f54e28b)

5. Exemplos de utilização.
   
![image](https://github.com/user-attachments/assets/2985cc9f-5f69-46a6-a977-3bde5a4529c9)

![image](https://github.com/user-attachments/assets/9bc27e97-632f-485e-9fa4-17524734781d)


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

Criado por [ESC0133](https://github.com/ESC0133).
