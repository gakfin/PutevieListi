import xlsxwriter
workbook = xlsxwriter.Workbook('Пох.xlsx')
worksheet = workbook.add_worksheet('Еще больше пох')
schetchik = True
y = 3
x = 'A'
z = 'B'
q = 3
write_format = workbook.add_format({
    'bold': 0,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'fg_color': 'white'
    })

voditel = []
with open("voditel.txt") as f:
	for line in f:
		voditel.append([str(x) for x in line.split()])

avto = ["зил", "уаз", "говно"]



while schetchik:

        for spskvod in enumerate(voditel):
            print (spskvod)
        xyu = int(input())
        if xyu==88:
            break
        #print (voditel[xyu])

        for spskavto in enumerate(avto):
            print (spskavto)
        yux = int(input())
        #print (avto[yux])
        print (voditel[xyu],avto[yux])

        #worksheet.write('A1', voditel[xyu], write_format)
        #worksheet.write('B1', avto[yux], write_format)

        def suko (x,y):
            return (x + str(y))

        def buko (z,q):
            return (z + str(q))

        oio = buko (z,q)
        ioi = suko (x,y)
        y += 1
        q += 1

        worksheet.write(ioi, voditel[xyu], write_format)
        worksheet.write(oio, avto[yux], write_format)



workbook.close()
