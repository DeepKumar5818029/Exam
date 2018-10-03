read1 = raw_input().split()
city = int(read1[0])
pCity = int(read1[1])
powerStation = [ 0 for i in range(city)]

hasPower = [False for i in range(city)]

a = [[ 0  for i in range(city)]for j in range(city)]
read2 = raw_input().split()

for i in range(pCity):
            powerStation[i] = (int(read2[i]))
            hasPower[powerStation[i]-1] = True

for i in range(city):
            read3 = raw_input().split()
            for j in range(city):
                        a[i][j] = int(read3[j])

def elec(K,n):
            mnCost = mxCost = mnCostId = totalCost = 0

            for k in range(K,n):
                        mnCost = 99999999

                        for i in range(n):
                                    if(hasPower[i] == False):
                                                for j in range(k):
                                                            if(a[i][powerStation[j]-1] < mnCost and i != (powerStation[j]-1)):
                                                                        mnCost = a[i][powerStation[j]-1]
                                                                        mnCostId = i
                                                totalCost += mnCost
                                                hasPower[mnCostId] = True
                                                powerStation[k] = mnCostId+1

            print totalCost

elec(pCity,city)
                                                                        
