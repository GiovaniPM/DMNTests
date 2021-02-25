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

>``` plantuml
>@startsalt
>{
>    {T
>        + Structure         | Descrition
>        + /                 | .
>        ++ boot/            | .
>        +++ bzImage         | (Kernel 2.2.18)
>        +++ floppy.raw      | (Imagem de disco de boot DOS)
>        +++ linux.bat       | (Arquivo de lote para chamada)
>        +++ loadlin.exe     | (Programa de carga do Linux)
>        +++ root.bin        | (Ambiente básico do Linux)
>    }
>}
>@endsalt
>```
>**Figura 1** - _Estrutura de diretórios para o boot do CD_

>``` dos
>@echo off
>loadlin bzImage ramdisk_size=20000 root=/dev/ram ro initrd=root.bin
>```
>**Figura 2** - _Conteúdo do arquivo de lote para a chamada do Linux (**Linux.bat**)_

Não abordaremos neste documento como é efetuada a decisão de qual o sistema operacional será chamado, pois dependerá da criação de um outro programa objeto de outra pesquisa.

## Qual kernel usar

Precisamos criar um kernel que suportasse as máquinas alvo bem como otimizações de performance. Dentre as otimizações criadas estão:

- compactação de file system;
- suporte a frame buffer;
- utilização de diversos ramdisks;
- suporte a loop devices.

Para isso usamos a compilação do kernel 2.2.18 aplicando o patch de suporte a EXT3.

## Como inicializar o Linux

Para a inicialização do Linux é necessário haver uma estrutura mínima, que fornece as condições necessárias para a execução do Linux. Esta estrutura é definida como um ramdisk inicial e será responsável pela hospedagem de programas, drivers e dispositivos necessários para a imediata execução do Linux. O programa de maior importância é o **Init**, que proverá uma série de funcionalidades (analagas ao **command.com** do DOS). Consideramos o **Init** como uma caixa preta, já que usaremos o do próprio CD de instalação do Debian com as funcionalidades necessárias. Poderá havers futuras customizações do **Init**, mas como fora citada anteriormente. Em nosso caso isto é dispensável. Para um melhor entendimento é aconselhável observar o **root.bin**:

>``` plantuml
>@startsalt
>{
>    {T
>        + /
>        ++ bin/
>        ++ cdrom/
>        ++ dev/
>        +++ ida/
>        +++ inet/
>        +++ rd/
>        ++ etc/
>        +++ init.d/
>        +++ j2re1.3/
>        ++++ security/
>        +++ menu-methods/
>        +++ X11/
>        ++++ app-defaults/
>        ++++ fs/
>        ++++ proxymngr/
>        ++++ rstart/
>        ++++ twm/
>        ++++ xinit/
>        ++++ xkb/
>        ++++ xserver/
>        ++++ xsm/
>        ++ floppy/
>        ++ initrd/
>        ++ java/
>        ++ lib/
>        +++ modules/
>        ++++ 2.2.18/
>        ++ mnt/
>        ++ proc/
>        ++ sbin/
>        ++ tmp/
>        ++ usr/
>        ++ var/
>    }
>}
>@endsalt
>```
>**Figura 3** - _Estrutura de **root.bin**_

Após a execução do **Init** será chamado um script de inicialização de serviços denominado **Inittab** dentro do diretório **/etc**.

