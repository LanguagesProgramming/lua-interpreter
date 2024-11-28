-- Busqueda binaria

function busquedaBinaria(array, item) 
    local primero = 0
    local ultimo = #array - 1
    local encontrado = false
    local indice = -1

    while (primero<=ultimo and not encontrado) do
        local puntoMedio = (primero + ultimo)/2
        if array[puntoMedio] == item then
            encontrado = True
            -- Si el valor buscado fue encontrado, se agrega el indice donde esta el valor
            indice = puntoMedio
        elseif item < array[puntoMedio] then
                ultimo = puntoMedio-1
            else
                primero = puntoMedio+1
            end
        end
    end

    return indice
end

valoresPrueba = {0, 1, 2, 8, 13, 17, 19, 32, 42}
print(busquedaBinaria(valoresPrueba, 3))
print(busquedaBinaria(valoresPrueba, 13))