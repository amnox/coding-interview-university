arr = [ 1242, 1683, 2491, 2941, 4057, 5299, 5362, 6875, 6895, 7359, 7630, 8606, 9516, 9519, 10228, 11512, 11802, 12108, 12633, 14946, 15146, 15758, 16751, 18135, 19498, 20283, 20390, 21358, 22948, 24120, 24166, 24415, 24931, 25472, 25634, 25934, 27802, 29083, 29911, 29939, 30046, 32968, 33327, 35450, 37355, 37530, 38030, 40818, 41161, 41372, 42813, 44485, 44544, 46095, 47724, 48304, 48772, 49982, 50494, 51444, 53289, 54298, 54959, 55233, 55278, 55737, 56838, 58222, 58294, 58402, 58875, 61614, 63653, 66360, 66763, 67531, 68054, 68671, 70548, 72087, 75691, 77630, 78085, 78393, 79458, 79645, 80195, 83071, 83686, 84108, 85016, 88051, 88252, 89986, 91533, 93780, 94199, 94312, 98556, 98665 ]

print(arr)
print(len(arr)//2)
mid = len(arr)//2
print(arr[mid])

def jam(arr, l, r, x):
      print (arr, l, r, x)
      mid = (l+r+1)//2
      print(mid)
      if arr[mid]==x:
            return mid
      if arr[mid]<x:
            l1 = mid
            r1 = r
      elif arr[mid]>x:
            l1 = l
            r1 = mid
      return jam(arr, l1,r1,x)


x = 88051

print("Calculated: ",jam(arr, 0, len(arr) - 1, x))

print("REal: ",arr.index(x))