>``` bash
>#/etc/inittab
>#     init(8) configuration for Debian boot-floppies Root Disk
>#
># Copyright (C) 1999,2000 Erik Andersen <andersee@debian.org>
># GPL-2
># 
># Note: Busybox init doesn't support runlevels. The runlevels field is
># completely ignored by BusyBox init. If you wnat runlevels, use sysvinit.
>#
># Format for each entry: <id>:<runlevels>:<action>:<process>
>#
># id        == tty to run on, or empty for /dev/console
># runlevels == ignored
># action    == one of sysinit, respawn, askfirst, wait, and once
># process   == program to run
>
># If this is the Linux console, and it's a vga16 frame buffer,
># force the vga palette to be reset to defaults.
>#tty1::sysinit:/etc/init.d/check_fb.sh
>
># main rc script
>null::sysinit:/etc/init.d/rcS
>
># Scriot to mount CD device
>#::sysinit:/sbin/startcd
>
># convenience shell
>#tty2::askfirst:/bin/sh
>tty2::wait:/sbin/startcd # aqui chamará próximo passo
>
>#Set uo stuff for logging
>::sysinit:/bin/dmesg > /dev/tty4
>#tty3::respawn:/usr/bin/tail -f /var/log/messages
>tty4::respawn:/usr/bin/tail -f /proc/kmsg
>
># Stuff to do before rebooting
>::ctrlaltdel:/bin/umount -a -r > /dev/null 2>&1
>::ctrlaltdel:/sbin/swapoff -a > /dev/null 2>&1
>```
>**Figura 4** - _Arquivo **Inittab**_

O principal script por nós customizado é o **startcd** localizado dentro do **/sbin**, ele é responsável pela chamada dos serviços que preverão a execução do CD.

>``` bash
>#!/bin/sh
>
>/sbin/mountcd
>/sbin/loader
>#/etc/X11/menu.sh
>/etc/X11/detect.sh
>```
>**Figura 5** - _Listagem do **startcd**_

A primeira tarefa executada será a montagem do CD, note que esta tarefa não é trivial. A montagem deve ser sensível a quanitdade de drivers existentes, e a qual unidade precisamente estará situado o CD.

>``` bash
>#!/bin/sh
>
># I could have built IDE as a loadable module but I'm lazy and I want
># to be able to use this same kernel as my routine one.
>
>mount_CD() {
>    echo Looking for the ATA CD device...
>    for i in hdc hdb hdd hda hde hdf
>    do
>      if /sbin/mount -n -r -t iso9660 /dev/$i /cdrom
>      then
>        CD_DEVICE=-$i
>            echo -e "CD found in /dev/$i device."
>          return
>      fi
>    done
>    echo CD not found
>    What do i do now!
>}
>
>mount_CD
>
>export CD_DEVICE
>
># Use instance of umount not on the CD
>#/bin/umount -n /cdrom
>```
>**Figura 6** - _Listagem do **mountcd**_

A segunda tarefa do **startcd** é chamar o loader localizado no **/sbin**, responsável pela montagem do filesysetm **java** e do **Xfree**. Por motivos de otimização optamos carregar em memória caso haja o suficiente, como segue a tabela:

>|Qtde Memória|Java|Xwin|
>|:-----|:-----|:-----|
>|< 64 Mb|CD|CD|
>|64 Mb - 127 Mb|CD|Memória|
>| > 128 Mb|Memória|Memória|
>
>**Figura 7** - _Otimizações de filesystem_

>``` bash
>#!/bin/sh
>
>if [ $1 = "-mem" ]
>then
>    #Create a ramdisk for the JVM
>    dd if=/dev/zero of=/dev/ram1 bs=1k count=36000
>    echo y | mkfs -t ext2 -m 0 /dev/ram1 36000
>    mount -t ext2 /dev/ram1 /usr/lib/j2re1.3
>    cd /usr/lib/j2re1.3
>    tar -zxvf /cdrom/java.tgz
>#    mkdir /tmp/point1
>#    mount -t ext2 -o loop -r /cdrom/jre1.3 /tp/point1
>#    cd /usr/lib/j2re1.3
>#    cp -dpR /tmp/point1/. .
>else
>    #Creaet a loopback for the JVM
>    mount -t ext2 -o loop -r /cdrom/jre1.3 /usr/lib/j2re1.3
>```
>**Figura 8** - _Listagem do **mountjava**_

