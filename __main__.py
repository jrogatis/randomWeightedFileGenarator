import csv
import modelRandonWeighted as md
import fixed_dics as fxDics
quant_lines = 100000
lines = 0
# write the block od lines
with open('bank-100mil.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # header
    writer.writerow(fxDics.header)
    # write the line
    while lines < quant_lines:
        data = md.register()
        # write the data
        writer.writerow(data)
        lines = lines + 1
        print(f'{lines} lines of: {quant_lines}, {(lines/quant_lines) * 100 }')
f.close()
