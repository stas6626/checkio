'''
You have a histogram. Try to find size of the biggest rectangle you can build out of the histogram bars:)
'''

def largest_histogram(histogram):
    maximum=max(histogram)
    local_max=0
    q=len(histogram)
    
    for i in range(1,maximum+1):
        macks=0
        
        for i1 in range(0,q):
            
            if ((histogram[i1-1]<i)and (i1>0)):
                macks=0
                
            if histogram[i1]>=i:
                macks+=1
                
            if (macks*i)>local_max:
                local_max=i*macks
                
    return local_max
