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

#HW เขียน subprocess sum output ทั้งหมดของ 3 อันข้างบน (ตัวเลขก่อน Hello world!)
import argparse

def parse_input():
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

def extract_numeric():

sum = 0
print(f"first run num=100 XX=90")
first = subprocess.run(["python","first.py", "--num", "100", "--XX", "90"])
print(f"Hello world!")

print(f"second run num=-10 XX=-90")
second = subprocess.run(["python","first.py", "--num", "-10", "--XX", "-90"])
print(f"Hello world!")

print(f"third run num=0")
third = subprocess.run(["python","first.py", "--num", "0"])
print(f"Hello world!")

if __name__ == "__main__":

output1 = extract_numeric(first.stdout)
output2 = extract_numeric(second.stdout)
output3 = extract_numeric(third.stdout)