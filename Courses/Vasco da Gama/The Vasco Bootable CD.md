# 1. Estrutura básica do CD

_Analisaremos alguns conceitos, que formaram a base da criação do CD._

Durante a criação deste CD muitas dúvidas surgiram, tais como: adoção de um padrão pré-existente ou criação de um próprio padrão, quais programas seriam necessários para a composição do CD, sequência que seria executada durante o boot (DOS/LINUX, LINUX/DOS ou outra), formas eficientes para a carga do sistema operacional.

Através do processo de pesquisa descobrimos que para estabelecer um padrão o processo seria complexo, pois seria necessário criar uma distribuição própria. Como a distribuição *Debian* já havia sido homologada, optamos por usar como base de trabalho o seu CD de instalação.

## Como executar o boot

Com isso em mente criou-se um impasse de como carregar o Linux, sabiamos que para a carga de um sistema operacional via CD deveria seguir o padrão **El-Torito**. Precisariamos criar um bootstrap próprio que fornecesse as funcionalidades básica exigidas pelo padrão, durante o processo de pesquisa identificamos a existências de diversas soluções para este problemas. Entre as possibilidades levantadas estavam:

1. **Boot DOS fazendo chamada ao Linux utilizando o progrma o loadlin:** Uma solução simples e eficiente cujo o único incoveniente é o de sempre haver um boot DOS (licenciamento);

1. **Boot Linux fazendo chamada DOS:** Por problemas de manipulação das interrupções do Linux esta alternativa foi descartada;

1. **Boot usando o bootstrap lilo:** Difícil de implementar o ponto de controle na mudança do sistema operacional a ser usado no momento;

1. **Boot usando o bootstrap isolinux:** Difícil de implementar o ponto de controle na mudança do sistema operacional a ser usado no momento;

Optou-se então pela primeira alternativa pois esta era mais factível para as necessidades paresentadas pelo CD. Para isso foi criada a seguinte estrutura:

>>``` plantuml
>>@startsalt
>>{
>>    {T
>>        + Structure         | Descrition
>>        + /                 | .
>>        ++ boot/            | .
>>        +++ bzImage         | (Kernel 2.2.18)
>>        +++ floppy.raw      | (Imagem de disco de boot DOS)
>>        +++ linux.bat       | (Arquivo de lote para chamada)
>>        +++ loadlin.exe     | (Programa de carga do Linux)
>>        +++ root.bin        | (Ambiente básico do Linux)
>>    }
>>}
>>@endsalt
>>```
>Figura 1 - Estrutura de diretórios para o boot do CD