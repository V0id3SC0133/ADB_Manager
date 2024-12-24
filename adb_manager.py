import subprocess
import os

def run_command(command):
    """Executa um comando no shell e retorna a saída."""
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            print(f"Erro ao executar o comando: {result.stderr.strip()}")
            return None
    except Exception as e:
        print(f"Erro: {e}")
        return None

def check_adb_connection():
    print("\nVerificando conexão com dispositivo usando adb...")
    print(run_command("adb devices"))

def identify_avd_type():
    print("\nIdentificando o tipo de AVD que está rodando...")
    print(run_command("adb shell getprop ro.product.cpu.abi"))

def config_proxy():
    proxy_host = input("Digite o host do proxy (ex: 127.0.0.1): ")
    proxy_port = input("Digite a porta do proxy (ex: 8080): ")

    print("\nConfigurando proxy usando adb...")
    run_command(f"adb reverse tcp:{proxy_port} tcp:{proxy_port}")
    result = run_command(f"adb shell settings put global http_proxy {proxy_host}:{proxy_port}")
    if result is not None:
        print("Proxy configurado com sucesso.")
    else:
        print("Falha ao configurar o proxy.")

def delete_proxy():
    print("\nDeletando configurações de proxy...")
    run_command("adb reverse --remove-all")
    run_command("adb shell settings delete global http_proxy")
    run_command("adb shell settings delete global global_http_proxy_host")
    run_command("adb shell settings delete global global_http_proxy_port")
    print("Configurações de proxy deletadas com sucesso.")

def extract_apk():
    print("\nListando pacotes disponíveis no emulador:")
    packages = run_command("frida-ps -Uai")
    print(packages)

    selected_package = input("\nDigite o nome do pacote que deseja extrair o APK (ou deixe em branco para voltar ao menu): ")
    if not selected_package:
        return

    print(f"\nExtraindo APK do pacote: {selected_package}")
    apk_path_output = run_command(f"adb shell pm path {selected_package}")
    if apk_path_output:
        apk_path = apk_path_output.split(":")[-1].strip()
        run_command(f"adb pull {apk_path} {selected_package}.apk")
        print("APK extraído com sucesso.")

def install_apk():
    apk_file = input("\nDigite o caminho completo do arquivo APK a ser instalado: ")
    run_command(f"adb install -r -d {apk_file}")

def intercept_flutter():
    print("\nInterceptando tráfego Flutter...")
    print("Adicione aqui os comandos para interceptar o tráfego Flutter.")

def list_adb_reverse():
    print("\nListando redirecionamentos adb:")
    print(run_command("adb reverse --list"))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    print("\n======================================")
    print("    Ferramentas ADB - Menu Principal  ")
    print("======================================")

def main():
    while True:
        clear_screen()
        display_header()

        print("1. Verificar conexão com dispositivo usando adb")
        print("2. Identificar tipo de AVD que está rodando")
        print("3. Configurar proxy usando adb")
        print("4. Deletar configurações de proxy")
        print("5. Extrair um APK de um emulador")
        print("6. Instalar um APK")
        print("7. Interceptar tráfego Flutter de uma APK")
        print("8. Listar redirecionamentos adb")
        print("9. Sair")

        choice = input("\nEscolha uma opção (1-9): ")

        if choice == "1":
            check_adb_connection()
        elif choice == "2":
            identify_avd_type()
        elif choice == "3":
            config_proxy()
        elif choice == "4":
            delete_proxy()
        elif choice == "5":
            extract_apk()
        elif choice == "6":
            install_apk()
        elif choice == "7":
            intercept_flutter()
        elif choice == "8":
            list_adb_reverse()
        elif choice == "9":
            print("\nSaindo... Até logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
