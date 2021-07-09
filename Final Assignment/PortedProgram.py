# Comp 333 Final Project - Ported Program (Written in Python)

# This converted program actually resulted in about 67 lines which is 35 less than that of the original
# one which came in at 102. Both function in a fairly similar manner, and all the calculations seem to be 
# perfectly fine. You're welcome to use any test cases you'd like for a sample run but this is just one
# of the series of inputs I've used for both the original in C as well as this ported one in Python:
# (1 3 2.5 1 6 3 4 5 2 2 3 4 5)

totalCycles = 0.0
totalInstructionCount = 0
numberOfClasses = 0
clockCycleRate = 0.0
cyclesPerInstruction = 0.0
instructionCount = 0

def EnterParameters():
    global totalCycles
    global totalInstructionCount
    global numberOfClasses
    global clockCycleRate
    global cyclesPerInstruction
    global instructionCount
    totalInstructionCount = 0
    totalCycles = 0.0
    print("Enter the number of instruction classes:")
    numberOfClasses = int(input())
    print("Enter the frequencey of the machine (GHz):")
    clockCycleRate = float(input())
    for element in range(numberOfClasses):
        print("Enter the CPI of the class:")
        cyclesPerInstruction = float(input())
        print("Enter the instruction count of the class (billions): ")
        instructionCount = int(input())
        totalInstructionCount += instructionCount
        totalCycles += cyclesPerInstruction * instructionCount

def CalculateCPI():
    averageCPI = totalCycles / totalInstructionCount
    print("The average CPI of the sequence is: " + str(averageCPI))

def CalculateExecutionTime():
    executionTime = totalCycles / clockCycleRate
    print("The execution time of the sequence is: " + str(executionTime) + " seconds")

def CalculateMIPS():
    mips = 1000 * (totalInstructionCount / (totalCycles / clockCycleRate))
    print("The total MIPS of the sequence is: " + str(mips))

def main():
    choice = 0
    while choice != 5:
        print("\nMeasuring Performance:")
        print("----------------------")
        print("1) Enter parameters")
        print("2) Calculate CPI of a sequence")
        print("3) Calculate Execution time of a sequence")
        print("4) Calculate MIPS of a sequence")
        print("5) Exit program")
        print("Enter selection: ")
        choice = int(input())
        print("")
        def switch_statement(choice):
            switcher = {
                1: EnterParameters,
                2: CalculateCPI,
                3: CalculateExecutionTime,
                4: CalculateMIPS
            }
            func = switcher.get(choice, lambda: "Invalid choice")
            func()
        switch_statement(choice)

main()