>``` bash
>#!/bin/sh
>
>if [ $1 = "-mem" ]
>then
>    #Create a ramdisk for the XFree86
>    dd if=/dev/zero of=/dev/ram2 bs=1k count=101000
>    echo y | mkfs -t ext2 -m 0 /dev/ram2 101000
>    mount -t ext2 /dev/ram2 /usr/X11R6
>    cd /usr/X11R6
>    tar -zxvf /cdrom/xwin.tgz
>#    mkdir /tmp/point2
>#    mount -t ext2 -o loop -r /cdrom/Xwin_4.1 /tp/point2
>#    cd /usr/X11R6
>#    cp -dpR /tmp/point2/. .
>else
>    #Creaet a loopback for the XFree86
>    mount -t ext2 -o loop -r /cdrom/Xwin_4.1 /usr/X11R6
>```
>**Figura 9** - _Listagem do **mountXwin**_

A terceira tarefa a ser executado pelo **startcd** é a detecção e customização do ambiente gráfico através do script **detect.sh** localizado no diretório **/etc/X11**. Não existe mágica apenas recorremos ao arquivo **PCI** do diretório **/proc** e capturamos a placa de vídeo.

<!--
``` plantuml
@startuml
:makeXfile;
:/etc/X11/<driver name>;
fork
  :/etc/X11/XF86Config.previous;
fork again
  :driver name;
fork again
  :/etc/X11/XF86Config.next;
end fork
:/etc/X11/XF86Config;
@enduml
```
>**Figura 10** - _Criação do **XF86Config**_
-->

>``` plantuml
>@startuml
>frame detect {
>    agent "makeXfile" as a2
>    file "/etc/X11/<driver name>" as a1
>}
>frame mount {
>    file "/etc/X11/XF86Config.previous" as b1
>    agent "driver name" as b2
>    file "/etc/X11/XF86Config.next" as b3
>}
>file "/etc/X11/XF86Config" as c1
>a1 -[dashed]-> a2
>detect -----[bold]-> b2
>b1 -[dashed]-> b2
>b3 -[dashed]-> b2
>mount --[bold]-> c1
>@enduml
>```
>**Figura 10** - _Criação do **XF86Config**_

Por exemplo o script pegará o string identificador da placa do arquivo PCI, consultará o arquivo **video_cards.txt** localizado no diretório **/etc/X11** devolvendo o driver adequado. Caso a placa possua particularidades de hardware, haverá também um arquivo denominado com o nome do driver contendo estas particularidades.

>```dos
>Ati                                                              ati
>Cirrus                                                           cirrus
>Intel                                                            i810
>Matrox                                                           mga
>S3                                                               savage
>```
>**Figura 11** - _Listagem do **video_cards.txt**_

>```dos
>      Option         "noaccel"
>      Option         "no_bitblt"
>```
>**Figura 11** - _Listagem do arquivo de particularidades **cirrus.txt**_

>``` bash
>Section "Module"
>    Load        "dbe"                      # Double buffer extension
>    Subsection  "extmod"
>      Option    "omit xfree86-dg"          # don't initialise the DGA extension
>    EndSubSection
>    Load        "type1"
>    Load        "freetype"
>EndSection
>
>Section "Files"
>    RGbPath     "/usr/X11R6/lib/X11/rgb"
>    FontPath    "/usr/X11R6/lib/X11/fonts/local/"
>    FontPath    "/usr/X11R6/lib/X11/fonts/misc/"
>    FontPath    "/usr/X11R6/lib/X11/fonts/75dpi/:unscaled"
>    FontPath    "/usr/X11R6/lib/X11/fonts/100dpi/:unscaled"
>    FontPath    "/usr/X11R6/lib/X11/fonts/Type1/"
>    FontPath    "/usr/X11R6/lib/X11/fonts/Speedo/"
>    FontPath    "/usr/X11R6/lib/X11/fonts/75dpi/"
>    FontPath    "/usr/X11R6/lib/X11/fonts/100dpi/"
>EndSection
>
>Section "InputDevice"
>    Identifier "Keyboard1"
>    Driver     "Keyboard"
>    Option "AutoRepeat" "500 30"
>    Option "XkbRules" "xfree86"
>    Option "XkbModel" "pc101"
>    Option "Xkblayout" "us"
>EndSection
>
>Section "InputDevice"
>    Identifier "Mouse1"
>    Driver     "Mouse"
>    Option "Protocol" "PS/2"
>    Option "Device"   "/dev/psaux"
>EndSection
>
>Section "Monitor"
>    Identifier  "My Monitor"
>    HorizSync   31.5, 35.15, 35.5
>    VertRefresh 50-70
>EndSection
>
>Section "Device"
>    Identifier "Standard VGA"
>    VendorName "Unknown" 
>    BoardName  "Unknown" 
>    Driver     "vga"
>EndSection
>
>Section "Device"
>    Identifier "Video_Card"
>```
>**Figura 13** - _Listagem **XF86Config.previous**_

