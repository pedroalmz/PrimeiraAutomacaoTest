import pyautogui as pa
import time

pa.PAUSE = 0.3

# Ask for MICRO number FIRST
numero = input("Digite a numeração para o MICRO (ex: 171): ")
nome_pc = f"MICRO{numero}"
print(f"Nome do PC definido: {nome_pc}")

print("Abrindo Propriedades do Sistema...")
pa.hotkey('win', 'r')
pa.write('sysdm.cpl')
pa.press('enter')
time.sleep(1)

print("Navegando para aba Alterações/Domínio...")
pa.press('tab')
pa.press('tab')
pa.press('enter')
time.sleep(2)

print("Preenchendo campos (Domínio Japi.local fixo, Nome MICRO{numero})...")
# Assume focus starts near top; tab to Membro de / Domínio field (~3 tabs)
pa.press('tab', presses=3)
pa.hotkey('ctrl', 'a')
pa.press('delete')
pa.write('Japi.local')
time.sleep(0.5)

# Shift-tab back to Nome do Computador (usually adjacent)
pa.press('shift+tab')
pa.hotkey('ctrl', 'a')
pa.press('delete')
pa.write(nome_pc)

# Tab to OK button(s)
pa.press('tab', presses=2)
pa.press('enter')
time.sleep(1)

print("Confirmando alterações (pressione OK se UAC/reboot prompt aparecer)...")
time.sleep(3)
