"""
Create the four suits as instances of a suit class?

Add the numbers 1-13 to a number pool - a card will be 'made' by assigning a suit and a number
    need a card assignment function
    
    need a function that gives the rules for each suit

Is it worth exclduing mirror matchups?

How to handle mutual kills, is that a win? A loss?

Check win % of champion with no supports - separate lists for champion pool and support pool?
    Generate new list of supports after champion has been selected with champion removed
    
    
Overall Program - calculate the win percentage for each card and every combination of supports
                  against every other card and support combination
    Inputs - probably self/none, alternatively could iterate through a list of cards
    Outputs - excel table or panda format table that contains each suit/card combo and its overall win percentage
    
    
    FN - Attacking Champion Designation(suits, numbers), output is Attacker and Supports variables defined
    For each suit in suits:
        for each num in numbers:
            assign that num/suit as the champion
            
            for each num in numbers:
                assign that num as 'attacker attack support'
                
                for each num in numbers:
                    assign that num as 'attacker health support'
                                      
    Once Attacking Champion and supports have been designated, need to iterate
    through same process to produce defending champion possibilities
    
        FN - Defending Champion Designation(suits, numbers)
        For each suit in suits:
            for each num in numbers:
                assign that num/suit as the defending champion
                
                for each num in numbers:
                    assign that num as 'defender attack support'
                    
                    for each num in numbers:
                        assign that num as 'defender health support'

            Once Defending Champion has been assigned, champions fight and fight
            resolution needs to be calculated and recorded
                Seperate functions for fighting and fight result
                    
            FN - Fight resolution(attacker, aas, ahs, defender, das, dhs), output is (attacker killed?, defender killed?)
            
                FN - Increment statistics for that champion
                
                    FN - write statistics to row of panda or excel table/export
                       
            
            
"""
#import pandas as pd


#takes an array of arrays containing atk+supports and def+supports, returns [[atk atk, atk def], [def atk, def]]
#based on suits and powers of the attacker and defender
#       Array Labels
#  [0][0][0]  [0][0][1]        [0][1][0]        [0][1][1]              [0][2][0]        [0][2][1]           [1][0][0]  [1][0][1]        [1][1][0]        [1][1][1]           [1][2][0]          [1][2][1]
#[[[atk suit, atk power],[atk atk supp suit, atk atk supp power],[atk def supp suit, atk def supp power]],[[def suit, def power],[def atk supp suit, def atk supp power],[def def supp suit, def def supp power]]]
#functions returns an array of lists representing the attack and defense of each champion: ([off atk, off def], [def atk, def def])
def calculateatkdefpower(atkdefplussupparray):
    array = atkdefplussupparray
    atkdefarray = []
    
#rules for atk champ            
    
    temparray = []                                
    atk = array[0][0][1]
    tempatk = atk
    dfnse = array[0][0][1]
    tempdef = dfnse
    
    #calculate effect of supports on power
    
    #if atk champ suit matches atk supp suit (club), add base power
    if array[0][0][0] == array[0][1][0]:
        tempatk += atk
    
    #if atk champ suit is diamond it gets an additional base power
    elif array[0][0][0] == 'diamond':
        tempatk += atk
        
    #series of rules for cutting or boosting attack based on type advantage disadvantage
    
    #increase power
    elif array[0][0][0] == 'club' and array[1][0][0] == 'diamond':
        tempatk += atk
    elif array[0][0][0] == 'diamond' and array[1][0][0] == 'heart':
        tempatk += atk
    elif array[0][0][0] == 'heart' and array[1][0][0] == 'spade':
        tempatk += atk
    elif array[0][0][0] == 'spade' and array[1][0][0] == 'club':
        tempatk += atk
    
    #cutting power
    elif array[0][0][0] == 'club' and array[1][0][0] == 'spade':
        tempatk += 1
        tempatk / atkmult
    elif array[0][0][0] == 'spade' and array[1][0][0] == 'heart':
        tempatk += 1
        tempatk / atkmult
    elif array[0][0][0] == 'heart' and array[1][0][0] == 'diamond':
        tempatk += 1
        tempatk / atkmult
    elif array[0][0][0] == 'diamond' and array[1][0][0] == 'club':
        tempatk += 1
        tempatk / atkmult
    
    #finally, add atk value of support, but only up to the value of the champ's power
    
    elif array[0][1][1] > array[0][0][1]:
        tempatk += array[0][0][1]
    else:
        tempatk += array[0][1][1]   
    
    #add calculated atk value to temparray
    temparray.append(tempatk)
    
