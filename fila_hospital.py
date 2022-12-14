import random

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Hospital:
    def __init__(self):
        self.consultaAtual = None
        self.timeRemaining = 0

    def tick(self):
        if self.consultaAtual != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.consultaAtual = None

    def ocupado(self):
        if self.consultaAtual != None:
            return True
        else:
            return False

    def começarProximaConsulta(self,novaconsulta):
        self.consultaAtual = novaconsulta
        self.timeRemaining = novaconsulta.getDuracao()


class Consulta:
    def __init__(self,time):
        self.timestamp = time
        self.duracaoconsulta = random.randrange(10,21)

    def getStamp(self):
        return self.timestamp

    def getDuracao(self):
        return self.duracaoconsulta

    def waitTime(self, currenttime, pausa):
        if pausa == True:
            return currenttime - self.timestamp + 15   
        else:
            return currenttime - self.timestamp






def simulation(numMinutes):

    atendimentohospital = Hospital()
    filaAtendimento = Queue()
    temposdeespera = []
    medicoPausa = False

    for currentMinute in range(numMinutes): #vai de minuto em minuto até chegar em 720
        if currentMinute%120     == 0:
            medicoPausa = True

        if novoPaciente():  #vê se tem consulta a ser criada nesse minuto
         consulta = Consulta(currentMinute) #cria uma consulta com timestamp no minuto atual
         filaAtendimento.enqueue(consulta) #coloca a consulta na ultima posiçao da fila filaAtendimento

        if (not atendimentohospital.ocupado()) and (not filaAtendimento.isEmpty()): #vê se o consultório tá ocupada (se o timeremaining da ultima consulta chegou a 0) ou se a fila acabou
            proximaconsulta = filaAtendimento.dequeue()  #auxiliar proximoatendimento recebe a consulta do inicio da fila de espera
            temposdeespera.append(proximaconsulta.waitTime(currentMinute,medicoPausa)) #vetor da simulação recebe o tempo esperado pelo paciente
            atendimentohospital.começarProximaConsulta(proximaconsulta) #define o tempo restante para termino da consulta
            medicoPausa = False
        atendimentohospital.tick() #diminui o tempo restante para concluir a consulta atual, se chegar a 0, ocupado fica false
#o tick diminui em um no tempo que falta para concluir a consulta, e ocorre a cada iteração de currentMinute, que é o tempo cronologico.

    mediaEspera=sum(temposdeespera)/len(temposdeespera)
    print("Tempo de espera médio: %6.2f min | %3d consultas remanescentes."%(mediaEspera,filaAtendimento.size()))




def novoPaciente():
    num = random.randrange(1,13)
    if num == 12:
        return True
    else:
        return False



for i in range(10): #10 simulações de 720 minutos (12 hora)
    simulation(720) #10 é o numero de paginas impressas por minuto