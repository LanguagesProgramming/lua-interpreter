function factorial(n)
    local resultado = 1
    for i = 1, n do
        resultado = resultado * i
    end
    return resultado
end