#calculate health value
    
    #if atk champ suit matches atk supp suit (heart), add base power
    if array[0][0][0] == array[0][2][0]:
        tempdef += dfnse
    
    #add value of health support
    
    elif array[0][2][1] > array[0][0][1]:
        tempdef += array[0][0][1]
    else:
        tempdef += array[0][2][1]   
    
    #add calulated def value to temparray
    temparray.append(tempdef)
    
    #add temparray to atdefarray
    atkdefarray.append(temparray)
    
#############Calculate same values for Def champ############

    temparray = []                                
    atk = array[1][0][1]
    tempatk = atk
    dfnse = array[1][0][1]
    tempdef = dfnse

    #calculate effect of supports on power
    
    #if atk champ suit matches atk supp suit (club), add base power
    if array[1][0][0] == array[1][1][0]:
        tempatk += atk
    
    #if atk champ suit is diamond it gets an additional base power
    elif array[1][0][0] == 'diamond':
        tempatk += atk
        
    #series of rules for cutting or boosting attack based on type advantage disadvantage
    
    #increase power
    elif array[0][0][0] == 'club' and array[1][0][0] == 'diamond':
        tempatk += 1
        tempatk / atkmult
    elif array[0][0][0] == 'diamond' and array[1][0][0] == 'heart':
        tempatk += 1
        tempatk / atkmult
    elif array[0][0][0] == 'heart' and array[1][0][0] == 'spade':
        tempatk += 1
        tempatk / atkmult
    elif array[0][0][0] == 'spade' and array[1][0][0] == 'club':
        tempatk += 1
        tempatk / atkmult
    
    #cutting power
    elif array[0][0][0] == 'club' and array[1][0][0] == 'spade':
        tempatk += atk
    elif array[0][0][0] == 'spade' and array[1][0][0] == 'heart':
        tempatk += atk
    elif array[0][0][0] == 'heart' and array[1][0][0] == 'diamond':
        tempatk += atk
    elif array[0][0][0] == 'diamond' and array[1][0][0] == 'club':
        tempatk += atk
        
    
    #finally, add atk value of support, but only up to the value of the champ's power
    
    elif array[1][1][1] > array[1][0][1]:
        tempatk += array[1][0][1]
    else:
        tempatk += array[1][1][1]   
    
    #add calculated atk value to temparray
    temparray.append(tempatk)
    
#calculate health value
    
    #if atk champ suit matches atk supp suit (heart), add base power
    if array[1][0][0] == array[1][2][0]:
        tempdef += dfnse
    
    #add value of health support
    
    elif array[1][2][1] > array[1][0][1]:
        tempdef += array[1][0][1]
    else:
        tempdef += array[1][2][1]   
    
    #add calulated def value to temparray
    temparray.append(tempdef)
    
    #add temparray to atdefarray
    atkdefarray.append(temparray)
    
    #print atkdefarray
    return atkdefarray



def buildchamppool(suits, powers):
    champpool = []
    
    for suit in suits:
        for power in powers:
            champpool.append([suit,power])
    
    #print champpool
    return champpool
    
    
#builds a pool of champ possibilities that excludes the atk champ
def builddefenderpool(atksuppcombo, champpool):
    defenderpool = champpool[:]
    
    for x in champpool:
        if x in atksuppcombo:
            defenderpool.remove(x)
                
    return defenderpool
    
    
    
