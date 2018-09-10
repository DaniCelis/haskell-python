sumar::[Int]->Int
sumar [ ] = 0
sumar (x:xs) = x + sumar(xs)


invertir::Ord a=>[a]->[a]
invertir [ ] = [ ]
invertir (x:xs) = (invertir xs)++[x]


igualLista:: Eq a => [a]->[a]->Bool
igualLista l1 l2 = l1 == l2


lista_ordenada::Ord a=>[a]->Bool
lista_ordenada [] = True
lista_ordenada [_] = True
lista_ordenada (x:y:xs) = (x<=y) && lista_ordenada (y:xs)


mostrar_ubicacion::Ord a=>[a]->Int->a
mostrar_ubicacion l n = l!!n


mayor::[Int]->Int
mayor (x:xs)
    | x > mayor(xs) = x
    | otherwise = mayor(xs)


contarpares::[Int]->Int
contarpares []=0
contarpares lista= length [x | x <- lista, mod x 2 ==0]


cuadrados::[Int]->[Int]
cuadrados [ ] = [ ]
cuadrados l = [x*x| x <- l]


divisible::Int->Int->Bool
divisible x y = (mod x y) ==0
divisibles::Int->[Int]
divisibles x = [y | y <-[1..x],divisible x y]
esPrimo::Int->Bool
esPrimo n = length (divisibles n) <=2

primos::Int->[Int]
primos n = [x | x <-[1..n],esPrimo x]
