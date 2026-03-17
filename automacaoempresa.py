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

nome_pc = "MICRO171"
print("Nome do PC definido: MICRO171")

print("Preenchendo campos...")
# Primeiro selecionar rádio Domínio (ativa campo nome)
pa.press('tab')  # Para rádio Member of
pa.press('space')  # Alterna radios se necessário
time.sleep(0.5)
pa.press('tab')  # Para sub-radio Domain
pa.press('space')  # Seleciona Domain
time.sleep(0.5)
pa.press('tab')  # Para campo Domínio
pa.hotkey('ctrl', 'a')
pa.press('delete')
pa.write('Japi.local')
time.sleep(0.5)

# Agora campo Nome do Computador ativado, tab pra ele
pa.press('shift+tab')  # Volta pro Nome do Computador
pa.hotkey('ctrl', 'a')
pa.press('delete')
pa.write(nome_pc)

# Tab para OK e confirmar
pa.press('tab')
pa.press('enter')
time.sleep(1)

# Possível prompt de confirmação/UAC
print("Confirmando alterações (pressione OK se aparecer UAC)...")
time.sleep(3)  # Tempo para usuário confirmar UAC/reboot prompt
