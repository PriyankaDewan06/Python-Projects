email = input ("Please enter your email: ")
k,j,d=0,0,0
if len(email)>=6:           # condition for proper length of email
   if email[0].isalpha():   # condition for starting email with alphabet
     if("@" in email) and (email.count("@")==1): # condition for containing one (@)sign in email
      if(email[-4]=='.') ^ (email[-3]=='.'): # condition for containing (.)sign in proper position
        for i in email:
         if i==i.isspace(): # condition for containing no space within email
                k=1
         elif i.isalpha():
              if i==i.upper(): #condition for containing 1st letter not in uppercase
                      j=1  
         elif i.isdigit(): 
                continue
         elif i=="_"or i=="."or i=="@":
                continue
         else:
               d=1       
        if k==1 or j==1 or d==1:
                 print("Wrong Email,Please enter correct pattern of your email") 
        else:
             print("Congratulations !! Your email is correct") 
      else:
         print("Wrong Email,Please enter correct pattern of your email")
     else:
         print("Wrong Email: email cannot contain more than one @ sign")
   else:
        print('Wrong Email: email must start with an alphabet')
else:
 print('Wrong Email: length of email is not correct')