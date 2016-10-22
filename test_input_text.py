
inputFile=open('news1.txt','r')
outputFile=open('news1_processed_data.txt','w')

news_data=inputFile.read().replace('\n','')
news_data=news_data.replace('.com','')
news_data=news_data.replace('\'','')
news_data=news_data.replace('\"','')

line_list=news_data.split('.')

data_str=""
for x in line_list:
    x=str(x+'\n')
    data_str+=x
    
    print len(x)

print data_str
outputFile.write(data_str)
inputFile.close()
outputFile.close()



