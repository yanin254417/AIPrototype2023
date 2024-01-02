import subprocess #สำหรับรัน terminal command

if __name__ == "__main__":
    # basic terminal command
    subprocess.run(["ls","-ltr"])
    subprocess.run(["rm","-r","home/yanin/testfolder1"])

    
#python commands
print(f"first run num=100 XX=90")
subprocess.run(["python","first.py", "--num", "100", "--XX", "90"])
print(f"-----------------------------------------------")
print(f"second run num=-10 XX=-90")
subprocess.run(["python","first.py", "--num", "-10", "--XX", "-90"])
print(f"-----------------------------------------------")
print(f"third run num=0")
subprocess.run(["python","first.py", "--num", "0"])
print(f"-----------------------------------------------")


#use output from other program
process_output = subprocess.Popen(["python", "first.py", "--num", "0"],
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
out, err = process_output.communicate()
print(out.decode('utf-8'))
print(len(out.decode('utf-8')))

#HW เขียน subproce
# ss sum output ทั้งหมดของ 3 อันข้างบน (ตัวเลขก่อน Hello world!)
import argparse
import re
def extract_numeric(word):
    for i in word.splitlines():
        if i.strip().isdigit() or (i.strip().lstrip('-').isdigit()):
            return int(i.strip())
    return 0 


#def parse_input():
    parser = argparse.ArgumentParser()

    parser.add_argument(
    "--num",
    type=int,
    required=True,
)
    parser.add_argument(
    "--XX",
    type=int,
    default=7
)

    args = parser.parse_args()
    return args

if __name__ == "__main__":

    print(f"first run num=100 XX=90")
    first = subprocess.run(["python","first.py", "--num", "100", "--XX", "90"])#, capture_output = True)
    print(f"Hello world!")

    print(f"second run num=-10 XX=-90")
    second = subprocess.run(["python","first.py", "--num", "-10", "--XX", "-90"])#, capture_output = True)
    print(f"Hello world!")

    print(f"third run num=0")
    third = subprocess.run(["python","first.py", "--num", "0"])#, capture_output = True)
    print(f"Hello world!")



    output1 = extract_numeric(first.stdout.decode('utf-8'))
    output2 = extract_numeric(second.stdout.decode('utf-8'))
    output3 = extract_numeric(third.stdout.decode('utf-8'))

    total = sum([output1,output2,output3])
    print(f"sum: {output1} + {output2} + {output3} = {total}")