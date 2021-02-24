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
>**Figura 1** - _Estrutura de diretórios para o boot do CD_

>>``` dos
>>@echo off
>>loadlin bzImage ramdisk_size=20000 root=/dev/ram ro initrd=root.bin
>>```
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

>>``` plantuml
>>@startsalt
>>{
>>    {T
>>        + /
>>        ++ bin/
>>        ++ cdrom/
>>        ++ dev/
>>        +++ ida/
>>        +++ inet/
>>        +++ rd/
>>        ++ etc/
>>        +++ init.d/
>>        +++ j2re1.3/
>>        ++++ security/
>>        +++ menu-methods/
>>        +++ X11/
>>        ++++ app-defaults/
>>        ++++ fs/
>>        ++++ proxymngr/
>>        ++++ rstart/
>>        ++++ twm/
>>        ++++ xinit/
>>        ++++ xkb/
>>        ++++ xserver/
>>        ++++ xsm/
>>        ++ floppy/
>>        ++ initrd/
>>        ++ java/
>>        ++ lib/
>>        +++ modules/
>>        ++++ 2.2.18/
>>        ++ mnt/
>>        ++ proc/
>>        ++ sbin/
>>        ++ tmp/
>>        ++ usr/
>>        ++ var/
>>    }
>>}
>>@endsalt
>>```
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
