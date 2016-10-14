#seperate sentance ended by period
"""


"""
file=open('news1.txt','r')
file1=open('news11','w')

#lines_list=file_id.readlines()
#print lines_list

line_list=file.read().split('.')



print line_list


i=0

for line in line_list:

    file1.write(str(line)+""+str(i))
    print str(line)+"------"+str(i)    
    i=i+1

