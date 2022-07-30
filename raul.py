from datetime import datetime
from pytz import timezone

dia_semana = ("segunda", "terça", "quarta", "quinta", "sexta", "sabado", "domingo")

RAUL_QUARTO = "O Raul está no quarto vendo vídeos ou no Jiu-Jitsu"
RAUL_DORMINDO = "O Raul está dormindo"
RAUL_ALMOCANDO = "O Raul provavelmente está almoçando ou se preparando"
RAUL_ESTUDANDO = "O Raul está na escola"
RAUL_JOGANDO = "O Raul provavelmente está jogando video game"
RAUL_MORGANDO = "O Raul está Morgando..."


def onde_esta_raul():
    # faz a localização para o fuso de sampa
    brazil = timezone('America/Sao_Paulo')

    #pega o dia e a hora atual
    hoje = datetime.now(brazil).weekday()
    hora = datetime.now(brazil).hour
    minutos = datetime.now(brazil).minute


    # faz o sabado e domingo
    if 5 <= hoje <= 6:
        speak_output = "Hoje é " + dia_semana[hoje] + ". " + RAUL_JOGANDO

    else:
        speak_output = "Hoje é " + dia_semana[hoje] + " feira " + str(hora) + " horas e " + str(minutos) + " minutos. "

    # faz a sexta feira
    if hoje == 4:
        speak_output = speak_output + sexta_feira(hora)

    # segunda a quinta
    if 0 <= hoje <= 3:
        speak_output = speak_output + rotina_diaria(hora)

    if is_morgando(hoje, hora):
        speak_output = RAUL_MORGANDO

    return speak_output


def seg_quinta(dia):
    if 0 <= dia <= 3:
        return True

    return False


# resolve a rotina diária do Raul des segunda a quinta baseada nos horários.
def rotina_diaria(hora):
    if 0 <= hora < 2:
        return RAUL_QUARTO
    if 2 <= hora < 11:
        return RAUL_DORMINDO
    if 11 <= hora < 13:
        return RAUL_ALMOCANDO
    if 13 <= hora < 18:
        return RAUL_ESTUDANDO

    return RAUL_QUARTO


# retorna a rotina do Raul na sexta feira
def sexta_feira(hora):
    if hora >= 18:
        return RAUL_JOGANDO

    return rotina_diaria(hora)


def is_morgando(dia, hora):
    if dia == 0 and 9 <= hora < 11:
        return True

    return False