#this function generates atksupport and defsupport pools that wont contain champ 
def buildatkchampsupportpools(champ, atksuppsuits, defsuppsuits, powers):  
    atksupppool = [['empty', 0]]
    defsupppool = [['empty', 0]]
    
    for suit in atksuppsuits:
        for power in powers:
            tempatkcombo = [suit, power]
            if tempatkcombo != champ:
                atksupppool.append(tempatkcombo)
        
    for suit in defsuppsuits:
        for power in powers:
            tempdefcombo = [suit, power]
            if tempdefcombo != champ:
                defsupppool.append(tempdefcombo)
                
    return atksupppool, defsupppool
    
    

def createdefchampplussupportpool(defenderpool, atksuppcombo):   
    
    alldefsuppcombos = []
    
    for x in defenderpool:
        #print x
        supppools = buildatkchampsupportpools(x, atksuits, defsuits, powers)
        
        for atkchamp in supppools[0]:
            if atkchamp in atksuppcombo and atkchamp != ['empty', 0]:
                supppools[0].remove(atkchamp)
            
        for defchamp in supppools[1]:
            if defchamp in atksuppcombo and defchamp != ['empty', 0]:
                supppools[1].remove(defchamp)

        for atkchamp in supppools[0]:
            for defchamp in supppools[1]:
                alldefsuppcombos.append([x, atkchamp, defchamp])        
        
    #print alldefsuppcombos
    return alldefsuppcombos


#use this function to create full attacker and defender champ/support pools
def addsupports(champ, buildsupportpoolsoutput):
    champsuppcombos = []
    
    
    for x in buildsupportpoolsoutput[0]:
        for y in buildsupportpoolsoutput[1]:
            champsuppcombos.append([champ, x, y])
       
    #print champsuppcombos
    return champsuppcombos

    
#use this function to create a pool that is arrays of atk champion plus supports and def champ plus supports
def createatkdefchampplussupportspool(atkplussupppool, defplussupppool):
    
    finalpool = []
    
    for x in atkplussupppool:

        for y in defplussupppool:
            
            finalpool.append([x, y])
        
    #print finalpool
    return finalpool


def resolveconflict(atkdefarray):
    atkatk = atkdefarray[0][0]
    atkdef = atkdefarray[0][1]
    defatk = atkdefarray[1][0]
    defdef = atkdefarray[1][1]
    atkdie = None
    defdie = None
    resolved = False
    i = 0
    
    while resolved == False and i < 20:
        i += 1
        
        if (i * atkatk) >= defdef and (i * defatk) >= atkdef:
            atkdie = True
            defdie = True
            resolved = True
        
        elif (i * atkatk) >= defdef and (i * defatk) < atkdef:
            atkdie = False
            defdie = True
            resolved = True
        
        elif (i * atkatk) < defdef and (i * defatk) >= atkdef:
            atkdie = True
            defdie = False
            resolved = True
    
    """
    if (atkdefarray[0][1] / atkdefarray[1][0]) > (atkdefarray[1][1] / atkdefarray[0][0]) or \
        ((atkdefarray[0][1] / atkdefarray[1][0]) == (atkdefarray[1][1] / atkdefarray[0][0]) and \
        (atkdefarray[0][1] % atkdefarray[1][0]) > (atkdefarray[1][1] % atkdefarray[0][0])):
        atkdie = False
        defdie = True
    
    elif (atkdefarray[0][1] / atkdefarray[1][0]) == (atkdefarray[1][1] / atkdefarray[0][0]):
        atkdie = True
        defdie = True
    
    elif (atkdefarray[0][1] / atkdefarray[1][0]) < (atkdefarray[1][1] / atkdefarray[0][0]) or \
        ((atkdefarray[0][1] / atkdefarray[1][0]) == (atkdefarray[1][1] / atkdefarray[0][0]) and \
        (atkdefarray[0][1] % atkdefarray[1][0]) < (atkdefarray[1][1] % atkdefarray[0][0])):
        atkdie = True
        defdie = False
    """
    
    return (atkdie, defdie)


