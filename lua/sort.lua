local function bubble_sort(arr) ; local n = #arr ; for i = 1, n - 1 do ; for j = 1, n - i do ; if arr[j] > arr[j + 1] then arr[j], arr[j + 1] = arr[j + 1], arr[j] end end end end

local array = { 5, 4, 3, 2, 1 }

bubble_sort(array)

for i = 1, #array do print(array[i]) end
