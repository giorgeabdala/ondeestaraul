from datetime import datetime
from pytz import timezone

dia_semana = ("segunda", "terça", "quarta", "quinta", "sexta", "sabado", "domingo")

quarto = "O Raul está no quarto vendo vídeos ou no Jiu-Jitsu"
dormindo = "O Raul está dormindo"
almoco = "O Raul provavelmente está almoçando ou se preparando"
escola = "O Raul está na escola"
game = "O Raul provavelmente está jogando video game"
morgando = "O Raul está Morgando..."


def onde_esta_raul():
    # faz a localização para o fuso de sampa
    brazil = timezone('America/Sao_Paulo')

    #pega o dia e a hora atual
    hoje = datetime.now(brazil).weekday()
    hora = datetime.now(brazil).hour()
    minutos = datetime.now(brazil).minute()

    speak_output = "Não sei onde o Raul está..."

    # faz o sabado e domingo
    if final_semana(hoje):
        speak_output = "Hoje é " + dia_semana[hoje] + ". " + game

    else:
        speak_output = "Hoje é " + dia_semana[hoje] + " feira " + str(hora) + " horas e " + str(minutos) + " minutos. "

        # faz a sexta feira
        if hoje == 4:
            speak_output = speak_output + sexta_feira(hora)

        # segunda a quinta
        if 0 <= hoje <= 3:
            speak_output = speak_output + rotina_diaria(hora)

        if is_morgando(hoje, hora):
            speak_output = morgando

    return speak_output


def final_semana(dia):
    if dia == 5 or dia == 6:
        return True

    return False


def seg_quinta(dia):
    if 0 <= dia <= 3:
        return True

    return False


# resolve a rotina diária do Raul des segunda a quinta baseada nos horários.
def rotina_diaria(hora):
    if 0 <= hora < 2:
        return quarto
    elif 2 <= hora < 11:
        return dormindo
    elif 11 <= hora < 13:
        return almoco
    elif 13 <= hora < 18:
        return escola
    elif hora >= 18:
        return quarto


# retorna a rotina do Raul na sexta feira
def sexta_feira(hora):
    if hora >= 18:
        return game
    else:
        return rotina_diaria(hora)


def is_morgando(dia, hr):
    if dia == 0 and 9 <= hr < 11:
        return True

    return False
