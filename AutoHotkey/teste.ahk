; Verifica se c:\teste.txt existe
if (not FileExist("c:\teste.txt"))
{
    ; Verifica se Notepad esta aberto
    if (not WinExist("ahk_class Notepad"))
    {
        Run Notepad
        WinWait ahk_class Notepad
    }
    else
        WinActivate ahk_class Notepad

    ; Realiza operações
    Send Hello`, world!
    Send, {enter}
    Send, {Ctrl down}s{Ctrl up}
    Send c:\teste.txt
    Send, {enter}
    Send, {Alt down}{F4}{Alt up}
}
else
    MsgBox, File c:\teste.txt exists!