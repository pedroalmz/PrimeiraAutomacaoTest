import pyautogui as pa
import time
import pyperclip
pa.PAUSE = 0.3

print("Abrindo Propriedades do Sistema...")
pa.hotkey('win', 'r')
pa.write('sysdm.cpl')
pa.press('ENTER')
time.sleep(1)

print("Navegando para Alterar Nome...")
pa.press('tab')
pa.press('tab')
pa.press('enter')
time.sleep(2)

numero = input("Qual o número desejado para o MICRO? ")
nome_pc = f"MICRO{numero}"
print(f"Nome do PC definido: {nome_pc}")

print("Preenchendo campos...")
# Foco no campo Nome do Computador (geralmente primeiro editable após dialog abrir)
pa.press('tab')  # Navega para Nome do Computador se necessário
time.sleep(0.5)
pa.hotkey('ctrl', 'a')  # Seleciona tudo
pa.press('delete')
pa.write(nome_pc)

# Tab para Domínio
pa.press('tab')
time.sleep(0.5)
pa.hotkey('ctrl', 'a')
pa.press('delete')
pa.write('Japi.local')

# Tab para OK e confirmar
pa.press('tab')
pa.press('enter')
time.sleep(1)

# Possível prompt de confirmação/UAC
print("Confirmando alterações (pressione OK se aparecer UAC)...")
time.sleep(3)  # Tempo para usuário confirmar UAC/reboot prompt
