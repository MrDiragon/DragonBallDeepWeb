<h1 align='center'>Dragonball Z: Deep Web</h1>
 
![Banner Dragonball Z: Deep Web](https://img.ibxk.com.br/2022/05/02/02121505592216.jpg)

---

<strong><em>Alunos:</em></strong>

- Alexandre Souza
- Arthur Caio
- Carlos Kaynan
- Diego Rafael Gomes
- Guilherme Ribeiro
- Humberto Campos

## Sinopse
O jogo se passa no planeta terra após a chegada de Freeza e Majin Boo, no intuito de se vingar de Goku devido a derrotas anteriores. Eles pretendem matá-lo e posteriormente destruir a terra. Goku tem a missão de derrotar os inimigos e salvar o planeta da ameaça dessas poderosas criaturas.

## Como Iniciar o Jogo
Caso seja primeira vez iniciando o projeto, faça um `git clone` do <a href="https://github.com/MrDiragon/P1_ProjetoFinal"><em>Link do Repositório</em></a> e siga esses passos:
  - Abra a IDE (VSCode ou Pycharm) com a biblioteca do Pygame instalada, depois abra a pasta onde salvou os arquivos baixados anteriormente com a IDE, inicie o arquivo “.py” da pasta e aperte em "Run".
  - Depois disso, inicie o jogo e aproveite!
 
## Teclas de Movimentação
- Seta para cima do teclado (Movimenta o personagem para cima)
- Seta para baixo do teclado (Movimenta o personagem para baixo)
- Espaço do teclado (Atira o <a href="https://dragonball.fandom.com/pt-br/wiki/Kamehameha">Kamehameha</a> no inimigo)

## Organização do Código:
“Dragonball Z Deep Web" é um jogo essencialmente orientado a objeto, onde nos dividimos em duplas para cada dupla trabalhar em uma classe específica, otimizando o tempo de trabalho e a organização do código. Após todas as classes estarem criadas e devidamente funcionando, chamamos as funções das classes e seus devidos objetos na classe principal do Game Loop.
- `Class Game`: Classe principal onde cria o Loop do jogo e chama todas as funções necessárias para o funcionamento do código.
- `Class Inimigo`: Cria a imagem do Jogador no jogo, adiciona função a de colisão do Jogador com outras instâncias do jogo, função de movimentação.
- `Class Player`: Cria a imagem do inimigo no jogo, adiciona função a de colisão do inimigo com outras instâncias do jogo, função de respawn e movimentação, função de vida do jogador.
- `Class Tiro`: Cria imagem do tiro na mão do jogador, função de colisão com inimigo, função de respawn, e contagem de pontos.
- `Class Esfera`: Cria imagem de esfera do dragão na tela, a ocorrência dela após algumas condições, spawn das esferas e adição de vida.
- `Pasta de Imagens`: Contém as imagens a serem chamadas no código.
- `Pasta de Som`: Contém os sons que serão utilizados no jogo.

## Ferramentas e Bibliotecas:
- `import random`: é um módulo que faz parte da linguagem Python e é utilizado para gerar números pseudo-aleatórios. Também podemos selecionar os elementos de uma lista de forma aleatória ou exibir o seu resultado embaralhado.
- `import pygame`: Voltada para o desenvolvimento de games e interfaces gráficas, o Pygame fornece acesso a áudios, teclados, controles, mouses e hardwares gráficos.

## Divisão de trabalho dentro do grupo:
- Carlos Kaynan e Humberto Campos: Criação de código base sem POO, Posteriormente a incrementação da POO, Criação de slides e Documento.
- Alexandre Souza e Diego Rafael: Gerenciamento do Git, criação de telas.
- Arthur Caio e Guilherme Ribeiro: Organização de tarefas no Notion, Implementação de sons e telas.

## Conceitos que foram apresentados durante a disciplina e utilizados no projeto:
- `Condicionais`: Essenciais na colisão dos elementos, contagem de vida e pontuação. (if, elif, else).
- `Laços`: O jogo ocorre dentro de um while True para o Loop do jogo, juntamente com um For:
- `Funções`: Funções das classes que são chamadas na classe do loop.
- `Orientação a Objetos`: Essencial para divisão do trabalho e organização do código.

## Os desafios e erros enfrentados no decorrer do projeto e as lições aprendidas:
- `Qual foi o maior erro cometido durante o projeto? Como vocês lidaram com ele?`: Inicialmente tentamos copiar um código que vimos em uma vídeo aula e trabalhar a partir dele. Porém, não conseguimos compreender o mesmo, perdendo muito tempo por causa disso. A partir disso, descartamos o antigo código e decidimos começar a criar um do zero, de acordo com o que nós estudamos em diversas video aulas.
- `Qual foi o maior desafio enfrentado durante o projeto? Como vocês lidaram com ele?`: O maior desafio foi separar o que cada membro do grupo iria fazer no começo, resolvido isso, passamos boa parte do prazo estudando e implementando POO no código original. Que foi de longe a coisa mais trabalhosa e desafiadora do projeto.
- `Quais as lições aprendidas durante o projeto? `: Aprendemos a programar em equipe, coisa que era nova para a maioria dos membros dos grupos. Conhecimento de POO adquirido.




---
<p align="center">
   <> Feito pela galera do CIn <\>
</p>

---
