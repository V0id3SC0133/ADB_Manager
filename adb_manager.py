import subprocess
import os

def run_command(command, silent=False):
    """Executa um comando no shell e retorna a saída."""
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            if not silent:
                print(f"Erro ao executar o comando: {result.stderr.strip()}")
            return None
    except Exception as e:
        print(f"Erro ao executar o comando '{command}': {e}")
        return None


def print_and_run(command, success_message, failure_message=None):
    """Executa um comando e exibe mensagens de sucesso ou falha."""
    result = run_command(command)
    if result is not None:
        print(success_message)
    elif failure_message:
        print(failure_message)


def check_adb_connection():
    print("\nVerificando conexão com dispositivo ou emulador...")
    devices = run_command("adb devices")
    print(devices if devices else "Nenhum dispositivo conectado.")


def identify_avd_type():
    print("\nIdentificando o tipo de AVD ou arquitetura do processador...")
    abi = run_command("adb shell getprop ro.product.cpu.abi")
    print(f"Arquitetura: {abi}" if abi else "Não foi possível identificar a arquitetura.")


def config_proxy():
    proxy_host = input("Digite o host do proxy (ex: 127.0.0.1): ").strip()
    proxy_port = input("Digite a porta do proxy (ex: 8080): ").strip()

    print("\nConfigurando proxy usando adb...")
    run_command(f"adb reverse tcp:{proxy_port} tcp:{proxy_port}", silent=True)
    print_and_run(
        f"adb shell settings put global http_proxy {proxy_host}:{proxy_port}",
        "Proxy configurado com sucesso.",
        "Falha ao configurar o proxy."
    )


def delete_proxy():
    print("\nDeletando configurações de proxy...")
    commands = [
        "adb reverse --remove-all",
        "adb shell settings delete global http_proxy",
        "adb shell settings delete global global_http_proxy_host",
        "adb shell settings delete global global_http_proxy_port"
    ]
    for cmd in commands:
        run_command(cmd, silent=True)
    print("Configurações de proxy deletadas com sucesso.")


def extract_apk():
    print("\nListando pacotes do dispositivo...")
    packages = run_command("frida-ps -Uai")
    if not packages:
        print("Nenhum pacote encontrado.")
        return

    print(packages)
    selected_package = input("\nDigite o nome do pacote que deseja extrair o APK (ou deixe em branco para voltar): ").strip()
    if not selected_package:
        return

    apk_path_output = run_command(f"adb shell pm path {selected_package}")
    if apk_path_output:
        apk_path = apk_path_output.split(":")[-1].strip()
        print_and_run(
            f"adb pull {apk_path} {selected_package}.apk",
            "APK extraído com sucesso.",
            "Falha ao extrair o APK."
        )
    else:
        print("Pacote não encontrado ou não acessível.")


def install_apk():
    apk_file = input("\nDigite o caminho completo do arquivo APK a ser instalado: ").strip()
    print_and_run(
        f"adb install -r -d {apk_file}",
        "APK instalado com sucesso.",
        "Falha ao instalar o APK."
    )


def intercept_flutter():
    print("\nInterceptando tráfego Flutter...")
    print("Comandos para interceptação ainda não foram implementados.")


def list_adb_reverse():
    print("\nListando redirecionamentos adb:")
    adb_reverse_list = run_command("adb reverse --list")
    print(adb_reverse_list if adb_reverse_list else "Nenhum redirecionamento encontrado.")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_header():
    print("\n======================================")
    print("    Ferramentas ADB - Menu Principal  ")
    print("======================================")


def main():
    actions = {
        "1": check_adb_connection,
        "2": identify_avd_type,
        "3": config_proxy,
        "4": delete_proxy,
        "5": extract_apk,
        "6": install_apk,
        "7": intercept_flutter,
        "8": list_adb_reverse
    }

    while True:
        clear_screen()
        display_header()

        print("1. Verificar conexão com dispositivo ou emulador")
        print("2. Identificar o AVD ou arquitetura do processador")
        print("3. Configurar proxy usando adb")
        print("4. Deletar configurações de proxy")
        print("5. Extrair um APK")
        print("6. Instalar um APK")
        print("7. Interceptar tráfego Flutter de uma APK")
        print("8. Listar redirecionamentos adb")
        print("9. Sair")

        choice = input("\nEscolha uma opção (1-9): ").strip()

        if choice == "9":
            print("\nSaindo... Até logo!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("\nOpção inválida. Tente novamente.")

        input("\nPressione Enter para continuar...")


if __name__ == "__main__":
    main()
