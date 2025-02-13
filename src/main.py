import task1
import task2
import task3

print("Task 1:")
task1.kwargsAcceptFun(name="Dilshod", hobby="Tennis")

print("\nTask 2:")
result = task2.typeBasedTransformer(
    num=7, pi=3.14, text="Python", flag=False, items=(10, 20, 30),
    pairs={"x": 5, "y": 10}
)
print(result)

print("\nTask 3:")
task3.func()
task3.funx()
task3.func()
task3.funx()
task3.func()