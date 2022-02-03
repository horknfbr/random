#!/bin/env python3

pathString = ["PDX-SFO", "SEA-JFK", "SFO-SEA", "LAX-PDX"]


def breakPairs(pairList):
    toFrom = {}
    fromTo = {}
    srca = ''
    dsta = ''
    src = ''
    dst = ''
    for i in pairList:
        airports = i.split('-')
        toFrom[airports[0]] = airports[1]
        fromTo[airports[1]] = airports[0]

    for key in toFrom.keys():
        if key not in fromTo.keys():
            srca = key

    for keye in fromTo.keys():
        if keye not in toFrom.keys():
            dsta = keye

    retString = f"{ srca }-{ toFrom[srca] }, "

    src = toFrom[srca]

    for e in toFrom.keys():
        if toFrom.get(e) && fromTo.get(e):
            retString = f"{ retString }{ fromTo[e] }-{ toFrom[fromTo[e]] }, "

    # if srca:
    #     for e in fromTo.keys():
    #         if dsta and fromTo.get(e):
    #             retString = f"{retString}{e}-{toFrom[e]}, "
    #         else:
    #             retString = f"{e}-{toFrom[e]}, {retString}"
    #         srca = toFrom.get(e)
    #         dsta = fromTo.get(e)

    print(f"Path: { retString }")


if __name__ == "__main__":
    print(f"Unsorted: { pathString }")
    breakPairs(pathString)
