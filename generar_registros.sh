#!/bin/bash

# Función para generar un código de producto aleatorio de 10 caracteres alfanuméricos
generate_random_code() {
    length=10
    characters="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    code=""
    for ((i=0; i<$length; i++)); do
        random_index=$((RANDOM % ${#characters}))
        code+=${characters:$random_index:1}
    done
    echo "$code"
}

# Generar registros aleatorios
for ((i=0; i<40000; i++)); do
    codigo=$(generate_random_code)
    cantidad=$((RANDOM % 100 + 1))  # Generar cantidad aleatoria entre 1 y 100
    echo "1"  # Opción 1: Agregar
    echo "$codigo"
    echo "$cantidad"
done
#!/bin/bash

# Función para generar un código de producto aleatorio de 10 caracteres alfanuméricos
generate_random_code() {
    length=10
    characters="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    code=""
    for ((i=0; i<$length; i++)); do
        random_index=$((RANDOM % ${#characters}))
        code+=${characters:$random_index:1}
    done
    echo "$code"
}

# Generar registros aleatorios
for ((i=0; i<40000; i++)); do
    codigo=$(generate_random_code)
    cantidad=$((RANDOM % 100 + 1))  # Generar cantidad aleatoria entre 1 y 100
    echo "1"  # Opción 1: Agregar
    echo "$codigo"
    echo "$cantidad"
done
