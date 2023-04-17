from RNG import rand_nums

def kumpul(list_candi, idx_rng):
  increment = 0
  print("Jin menemukan", end=" ")
  for i in range(1, 4):
    list_candi[i][2] += rand_nums[((idx_rng-1)*3)+i]
    if i == 1:
      list_candi[i][0] = "pasir"
      print(rand_nums[((idx_rng-1)*3)+i], "pasir", end= " ")
    if i ==2:
      list_candi[i][0] = "batu"
      print(rand_nums[((idx_rng-1)*3)+i], "batu", end=" ")
    if i == 3:
      list_candi[i][0] = "air"
      print(rand_nums[((idx_rng-1)*3)+i], "air")
  return list_candi