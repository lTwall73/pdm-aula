# principal.py
import subprocess

# Usamos o subprocess.run() para executar o arquivo conteudo.py
# capture_output=True: captura a saída do processo
# text=True: decodifica a saída como texto (string)
try:
    resultado = subprocess.run(
        ['python', 'lista.py'], #<----------- põe o nome do arquivo aqui
        capture_output=True,
        text=True,
        check=True
    )
    
    # A saída padrão (stdout) está na propriedade .stdout
    print("--- Conteúdo do lista.py ---")
    print(resultado.stdout)
    
except subprocess.CalledProcessError as e:
    # Se o conteudo.py retornar um erro, ele será capturado aqui
    print(f"Ocorreu um erro ao executar o arquivo: {e}")
    print(f"Saída de erro: {e.stderr}")