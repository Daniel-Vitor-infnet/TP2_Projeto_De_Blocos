class Node:
    def __init__(self, content):
        self.content = content
        self.next = None
        self.prev = None

class EditorDeTexto:
    def __init__(self):
        self.primeira_l = None
        self.linha_a = None  # Ponteiro C (corrente)

    #Move o ponteiro linha_a para a linha de número 'n'
    def ir_para_linha(self, n):
        if n <= 0:
            return
        
        temp = self.primeira_l
        contador = 1
        
        # Percorre a lista até achar a linha n ou chegar ao fim
        while temp and contador < n:
            temp = temp.next
            contador += 1
            
        if temp:
            self.linha_a = temp

    def comando_inserir(self, text, n=None):
        """
        Entra no modo de inserção. 
        Se 'n' for fornecido vai para a linha 'n' antes de inserir.
        """
        if n is not None:
            self.ir_para_linha(n)

        novo_no = Node(text)

        if not self.primeira_l:
            self.primeira_l = novo_no
            self.linha_a = novo_no
        else:
            # caso a inserção seja no meio do texto
            novo_no.next = self.linha_a.next
            novo_no.prev = self.linha_a
            
            if self.linha_a.next: # Se houver uma linha depois da atual, ela aponta para a nova
                self.linha_a.next.prev = novo_no
                
            self.linha_a.next = novo_no
            self.linha_a = novo_no # A linha corrente

    def imprimir(self):
        temp = self.primeira_l
        contador = 1
        print("\n--- Texto Atual ---")
        while temp:
            # Coloquei um contador de linha só para ficar melhor apresentavel
            print(f"{contador:02d} | {temp.content}")
            temp = temp.next
            contador += 1
        print("-------------------\n")
        

    # Exclui as linhas da posição i até f (Caso nada seja passoado irá excluir a linha corrente) 
    def comando_excluir(self, i=None, f=None):
        if not self.primeira_l:
            return

        # Defini quem é o primeiro e o último nó a serem excluídos
        if i is None and f is None:
            no_inicio = self.linha_a
            no_fim = self.linha_a
        else:
            # Encontra o nó inicial (i)
            no_inicio = self.primeira_l
            contador = 1
            while no_inicio and contador < i:
                no_inicio = no_inicio.next
                contador += 1
            
            if not no_inicio: return 
            
            # Encontra o nó final (f) a partir do inicial
            no_fim = no_inicio
            while no_fim and contador < f:
                if no_fim.next:
                    no_fim = no_fim.next
                contador += 1

        # Ponte entre o que vem antes de 'i' e depois de 'f'
        no_anterior = no_inicio.prev
        no_proximo = no_fim.next

        if no_anterior:
            no_anterior.next = no_proximo
        else:
            self.primeira_l = no_proximo

        if no_proximo:
            no_proximo.prev = no_anterior

        # Atualizar o ponteiro da linha corrente (linha_a)
        if no_proximo:
            self.linha_a = no_proximo
        elif no_anterior:
            self.linha_a = no_anterior
        else:
            self.linha_a = None # O texto todo foi apagado

# --- TESTANDO O CÓDIGO ---
if __name__ == "__main__":
    editor = EditorDeTexto()

    print("1. Inserindo linhas iniciais (sem passar o 'n'):")
    editor.comando_inserir('"A natureza,')
    editor.comando_inserir('dizem-nos,')
    editor.comando_inserir('(Rousseau)')
    editor.comando_inserir('Linha 4 - Excluir A')
    editor.comando_inserir('Linha 5 - Excluir B')
    editor.comando_inserir('Linha 6 - Excluir C (vai sobrar)')
    editor.imprimir()


    editor.comando_excluir(4, 5)

    editor.imprimir()