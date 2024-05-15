iterable = {
    'casa':{
        'porta':(('maçaneta',0),34)
    },
    'carro':{
        'imposto':{
            'p':2
        },
        'gasolina':456,
    },
}

newElement = 'p'

iterable['casa'][newElement] = 1

print(iterable)