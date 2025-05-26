texte = "BeeBeeBeeBeeBoomDeepBoomDeepBoomBeeDeepDeepBeeBoomBeeBeeBeeBoomDeepDeepDeepBeeBeeBeeBoomDeepBeeBeeDeepBeeBoomDeepBeeBeeDeepBeeBoomDeepDeepBeeBoomDeepDeepDeepBoomBeeDeepBeeDeepBeeDeepBoomBeeBeeDeepBoomDeepBeeBoomBeeBeeBoomBeeBeeBeeDeepBoomDeepBeeBeeBeeBeeDeepBoomBeeDeepBeeBeeBoomDeepBeeDeepDeepBoomDeepDeepDeepBoomDeepBeeBoomBeeDeepDeepDeepDeepBoomBeeDeepBeeDeepBeeDeepBoomBeeBeeDeepBeeBoomBeeDeepBeeBoomDeepBeeBeeDeepBeeBoomBeeBeeDeepDeepDeepBoomBeeBeeBeeDeepDeepBoomBeeBeeBeeBoomDeepDeepBeeBeeBoomDeepBeeBoom"

t2 = ""

tmp = "B"

for i in range(1,len(texte)) :
    if texte[i].isupper():
        match tmp:
            case "Bee":
                t2+="."
            case "Deep":
                t2+="_"
            case "Boom":
                t2+=" "
            case _:
                t2+="_"
        
    tmp += texte[i]