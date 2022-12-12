
data = [
    ["ID1234558226801","090"], #26
    ["ID1234558226802","088"],
    ["ID1234558226803","050"],
    ["ID1234558226804","070"]    #100
]

dataFrom = {
    "ip" : "", #30
    "port" : 0,
    "data" : ""
}

STX = 0x01
ETX = 0x02

txData = {
    "stx" : STX,
    "area" : 1,
    "rack" : 0,
    "status" : 0,
    "v37" : 60,
    "v74" : 90,
    "first" : "kwang seon",
    "last" : "hong",
    "phone" : "010-2401-9059",
    "from" : dataFrom,
    "age" : 63,
    "count" : 0,
    "data" : data,
    "dataSize" : 0,
    "etx" : ETX  #150
}
