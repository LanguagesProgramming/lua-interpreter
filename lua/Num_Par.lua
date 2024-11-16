
function esPar(n)
    local par = false
    if n%2 == 0 then
        par = true
    end
    return par
end
    
num = 25
num2 = 150
num3 = 78
num4 = 51
num5 = 40

local array = { 25, 150, 78, 51, 40 }

for i = 1, #array do
    print("El numero es "array[i])
end
