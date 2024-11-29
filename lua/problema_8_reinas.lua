-- Problemas de las 8 reinas
function imprimir(tablero, letras, n) 
    -- Imprime cabecera
    print("   ")
        
    for i = 0, #n-1 do
        print(" " + letras[i] + "     ")
        i++
    end
        
    print("\n")
        
    -- Imprime tablero - filas 0 a (n - 1)
    for i = 0, #n-1 do
            
        -- Imprime índice de fila
        print((i + 1))
            
        -- Imprime fila i - Columnas 0 a (n - 1)
        for j = 0, #n-1 do
            print("   " + tablero[i][j] + "   ")

            j++
        end

        i++
            
        print("\n\n")
    end      
end

function posicionVerdadera(fila, columna, tablero)
    -- Verificar que la fila actual sea segura, verificando cada columna de esta
    for iterColumna = 1, #tablero do
        if iterColumna ~= columna then
            if tablero[fila][iterColumna] == 1 then
                return false
            end
        end
    end

    -- Verificar que la columna actual sea segura, verificando cada fila de esta
    for iterFila = 1, #tablero do
        if iterFila ~= fila then
            if tablero[iterFila][columna] == 1 then
                return false
            end
        end
    end

    -- Verificar que la diagonal superior (pendiente positiva) sea segura
    -- Buscar el extremo izquierdo de la diagonal superior
    local iterColumna = columna
    local iterFila = fila

    while iterColumna > 1 and iterFila < #tablero do
        iterFila = iterFila + 1
        iterColumna = iterColumna - 1
    end

    -- Recorrer toda la diagonal excepto la posición marcada por los parámetros fila, columna
    while iterFila >= 1 and iterColumna <= #tablero do
        if not (iterFila == fila and iterColumna == columna) then
            if tablero[iterFila][iterColumna] == 1 then
                return false
            end
        end
        iterFila = iterFila - 1
        iterColumna = iterColumna + 1
    end

    -- Verificar que la diagonal inferior (pendiente negativa) sea segura
    -- Buscar el extremo izquierdo de la diagonal inferior
    iterColumna = columna
    iterFila = fila

    while iterColumna > 1 and iterFila > 1 do
        iterFila = iterFila - 1
        iterColumna = iterColumna - 1
    end

    -- Recorrer toda la diagonal excepto la posición marcada por los parámetros fila, columna
    while iterFila <= #tablero and iterColumna <= #tablero do
        print("iterFila = " .. iterFila .. ", iterColumna = " .. iterColumna)
        if not (iterFila == fila and iterColumna == columna) then
            if tablero[iterFila][iterColumna] == 1 then
                return false
            end
        end
        iterFila = iterFila + 1
        iterColumna = iterColumna + 1
    end

    -- Verifica que no hayan atacantes ni en sus lados, ni en sus diagonales (y en la columna)
    return true
end


function solucion(columna, tablero) 
    -- Caso base: si la solucion es la correcta
    if columna >= n then
        return true
    end 

    -- Se considera la columna actual como una posible solución y se verifica
    for i = 0, #n-1 do
        -- verifica si se puede colocar en el tablero[i][columna]
        if posicionVerdadera(i, columna) then
            
            tablero[i][columna]=1
            -- se invoca la funcion recursiva para dar solucion a las demas reinas del tablero
            if solucion(columna+1) then
                return true
            end
            
            tablero[i][columna]=0
            
        end
        i++
    end
    -- si no hay solucion la reina puede ser colocada en ninguna fila de esta columna
    return false
end

function inicializar()

    local n = 8

    tablero = {}
    for i=1, n do
        mt[i] = {}
        for j=1, n do
            mt [i] [j] = 0 
        end
    end

    letras = {"A","B","C","D","E","F","G","H"}
    
    if solucion(0, tablero)==false then
        print("No hay solucion")
        return false
    end

    imprimir(tablero, letras, n)
    
    return true
end

inicializar()

