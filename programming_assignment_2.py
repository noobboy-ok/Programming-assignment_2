#Problem 1:
#1
def next_string(s):
    A = ['a', 'b', 'c', 'd']
    x = len(s)
    next_string_list = list(s)
    
    for i in range(x - 1, -1, -1):
        if next_string_list[i] != 'd':
            next_string_list[i] = A[A.index(next_string_list[i]) + 1]
            
            for j in range(i + 1, x):
                next_string_list = 'a'
            return "".join(next_string_list)
    return 'a'* (x + 1)
           
n = input("Hay nhap chuoi bat ky: ")
list_result = [s.strip() for s in n.split(',')]
for string in list_result:
    result = next_string(string)
    print(f"Chuoi tiep theo cua {string} la {result}")  

#2        
    
def wavy(s):
    if len(s) < 2: return True
    for i in range(len(s) - 1):
        if i % 2 == 0:
            if not (s[i] < s[i+1]): return False
        else:          
            if not (s[i] > s[i+1]): return False
    return True

def closest_wavy(s):
    a = next_string(s)
    while not wavy(a):
        a = next_string(a)
    return a

b = input("\nHay nhap cac chuoi cho Bai 2 : ")


list_input2 = [s.strip() for s in n2.split(',')]

list_result2 = []
for string in list_input2:
    res = closest_wavy(string)
    list_result2.append(res)

print("Chuoi wavy dung sau la: " + ", ".join(list_result2))