>``` bash
>EndSection
>
>Section "Screen"
>    Identifier  "Screen 1"
>    Device      "Video_Card"
>    Monitor     "My Monitor"
>    DefaultDepth 8
>    Subsection "Display"
>        Depth       8
>        Modes       "800x600" "640x480" "640x400"
>        ViewPort    0 0
>    EndSubsection
>EndSection
>
>Section "Serverlayout"
>    Identifier "Video_Card"
>    Screen "Screen 1"
>    InputDevice "Mouse1" "CorePointer"
>    InputDevice "Keyboard1" "CoreKeyboard"
>EndSection
>```
>**Figura 14** - _Listagem **XF86Config.next**_

>``` bash
>#!/bin/sh
>
>cat /proc/pci | grep VGA > /tmp/hp_0005
>tail /tmp/hp_0005 > /tmp/hp_0006
>colrm 1 31 < /tmp/hp_0006 > /tmp/hp_0005
>colrm 51 < /etc/X11/video_cards.txt > /tmp/hp_0006
>_status="no"
>for i in `cat /tmp/hp_0006`
>do
>    grep -i $i /tmp/hp_0005 > /tmp/hp_0007
>    _card=`colrm 2 < /tmp/hp_0007`
>    if [ "x"$_card != "x" ]
>    then
>      echo "Card found: " $i
>      /etc/X11/makeXfile.sh $i
>      _status="ok"
>    fi
>    done
>if [ $_status = "no" ]
>then
>#    /etc/X11/menu.sh
>    co /etc/X11/XF86Config.framebufer /etc/X11/XF86Config
>fi
>win
>```
>**Figura 15** - _Listagem **detect.sh**_

