#MFR - My File Rename

This small Python module is the result of having to try and sort out horrible filename from usually Internet Downloaded resources. I am perfectly capable of typing "mv X y" but the **.iThisZ_S0-Kool** stuff drives me around the twist (Yes I am becoming a grumpy old man).

So **MFR** is just a wrapper for a little

* os.walk
* re.find
* str.replace
* os.rename


I took the oppertunity to add some moderate command line parsing options, plus logging. The latter is one of the most underutilised Python modules I feel.

#I Have tested this on


##OS

* Max 10.4
* Ubuntu 12
* Ubuntu 14

##Python

* 2.7
* 3.4

#Install

Test and then move to **/usr/local/bin/** you need to chmod +x and then you should be ready to use this.

#Usage

I have a collection of similarly names files - looking like this


    .                                             School 3 Report Stud Junk E-Subs [MissX].txt  School 8 Report Stud Junk E-Subs [MissX].txt
    ..                                            School 4 Report Stud Junk E-Subs [MissX].txt  School 9 Report Stud Junk E-Subs [MissX].txt
    School 1 Report Stud Junk E-Subs [MissX].txt  School 5 Report Stud Junk E-Subs [MissX].txt  t.sh
    School 10 Report Stud Junk E-Subs [MissX].txt School 6 Report Stud Junk E-Subs [MissX].txt
    School 2 Report Stud Junk E-Subs [MissX].txt  School 7 Report Stud Junk E-Subs [MissX].txt
    
    
So I type
 
    mfr -f txt -i "[MissX]"
 
This means find **--file** txt, with **--input** [MissX] 

You will see something like this



    DEBUG:root:Debug Enabled
    DEBUG:__main__:file    is txt
    DEBUG:__main__:from    is [MissX]
    DEBUG:__main__:to      is 
    DEBUG:__main__:write   is False
    DEBUG:__main__:file    is txt
    INFO:__main__:Starting
    DEBUG:__main__:Orig File School 1 Report Stud Junk E-Subs [MissX].txt
    DEBUG:__main__:TEST: mv ./School 1 Report Stud Junk E-Subs [MissX].txt to ./School 1 Report Stud Junk E-Subs .txt
    DEBUG:__main__:Orig File School 10 Report Stud Junk E-Subs [MissX].txt
    DEBUG:__main__:TEST: mv ./School 10 Report Stud Junk E-Subs [MissX].txt to ./School 10 Report Stud Junk E-Subs .txt
    DEBUG:__main__:Orig File School 2 Report Stud Junk E-Subs [MissX].txt
    DEBUG:__main__:TEST: mv ./School 2 Report Stud Junk E-Subs [MissX].txt to ./School 2 Report Stud Junk E-Subs .txt
    DEBUG:__main__:Orig File School 3 Report Stud Junk E-Subs [MissX].txt
    DEBUG:__main__:TEST: mv ./School 3 Report Stud Junk E-Subs [MissX].txt to ./School 3 Report Stud Junk E-Subs .txt
    DEBUG:__main__:Orig File School 4 Report Stud Junk E-Subs [MissX].txt
    DEBUG:__main__:TEST: mv ./School 4 Report Stud Junk E-Subs [MissX].txt to ./School 4 Report Stud Junk E-Subs .txt
    DEBUG:__main__:Orig File School 5 Report Stud Junk E-Subs [MissX].txt
    DEBUG:__main__:TEST: mv ./School 5 Report Stud Junk E-Subs [MissX].txt to ./School 5 Report Stud Junk E-Subs .txt
    DEBUG:__main__:Orig File School 6 Report Stud Junk E-Subs [MissX].txt
    DEBUG:__main__:TEST: mv ./School 6 Report Stud Junk E-Subs [MissX].txt to ./School 6 Report Stud Junk E-Subs .txt
    DEBUG:__main__:Orig File School 7 Report Stud Junk E-Subs [MissX].txt
    DEBUG:__main__:TEST: mv ./School 7 Report Stud Junk E-Subs [MissX].txt to ./School 7 Report Stud Junk E-Subs .txt
    DEBUG:__main__:Orig File School 8 Report Stud Junk E-Subs [MissX].txt
    DEBUG:__main__:TEST: mv ./School 8 Report Stud Junk E-Subs [MissX].txt to ./School 8 Report Stud Junk E-Subs .txt
    DEBUG:__main__:Orig File School 9 Report Stud Junk E-Subs [MissX].txt
    DEBUG:__main__:TEST: mv ./School 9 Report Stud Junk E-Subs [MissX].txt to ./School 9 Report Stud Junk E-Subs .txt
 
 
 Looking **CAREFULLY** , you can see it is telling what it would Do.... i.e. Remove the [MissX]
 
 If you have to change [MissX] to something else - the command will be
 
     mfr -f txt -i "[MissX]" -o "Operator"
     
  and you will see
  
      DEBUG:__main__:TEST: mv ./School 9 Report Stud Junk E-Subs [MissX].txt to ./School 9 Report Stud Junk E-Subs Operator.txt
      
      
 ## Happy with what will happen ?
 
 Then you add the **--write** or **-w** command
 
     mfr -f txt -i "[MissX]" -o "Operator" -w
  
  or

     mfr -f txt -i "[MissX]" -o "Operator" -i "Operator"-w
  
  
  #Confused ?
  
  There is some help...
  
      mfr --help
      
      
  