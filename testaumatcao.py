import pyautogui as pa
import time

pa.PAUSE = 0.3

while True:
    # Ask for MICRO number FIRST
    numero = input("Digite a numeração para o MICRO (ex: 171, ou 'sair' para parar): ")
    if numero.lower() == 'sair':
        print("Script finalizado.")
        break
    nome_pc = f"MICRO{numero}"
    print(f"Nome do PC definido: {nome_pc}")

    print("Abrindo Propriedades do Sistema...")
    pa.hotkey('win', 'r')
    pa.write('sysdm.cpl')
    pa.press('enter')
    time.sleep(1)

    print("Navegando para aba Alterações/Domínio...")
    pa.press('tab', presses=2)
    pa.press('enter')
    time.sleep(2)

    print("Preenchendo campos (Nome MICRO{numero}, Domínio Japi.local)...")
    # Nome do Computador
    pa.press('delete')
    pa.write(nome_pc)
    # Domínio Japi.local
    pa.press('tab', presses=3)
    pa.press('delete')
    pa.write('Japi.local')
    pa.press('tab')
    pa.press('ENTER')  # Até OK
    pa.hotkey('Alt', 'tab')
    pa.press('Enter')

    print("\n🚨 PAUSADO - CLIQUE OK manual + confirme UAC/reboot!")
    confirma = input("ENTER após finalizar confirmações (ou 'sair'): ")
    if confirma.lower() == 'sair':
        print("Script finalizado.")
        break
    print("✅ Ciclo completo! Reiniciando...")

print("Obrigado por usar a automação MICRO/Japi.local!")
