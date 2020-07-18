_ = int(input())

femaleParticipants = input()
maleParticipants = input()

numberOfRum = maleParticipants.count('r')
numberOfMojito = maleParticipants.count('m')

femaleParticipantsArray = list(femaleParticipants)

def handleParticipant():
    for femaleParticipant in femaleParticipants:
        if femaleParticipant == 'r':
            if numberOfRum == 0:
                print(len(femaleParticipantsArray), end= '')
                break
            numberOfRum -= 1
            femaleParticipantsArray.pop(0)

        elif femaleParticipant == 'm':
            if numberOfMojito == 0:
                print(len(femaleParticipantsArray), end = '')
                break
            numberOfMojito -= 1
            femaleParticipantsArray.pop(0)
    else:
        print(0, end='')

handleParticipant()