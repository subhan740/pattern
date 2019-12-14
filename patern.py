
#include <iostream>

using namespace std;

int main()
{
    int n;
     cout<<"Enter a number\n";
     cin>>n;
    int x=0;
    for(int i=0;i<2*n;i++)
    {
        bool flag = false;
        if(i<n+1)cout<<"@";else cout<<" ";
        for(int j=0;j<n*(n-1)+1;j++){
            if(i>=n/2 && i<2*n-n/2){
                if(j<(n-1)*x||j>(n-1)*x+n-1)cout<<" ";
                else
                cout<<"*";
                flag=true;
            }
            else cout<<" ";
        }
        if(flag)x++;
        if(i>=n-1)cout<<"@";else cout<<" ";
        cout<<endl;
    }
}


============================================================
#rows=int(input('enter no of rows: '))
#for i in range(rows):
#    if i%2==0:
#        print(' '*(rows-i-1)+'* '*(i+1))
#    if 2*i+1==rows:
#        print(end="@"*(2*i+3))        
#for j in range(rows-1,0,-1):
#    if j%2!=0:
#        print(' '*(rows-j)+'* '*(j))


'''PRINTING ASCII CHARACTER VALUE '''       
#
#a=65
#for i in range(65,122):
#    print(a,chr(a))
#    a=a+1


'''***Right angle triangle with character'''
#n=int(input('enter no of rows'))
#for i in range(n):
#    print((chr(65+i)+'  ')*(i+1))

'''*** Inverted Right Angle Triangle pattern with * symbols'''
#n=int(input('enter no of rows: '))
#for i in range(n):
#    print((' * ')*(n-i))

'''*** square pattern with provided fixed digit'''
#n=int(input('enter no of rows: '))
#for i in range(n):
#    print((str(n)+' ')*n)
'''***square pattern with provided fixed digit in every row:'''
#n=int(input('enter no of rows: '))
#for i in range(n):
#    print((str(i+1)+' ')*n)
'''***Right Angle Triangle pattern with fixed alphabet symbol'''
#n=int(input('enter raws: '))
#for i in range(n):
#    print((chr(65+i)+' ')*(i+1))

'''***Inverted Right Angle Triangle pattern with digits'''
#n=int(input('enter rows'))
#for i in range(n):
#    for j in range(n-i):
#        print(j+1,end=' ')
#    print()    
'''***To print Pyramid pattern with fixed digit in every row'''
#n=int(input('enter rows: '))
#for i in range(n):
#    print(' '*(n-i-1)+(str(i+1)+' ')*(i+1))

'''***Pyramid pattern with alphabet symbols in reverse of dictionary order'''
#n=int(input('enter rows: '))
#for i in range(n):
#    print(' '*(n-i-1),end=' ')
#    for j in range(i+1):
#        print(chr(64+n-j),end=' ')
#    print()   
 
'''***To print Diamond Pattern with * symbols'''
#n=int(input('enter no of rows: '))
#for i in range(n):
#    print(' '*(n-i-1)+'* '*(i+1))    
#for i in range(n-1):
#    print(' '*(i+1)+'* '*(n-i-1))

'''***Right Half Diamond Pattern with alphabet symbols in dictionary order'''
#n=int(input('enter no of rows: '))
#for i in range(n):
#    for j in range(i+1):
#        print(chr(65+j),end=" ")
#    print()   
#for i in range(n-1):
#    for j in range(n-i-1):
#        print(chr(65+j),end=' ')
#    print()    


'''***To print Inverted Pyramid Pattern with alphabet symbols in dictionary order'''
#n=int(input('enter no of rows: '))
#for i in range(n):
#    print(' '*i,end=' ')
#    for j in range(n-i):
#        print(chr(65+j),end=' ')   
#    print()    

'''***To print Right Half Diamond Pattern with * symbols'''
#n=int(input('enter no of rows: '))
#for i in range(n):
#    print('* '*(i+1))
#for i in range(n-1):
#    print('* '*(n-i-1))

'''***To print Left Half Diamond Pattern with * symbols'''
#n=int(input('enter no of rows: '))
#for i in range(n):
#    print('  '*(n-i-1)+'* '*(i+1))
#for i in range(n-1):
#    print('  '*(i+1)+'* '*(n-i-1))    

''' ***To print Top Half HALLOW DIAMOND PATTERN with * symbols'''
#n=int(input('enter rows: '))
#for i in range(n):
#    print('  '*(n-i-1)+'* ',end='')
#    if i>=1:
#        print('  '*(2*i-1)+'*',end='') 
#    print()    
#  

