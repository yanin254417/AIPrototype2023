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
def parse_input(num,XX):
    parser = argparse.ArgumentParser("--num", "--XX")

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

def multiplyby9(inputV):
    print(9*inputV)

if __name__ == "_main_":
    input_v = parse_input()
    print(f'the input XX is {input_v.XX}')
    print('we are in the main function')
    multiplyby9(input_v.num)
sum = 0
print(f"first run num=100 XX=90")
first = subprocess.run(["python","first.py", "--num", "100", "--XX", "90"])
print(f"sum of first run = {extract(first)}")
print(f"Hello world!")

print(f"second run num=-10 XX=-90")
second = subprocess.run(["python","first.py", "--num", "-10", "--XX", "-90"])
print(f"sum of second run = {extract(second)}")
print(f"Hello world!")

print(f"third run num=0")
third = subprocess.run(["python","first.py", "--num", "0"])
print(f"sum of third run = {extract(third)}")
print(f"Hello world!")

print(f"extract(first+second+third)")
