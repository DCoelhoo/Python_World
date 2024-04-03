short_messages = ["Bom dia", "Boa tarde", "Boa noite", "Tudo bem?", "Adeus"]

def show_messages(messages):
    ''' Return nas mensagens que se encontram dentro da lista.'''

    for message in messages:
        print(message)


show_messages(short_messages)

print("\n ------------ \n")

def send_messages(messages, sent_messages):
    '''Envia as mensagens e altera as mesmas para outra lista'''

    while messages:
        sending_message = messages.pop()
        print(f"A enviar '{sending_message}'")
        sent_messages.append(sending_message)
        print("Mensagem enviada.")

def show_sent(messages):
    ''' Mostra a lista das mensagens enviadas'''

    for message in messages:
        print(f"Mensagens enviadas: {message}")


short_messages2 = ["Bom dia", "Boa tarde", "Boa noite"]
sent_messages = []

send_messages(short_messages2, sent_messages)

print(short_messages2)

show_sent(sent_messages)