>``` bash
>#!/bin/sh
>/etc/X11/video.sh "$1";
>cat /etc/X11/XF86Config.previous                    >  /etc/X11/XF86Config;
>echo -e "    Driver      \ ""`cat /tmp/hp_0003`"\"" >> /etc/X11/XF86Config;
>_file_card="/etc/X11/"`cat /tmp/hp_0003".txt"
>if [ -f $_file_card ]
>then
>      cat $_file_card                               >> /etc/X11/XF86Config;
>fi
>cat /etc/X11/XF86Config.next                        >> /etc/X11/XF86Config;
>```
>**Figura 16** - _Listagem **makeXfile.sh**_

>``` bash
>#!/bin/sh
>
>export PATH=.:/usr/X11R6/bin:/usr/X11R6/lib:$PATH
>startx
>```
>**Figura 17** - _Listagem **win**_

A primeira tarefa do ambiente gráfico é ler o arquivo das configurações iniciais do ambiente localizado em **/etc/X11/xinit** denominado **xinitrc**.

>``` bash
>#!/bin/sh
># $Xorg: xinitrc.cpp,v 1.3 2000/08/17 19:54:30 cpqbld Exp $
>
>userresources=$HOME/.Xresources
>usermodmap=$HOME/.Xmodmap
>sysresources=/usr/X11R6/lib/X11/xinit/.Xresouerces
>sysmodmap=/usr/X11R6/lib/X11/xinit/.Xmodmap
>
># merge in defaults and keymaps
>
>if [ -f $sysresources ]; then
>    xrdb -merge $sysresources
>fi
>
>if [ -f $sysmodmap ]; then
>    xmodmap $sysmodmap
>fi
>
>if [ -f $userresources ]; then
>    xrdb -merge $userresources
>fi
>
>if [ -f $usermodmap ]; then
>    xmodmap $usermodmap
>fi
>
>cd /cdrom/hpgui
>oroborus &
>java HPGUI
>```
>**Figura 18** - _Listagem **xinitrc**_

><br>
>
>![18a](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/Vasco%20da%20Gama/Images/18a.svg)
>
>**Figura 19.a** - _BOOT SEQUENCE_
>
>![18b](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/Vasco%20da%20Gama/Images/18b.svg)
>
>**Figura 19.b** - _ROOT.BIN_
>
>![18c](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/Vasco%20da%20Gama/Images/18c.svg)
>
>**Figura 19.c** - _MOUNT.GRAPH_

# 2. Um pouco de Teoria

_Explicaremos agora algumas premissas usadas na confecção do CD._

O sistema operacional Linux está baseado na filosofia Unix, portanto qualquer pessoa que tenha trabalhado com algum sistema operacional Unix já terá todo o embassamento necessário. O Linux herdou do Unix o sistema de arquivos e a forma com que são gerenciados os dispositivos.

Um dos conceitos muito usado em nosso trabalho foi o filesystem. O filesystem empacota arquivos, podendo estar localizado nos mais diversos dispositivos e facilmente acessado mediante montagem. Como este pacote é enxergado pelo sistema operacional como apenas um único arquivo, podemos colocando dentro de um CD, floppy, Zip drive ou até mesmo na memória.

><br>
>
>![20](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/Vasco%20da%20Gama/Images/20.svg)
>
>**Figura 20** - _Como o Linux manipul filesystem_

## Formas otimizadas de armazenamento

O grande gargâlo de performance está localizado no I/O de dispositivo, portanto testamos soluções alternativas na tentativ de otimizar o desempenho. Dentre as otimizações cito:

- **Montagem de filesystem diretamente do CD**: Um solução clássica, mas mostrou-se problemática pelo fato de honerar muito tempo (cerca de 3 minutos).

>```bash
>mount -o loop -t ext2 -r /cdrom/jre1.3 /usr/lib/j2re1.3
>```
>**Figura 21** - _Montando um filesystem do CD_

- **Montagem de filesystem na memória**: Com essa solução tentamos reduzir o tempo de I/O, pois ao invés de fazer um acesso direto ao CD descompactamos um único aruivo diretaamente n memória do computador. Como o CD deve ser genérico devemos possuir os filesystems duplicados (versões: tar e filesystem)

>```bash
>dd if=/dev/zero of=/dev/ram1 bs=1k count=36000
>echo y | mkfs -t ext2 -m 0 /dev/ram1 36000
>mount -t ext2 /dev/ram1 /usr/lib/j2re1.3
>cd /usr/lib/j2re1.3
>tar -zxvf /cdrom/java.tgz
>```
>**Figura 22** - _Montando um filesystem do memória_

><br>
>
>![23](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/Vasco%20da%20Gama/Images/23.svg)
>
>**Figura 23** - _Filesystem em memória_

- **Montagem de filesystem compactado diretamente do CD**: Uma sofisticação da primeria alternativa, acrescendo o suporte a compactação de filesystem (**EXT3**). Esta compactação deve ser suportada pelo kernel, mediante aplicação do pacth. Esta solução é tão eficiente quanto a anterior, precisando apenas uam vcersão do filesystem. Optamos por esta solução.

>```bash
>mount -o loop -t ext2 -r /cdrom/jre1.3 /usr/lib/j2re1.3
>```
>**Figura 24** - _Montando um filesystem compactado do CD_

## Compactando um flesystem

Para compactar um filesystem é necessário que o kernel possua suporte adequado. A compactação é realizada mediante a troca do atributo de compactação de um arquivo ou diretório.

>```bash
>chattr -R +c /java/*
>```
>**Figura 25** - _Compactando o diretório java_

Cuidado ao manipular arquivos compactados, pois ao transferi-los para uma área não compactada eles automaticamente serão expandidos. Mesmo se copiarmos para uma área compactada, durante o processo de cópia ele será descompactado em memória e recompactado na nova área.

><br>
>
>![26](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/Vasco%20da%20Gama/Images/26.svg)
>
>**Figura 26** - _Transferindo arquivo de área_

## Um drive de vídeo genérico

Para ter total controle e a previsibilidade desejada, desenvolvemos um detector de placaa de vídeo (com suporte as placaas conhecidas pelos nossos servidores). Apesar deste detector funcionar a contento, devemos também fornecedor uma alternativa genérica mesmo que essa não seja tão eficiente. Optamos pelo uso do driver vesa, o qual suporta uma grande quantidade de placas (com suporte ao chipset vesa).

Contudo devemos ressaltar que mesmo assim algumas placas de vídeo podeão não funcionar, neste caso deverá ser atualizado o arquivo **video_cards.txt** localizado em **/etc/X11** com a placa e seu respectivo driver.

