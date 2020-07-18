#/bin/Python
import subprocess
import argparse, sys
import pexpect


LYNIS_URL="https://github.com/CISOfy/lynis"



def m_git_clone_Lynis():
    lynis_url =LYNIS_URL
    git_co = subprocess.run(["git","clone",lynis_url])
    
def m_rm_Lynis():
    rm_lynis = subprocess.run(["rm", "-rf", "lynis"])
    
    
def m_run_Lynis_Full():
    '''Requirement:Pexpect'''
    '''Todo implement execution no pexpect'''
    LynisFull_Child= pexpect.spawn('/bin/bash -c "cd lynis && ./lynis audit system > ../LynisTestReport.txt"')
    
    #Interesting code could be put here
    LynisFull_Child.expect(pexpect.EOF, timeout=None)
    
    

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("-c", "--clone", help="Auto Clone the latest Lynis from LYNIS_URL to lynis dir",action="store_true")
    parser.add_argument("-r", "--run", help="Run the specified run suite from lynis dir")
    parser.add_argument("--clean", help="Remove Lynis Directory",action="store_true")
    args=parser.parse_args()   

    
    if args.clean:
        print("Cleaning Lynis Subdirectory...")
        m_rm_Lynis()
        print("...Done Cleaning Subdirectory")
    elif args.clone:
        print("Cloning....")
        m_git_clone_Lynis()
        print("...Done Cloning")
    elif args.run:
        if (args.run == 'FULL'):
            print("Executing Lynis Suite, Generating Report....")
            m_run_Lynis_Full()
            print("Done")
        pass
    
if __name__ == '__main__':
    main()
