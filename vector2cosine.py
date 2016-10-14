"""
-------reade  vectore file and find cosine similarity-------
input_file:
------------
10 100
sent_1 1 . . . 100th
.
.
.
sent_10 1  . . . 100th

output file:
------------
sent_0 12
sent_1 .56
.
.
.
sent_10 5.6

"""
def vector2cosine(file_vec):
    inputFile=open(file_vec,'r')
    outputFile=open(file_vec+"_sentence_cosine_value.txt",'w')

    #lines_list=file_id.readlines()
    #print lines_list
    line_list=inputFile.readlines()
    line_1=line_list[0].split(' ')

    row_count=int(line_1[0])
    colum_count=int(line_1[1])

    data_arr=[]
    mat=[]
    i=0
    """
    delete the first 2 length row , clm array and
    create only a vectore array
    """
    for line in line_list:
        if i!=0:
            data_arr=line.replace('\n','').split(' ')
            mat.append(data_arr)
            
        i+=1

    """
    1. remove sent_x string from front
    2. replace string value by int(str_value) value
    """
    for i in range(0,row_count):
        line=mat[i]
        line.remove('sent_'+str(i))
        line=[float(x) for x in line]
        mat[i]=line

    #print len(mat[1])

    from scipy import spatial

    #-------test
    #cosine_val=1-spatial.distance.cosine(mat[1],mat[2])
    #print cosine_val

    """
    #test
    for x in mat:
        print len(x)
    """

    """
    1. calculate pair wise cosine(s1,s2) value
    """

    sent_cosine_val_array=[]
    i=0
    for u in mat:
        
        j=0
        sent_u_val=0.0
        for v in mat:

            #print i,j
            cosine_val=1-spatial.distance.cosine(u,v)
            sent_u_val+=cosine_val
            #cosine_val=float(cosine_val)
            
            #print "cosine(u,v) = "+str(cosine_val)+"\n"
            j+=1
        
        #print "sent_"+str(i)+" total cosine value = "+str(sent_u_val)
        sent_output=str("sent_"+str(i)+" "+str(sent_u_val/len(mat))+'\n')
        outputFile.write(sent_output)
        #sent_cosine_val_array.append(sent_u_val/len(mat))
        
        i+=1
        
        
    #print "len-----> "+str(len(sent_cosine_val_array))
    
#----------------------start execution from here-----
import sys
if len(sys.argv)> 1:
    vector2cosine(sys.argv[1])
else :
    print "-------------Error-----------in vector2cosine.py\n"




    
gi