# 3. Como criar um CD

_Explicaremos agora em linhas gerais a criação do CD._

Primeiramente é aconselhavél que você obtenha o ambiente de criação. A forma mais fácil disto é conseguindo o próprio CD, seguindo os seguintes passos:

1. Você deverá estar no Linux;
1. Deverá possuir no mínimo 300 Mb disponíveis;
1. Criar um diretório denominado **/ambiente**;
1. Criar o diretório **/ambiente/initrd**;
1. Criar o diretório **/ambiente/struct**;
1. Executar os seguintes comandos para popular o diretório **/ambiente/initrd**:
>```bash
>mkdir /tmp/temp1
>cp /cdrom/root.bin /tmp/.
>gunzip -S .bin /temp/root.bin
>mount -o loop -t ext2 /tmps/root /tmp/temp1
>cd /temp/temp1
>cp -dpR . /ambiente/initrd/.
>umount /temp/temp1
>```
>**Figura 27** - _Populando o initrd_
7. Executar os seguintes comandos para popular o diretório **/ambiente/struct**:
>```bash
>cd /cdrom
>cp -dpR . /ambiente/struct/.
>```
>**Figura 28** - _Populando o struct_

Com isso o ambiente de criação do CD estará preparada.

Neste ponto teremos todo o suporte necessário a criação do CD, podemos incluir, excluir ou alterar qualquer componente do CD. Vale lembrar que o diretório **/ambiente/initrd** é responsável pela geração do nosso **ROOT.BIN**, e o diretório **/ambiente/struct** pela geração da imagem do CD.

## Gerando um CD

Vale lembrar que qualquer alteração implica diretamente no funcionamento do CD, portando cuidado e bom senso é uma boa política. Chegamos agora ao momento de criar o nosso CD, para isso executaremos os seguitnes comandos:

>```bash
>cd /ambiente/struct/boot
>mkdir /tmp/temp2
>dd if=/dev/zero of=root count=18000 bs=1k
>echo y | mkfs -t ext2 root
>mount -t ext2 -o loop root /tmp/temp2
>cp -dpR /ambiente/initrd/. /temp/temp2/.
>umount /tmp/temp2
>gzip -S .bin root
>cd /ambiente/struct
>mkisofs -R -b boot/floppy.raw -l -c boot/isolinux.boot ./ > cd.iso
>```
>**Figura 29** - _Criando o CD_

Notem que o parâmetro **count** deverá ser superior ao tamanho do diretório **/ambiente/initrd**, aconselho que haja folga de 3000 para o **/tmp** do CD.