#need a fn that processes all fighting for each champ in the champ pool and records the result
def buildchampstatsdict(suits, atksuits, defsuits, powers):
    
    champstatsdict = {
                        'Champ': [],
                        'Kill Opponent %': [],
                        'Kill Opponent and Live %': []                   
                        }
    
    champpool = buildchamppool(suits, powers)
    #print champpool
    
    
    for champ in champpool:
        matchups = 0
        atkdiecount = 0
        defdiecount = 0
        bothdiecount = 0
        killandlivecount = 0
        defwincount = 0
        
        supportpools = buildatkchampsupportpools(champ, atksuits, defsuits, powers)
        atkplussupps = addsupports(champ, supportpools)
        print '------------------------------------------'
        print 'atkplussupps'
        print atkplussupps
        
        for atksuppcombo in atkplussupps[:1]:
            
            defenderpool = builddefenderpool(atksuppcombo, champpool)
            defplussupps = createdefchampplussupportpool(defenderpool, atksuppcombo)
            finalpool = createatkdefchampplussupportspool(atkplussupps, defplussupps)
            
            
            print 'atksuppcombo'
            print atksuppcombo
            print 'defenderpool'
            print defenderpool
            print 'defplussupps'
            print defplussupps
            
            #print atksuppcombo
            #print defenderpool
            #print defplussupps
            

            for matchup in finalpool[:2]:
                print 'matchup'
                print matchup
                
                matchups += 1
    
                powerlist = calculateatkdefpower(matchup)
                print powerlist
                
                outcome = resolveconflict(powerlist)
                print outcome
                
                if outcome == (False, True):
                    defdiecount += 1
                    killandlivecount += 1
                
                elif outcome == (True, True):
                    atkdiecount += 1
                    defdiecount += 1
                    bothdiecount += 1
                    
                elif outcome == (True, False):
                    atkdiecount += 1
                    defwincount += 1
        
            
        defdiepercent = float(defdiecount) / float(matchups) * 100.0
        killandlivepercent = float(killandlivecount) / float(matchups) * 100.0
        
        champstatsdict['Champ'].append(champ)
        champstatsdict['Kill Opponent %'].append(defdiepercent)
        champstatsdict['Kill Opponent and Live %'].append(killandlivepercent)
        
    print champstatsdict
    #return champstatsdict

###############################################################
    
#next steps: fix power calculation algorithm


#"""

suits = ['heart', 'club', 'diamond', 'spade']
atksuits = ['club']
defsuits = ['heart']
powers = [1]

#combat multipliers
atkmult = 2
defmult = 2

"""
champ = ['heart', 1]
champpool = buildchamppool(suits, powers)
supportpools = buildatkchampsupportpools(champ, atksuits, defsuits, powers)
atkplussupps = addsupports(champ, supportpools)
atksuppcombo = [['heart', 1], ['empty', 0], ['empty', 0]]

defenderpool = builddefenderpool(atksuppcombo, champpool)
defplussupps = createdefchampplussupportpool(defenderpool, atksuppcombo)

finalpool = createatkdefchampplussupportspool(atkplussupps, defplussupps)
#atkdefarray = calculateatkdefpower(finalpool)    #calcpower fn only works on one array at a time, finalpool is many arrays
"""

array = [[['diamond', 7],['club', 4],['heart', 10]],[['diamond', 7],['club', 4],['heart', 10]]]
#calculateatkdefpower(array)

x = ([1, 2], [3, 4])
y = {
    'key': [1]
        }
        
#buildchampstatsdict(suits, atksuits, defsuits, powers)
a = [[2,3],[2,2]] #False, True
b = [[2,6],[2,2]] #False, True
c = [[2,3],[2,3]] #True, True
d = [[2,4],[2,4]] #True, True
e = [[2,5],[2,7]] #True, False
f = [[6,3],[3,2]] #True, True
g = [[2,8],[3,5]] #True, True