'''***To print Bottom Half Hallow Diamond Pattern with * symbols'''
#n=int(input('enter rows: '))
#for i in range(n):
#    print('  '*i+'* ',end='')
#    if i!=(n-1):
#        print('  '*(2*n-2*i-3)+'*',end='') 
#    print()    
#  


                
'''***Print Hollow Rectangle star pattern'''

#rows=int(input('enter no of rows: '))
#cols=int(input('enter no of cols: '))
#print('Hollow rectangle star pattern')
#for i in range(rows):
#    for j in range(cols):
#        if(i == 0 or i == rows-1 or j == 0 or j == cols-1):
#            print('* ',end =' ')
#        else:
#            print(' ',end =' ')
#    print()            
#            

'''***pattern prog to print inverted triangle'''
#n = int(input('enter no: '))
#print('The required star pattern')
#
##for i in range(n,0,-1):
##    for k in range(n,i,-1):
##        print(' ',end='')
##    for j in range(1,i*2):
##        print('*',end='')
##    print()    
#    
#for i in range(n):
#    if i%2!=0:
#        print()
#    else:
#        print(' '*(n-i-1)+" *"*(i+1))

'''***WEBKUL PATTERN PROGRAM'''

#n=int(input('enter rows: '))
#if(n<1 or n%2==0):
#    print('plese enter odd +ve integer')
#else:    
#    for i in range(n-1):
#        print(' '*(n-i-1)+'* '*(i+1))
#        if(i==n-2):    
#            print('* '*(n)+'@ '*(n+2))
#        
#    for i in range(n-1):
#        print(' '*(i+1)+'* '*(n-i-1))    




'''***printing invert pyramid triangle pattern'''
#n = int(input('enter no: '))
#print('The required star pattern')
#
#    
#for i in range(n):
#    if i%2!=0:
#        print()
#    else:
#        print(' '*(n-i-1)+" *"*(i+1))
#
#    
#for j in range(i):
#    if j%2==0:
#        print()
#    else:    
#        print(' '*(j+1)+" *"*(i-j))
        
    

####diamond pattern
#rows=int(input('enter no of rows: '))
#for i in range(rows):
#    if i%2==0:
#        print(' '*(rows-i-1)+'* '*(i+1))        
#for j in range(rows-1,0,-1):
#    if j%2!=0:
#        print(' '*(rows-j)+'* '*(j))



''' FABONACCI SERIES'''
#a,b=0,1
#for i in range(0, 10):
#    print(a)
#    a,b=b,a+b
    
#n=int(input("enter a no: "))
#for i in range(n):
#    for j in range(0,n//2):
#        print()
#    for j in range(i):
#        print(end="  ")
#    for j in range(n-(2*i)):
#        print('@',end="")
#        print(end=" ")
#for i in range(n):
#    for j in range(n):
#        if(i == 0 or j == 0 or j == n - 1):
#            print('*', end = '  ')
#        else:
#            print(' ', end = '  ')
#    print()   
# 

'''***WEBKUL PATTERN INTERVIEW Que 2019 for odd no of user input'''              
#n = int(input('enter no: '))
#print('The required star pattern') 
#if(n<1 or n%2==0):
#    print("enter odd +ve intgr")
#else:    
#    for i in range(n+1):
#        if i%2!=0:
#            print()
#        else:    
#            print(' '*(i+1)+" @"*(n-i))
#    for i in range(n):
#        for j in range(n):
#            if(i == 0 or j == 0 or j == n - 1):
#                print('*', end = ' ')
#            else:
#                print(' ', end = ' ')
#        print()


'''***ALGOSCALE PATTERN QUE'''
#
#n=int((input('enter rows: ')))
#for i in range(n):
#    if(i==0):
#        print(' '*(n-i-1)+'* '*n)
#    elif(i==n-1):
#        print('* '*n)
#    else:
#        print(' '*(n-i-1)+'* '+'  '*(n-2)+'*')
#        


'''***WEBKUL pattern program 2019'''
        
#n=int(input('enter rows: ')) 
#for i in range(n):
#   
#    if(i==n-1):
#        print('* '*(2*n+2))
#    elif(i==n-2):
#        print('* '*n+'  '*(n)+'* ')
#    else:    
#        print('* '*(i+1))    
#for i in range(n):
#    if(i==0):
#        print('* '*n+'  '*(n)+'* ')
#    else:
#        print('* '*(n-i))        
#    



