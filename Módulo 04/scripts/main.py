"""
Programa principal 
Author: Richard Brosler 
Version: 25-04-03
"""
import funcoes 
from click import clear # importando somente a função clear 
clear () # Limpa o console 
funcoes.cabecalho(colunas=50,titulo="Bem vindo!") 
funcoes.cabecalho("Olá turma, boa noite!",30) 
funcoes.cabecalho()
funcoes.cabecalho(colunas=15)
print("Fatorial de 5=",funcoes.fatorial(1000))
print("Fatorial de 5=",funcoes.fatorial_rec(5))