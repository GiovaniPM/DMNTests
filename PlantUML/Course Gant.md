# required metadata

title: [Building Gant diagrams with PlantUML]
description: [How build Gant diagram with scripting PlantUML tool.]
author: [https://github.com/GiovaniPM]
manager: Giovani Perotto Mesquita
ms.date: 1/20/2021
ms.topic: article
ms.prod: 
ms.service: 
ms.technology: 

# Building Gant diagrams with [PlantUML](https://plantuml.com/sitemap)

[![PlantUML 1.2020.23](https://img.shields.io/badge/PlantUML-1.2020.23-brightgreen.svg)](https://plantuml.com/)
[![Creole 1.00](https://img.shields.io/badge/Creole-1.00-brightgreen.svg)](https://web.archive.org/web/20190417093012/http://www.wikicreole.org/wiki/Home)
[![Graphviz 2.44.1.20201124](https://img.shields.io/badge/Graphviz-2.44.1.20201124-brightgreen.svg)](https://graphviz.org/)
<br>Try install using:<br>
[![Chocolatey 0.10.15](https://img.shields.io/badge/Chocolatey-0.10.15-brightgreen.svg)](https://chocolatey.org/install)

## Language specification

- Light [Creole](https://plantuml.com/creole) engine syntax;
- [Common PlantUML commands](https://plantuml.com/commons);
- [Gant PlantUML standards](https://plantuml.com/gantt-diagram)
- [Graphviz](https://graphviz.org/)

## Gant theme customization

```CSS
<style>

  ganttDiagram {

  	task {
  		...
  	}

  	milestone {
  		...
  	}

  	note {
  		...
  	}

  }

  footer {
   ...
  }

  title {
    ...
  }

  legend {
   ...
  }

  caption {
    ...
  }

</style>

skinparam ...
```
- **style** - Looks like CSS format
  - **ganttDiagram**
    - **task**
      - **FontName** *fontname*
      - **FontColor** *[color](https://www.w3.org/TR/css-color-4/#named-colors)*
      - **FontSize** *size*
      - **FontStyle** <ins>(bold|italics|monospaced|stroked|underlined)</ins>
      - **BackGroundColor** *[color](https://www.w3.org/TR/css-color-4/#named-colors)*
      - **LineColor** *[color](https://www.w3.org/TR/css-color-4/#named-colors)*
  	- **milestone**
  		- **FontColor** *[color](https://www.w3.org/TR/css-color-4/#named-colors)*
  		- **FontSize** *size*
  		- **FontStyle** <ins>(bold|italics|monospaced|stroked|underlined)</ins>
  		- **BackGroundColor** *[color](https://www.w3.org/TR/css-color-4/#named-colors)*
  		- **LineColor** *[color](https://www.w3.org/TR/css-color-4/#named-colors)*
  	- **note**
      - **FontColor** *[color](https://www.w3.org/TR/css-color-4/#named-colors)*
      - **FontSize** *size*
      - **LineColor** *[color](https://www.w3.org/TR/css-color-4/#named-colors)*
      - **BackGroundColor** *[color](https://www.w3.org/TR/css-color-4/#named-colors)*
  - **footer**
    - **HorizontalAlignment** <ins>(left|center|right)</ins>
  - **title**
    - **FontColor** *[color](https://www.w3.org/TR/css-color-4/#named-colors)*
    - **FontSize** *size*
    - **FontStyle** <ins>(bold|italics|monospaced|stroked|underlined)</ins>
    - **HorizontalAlignment** <ins>(left|center|right)</ins>
  - **legend**
    - **FontSize** *size*
    - **BackGroundColor** *[color](https://www.w3.org/TR/css-color-4/#named-colors)*
    - **Margin** *number*
    - **Padding** *number*
  - **caption**
    - **FontSize** *size*
- **skinparam** - Parameters
    - **footerFontColor** *[color](https://www.w3.org/TR/css-color-4/#named-colors)*
    - **footerFontSize** *size*
    - **footerFontStyle** <ins>(bold|italics|monospaced|stroked|underlined)</ins>
    - **titleBackgroundColor** *[color](https://www.w3.org/TR/css-color-4/#named-colors)*
    - **titleBorderColor** *[color](https://www.w3.org/TR/css-color-4/#named-colors)*
    - **titleBorderRoundCorner** *number*
    - **titleBorderThickness** *number*

<div align="center">:star2:</div>

## Project initialization

- **title**<br>
Defines the title of Gant graph, to be showed above the graph.
>**title** *string*
>- - -
> ex.:<br>
>    title My first\nProject<br>

|Before|After|
| :----: | :----: |
| ![before](http://www.plantuml.com/plantuml/png/SoWkIImgIK_CAodXAYZApqfDBb402nKhb6IaAXWP61dg6u0GbqDgNWfO7G00) | ![after](http://www.plantuml.com/plantuml/png/SoWkIImgIK_CAodXAiaioKbLyArKICiiAYw9oIieoizAJIxXWj8AOAN52YKPgGf61aQ6-WOWnEMGcfS2rWy0) |
- - -
- **footer**<br>
Defines the footer message, to be showed under the graph.
>**footer** *string*
>- - -
>ex.:<br>
>    footer Giovani Perotto Mesquita\n18/01/2011 - 13:01<br>

|Before|After|
| :----: | :----: |
| ![before](http://www.plantuml.com/plantuml/png/SoWkIImgIK_CAodXAYZApqfDBb402nKhb6IaAXWP61dg6u0GbqDgNWfO7G00) | ![after](http://www.plantuml.com/plantuml/png/7Son3G8n30NGFbFy1L3iq22gwwYG680c0WEXiC7vC3_Yf5U_PR8dxzt9SekW9GuZljq7JfP11eustv_1VdRTLT7QH1KRw7OlMbuPJxiGQpF1Xw59qof_PJ6_hlSF) |
- - -
- **scale**<br>
Defines the start scale, to be showed. Useful when you need print, or show the graph.
>**scale** *factor*<br>
>or <br>
>**scale** *fraction*<br>
>or <br>
>**scale** *number* **width**<br>
>or <br>
>**scale** *number* **height**<br>
>or <br>
>**scale** _number_**\***_number_<br>
>or <br>
>**scale max** *number* **width**<br>
>or <br>
>**scale max** *number* **height**<br>
>plantuml<br>
>- - -
>ex.:<br>
>    scale 1.5<br>
>    scale 2/3<br>
>    scale 200 width<br>
>    scale 200 height<br>
>    scale 200*100<br>
>    scale max 300*200<br>
>    scale max 1024 width<br>
>    scale max 800 height<br>

|Before|After|
| :----: | :----: |
| ![before](http://www.plantuml.com/plantuml/png/SoWkIImgIK_CAodXAYZApqfDBb402nKhb6IaAXWP61dg6u0GbqDgNWfO7G00) | ![after](http://www.plantuml.com/plantuml/png/SoWkIImgIK_CAodXAavEp4bLCDGpvIeeoizAJIvH04iMAvHaf2eO6HWPwXk049T3QbuAM0S0) |
- - -
- **hide**<br>
Hides the bottom time information under the graph, does not affect the time information on the top.
>**hide footbox**
>- - -
>ex.:<br>
>    hide footbox<br>

|Before|After|
| :----: | :----: |
| ![before](http://www.plantuml.com/plantuml/png/SoWkIImgIK_CAodXAYZApqfDBb402nKhb6IaAXWP61dg6u0GbqDgNWfO7G00) | ![after](http://www.plantuml.com/plantuml/png/SoWkIImgIK_CAodXoiXCILL8oyylISglu2eeoizAJIvH0CiNAvHaf2eO6HWPwXk049T3QbuAM1C0) |
- - -
- **printscale**<br>
Useful for condesing the Gant graph timeline, useful for large projects.
>**printscale** <ins>(diary|weekly|montly)</ins><br>
>- - -
>ex.:<br>
>    printscale weekly<br>

|Before|After|
| :----: | :----: |
| ![before](http://www.plantuml.com/plantuml/png/SoWkIImgIK_CAodXKYyeoimhAKvEp4bLoCtFAyd8gUGgAChFIaqkKG0hArOeoKXLC38mCjGt026kwBJCt5Ye75JSID_80YgUMQoGd9-JNvIQef2Pfr2UaLcIgWyceVAfUIaekXo00c2N0000) | ![after](http://www.plantuml.com/plantuml/png/SoWkIImgIK_CAodXAYZAp2ifJaxCILN8pSyhoSYf10hbPwKcboY0LHKhb6IaAXWP61dg6u0GLtHQPcuiL0ugRgHlP04LponMICxFoIzAJL78p5CepyWiITK7ar3vrBmK55qEG06mGm00) |
- - -
- **project**<br>
Defines when the project starts.
>**project starts the** *date*<br>
>- - -
>ex.:<br>
>    project starts the 2021/01/01<br>

|Before|After|
| :----: | :----: |
| | ![after](http://www.plantuml.com/plantuml/png/SoWkIImgIK_CAodXKYyeoimhAKvEp4bLoCtFAyd8gUGgAChFIaqkKG0hArOeoKXLC38mCjGt026kwBJCt5Ye75JSID_80YgUMQoGd9-JNvIQef2Pfr2UaLcIgWyceVAfUIaekXo00c2N0000) |
- - -
- **caption**<br>
Defines the graph caption, useful when need export to a document.
>**caption** *description*
>- - -
>ex.:<br>
>    caption figure 1<br>

|||
| :----: | :----: |
|Before| ![before](http://www.plantuml.com/plantuml/png/SoWkIImgIK_CAodXKYyeoimhAKvEp4bLoCtFAyd8gUGgAChFIaqkKG0hArOeoKXLC38mCjGt026kwBJCt5Ye75JSID_80YgUMQoGd9-JNvIQef2Pfr2UaLcIgWyceVAfUIaekXo00c2N0000) |
|After| ![after](http://www.plantuml.com/plantuml/png/SoWkIImgIK_CAodXIauiACdCprD8oqmlBKfKCEGgAChFIaqkKG2hALOeoKXLC38mCjGt026kwBJCt5Ye75JSID_80YgUMQoGd9-JNvIQef2Pfr2UaLcIgWyceVAfUIaekXo00c1d0000) |
- - -
- **today**<br>
Defines the current day to be showed in the graph.
>**today is** *date* **and is colored in** *[color](https://www.w3.org/TR/css-color-4/#named-colors)*<br>
>or<br>
>**today is** *day(s)* **days after start and is colored in** *[color](https://www.w3.org/TR/css-color-4/#named-colors)*
>- - -
>ex.:<br>
>    today is 2021/01/20 and is colored in Yellow<br>
>or<br>
>    today is 14 days after start and is colored in Yellow<br>

|||
| :----: | :----: |
|Before| ![before](http://www.plantuml.com/plantuml/png/SoWkIImgIK_CAodXKYyeoimhAKvEp4bLoCtFAyd8gUGgAChFIaqkKG0hArOeoKXLC38mCjGt026kwBJCt5Ye75JSID_80YgUMQoGd9-JNvIQef2Pfr2UaLcIgWyceVAfUIaekXo00c2N0000) |
|After| ![after](http://www.plantuml.com/plantuml/png/LOv12WCX34NtdY8tKBFgSgvHIXSofXsBDKK_3Brzfo83Ra9uZnUoD8IAPoY0WSRmfTI87Nlhl6L7eSG_MJLhbMCjT9MSTJUVgYzPGRrlX4tEp7bpUwJtVRZ1sV9byFdWlYM8xNDuAN6gbWFq5ty0) |

<div align="center">:star2:</div>

## Comments

- **comment**<br>
Defines a line comment in the graph script, do not affect the graph showed.
>**'** *comment*
>- - -
>ex.:<br>
>    ' Comentary<br>

<div align="center">:star2:</div>

## Legends

- **legend**<br>
Defines a legend.
>**legend** (left|right|top|bottom|center)<br>
>  ...<br>
>**endlegend**<br>
>- - -
>ex.:<br>
>    legend right<br>
>      Short<br>
>      legend<br>
>    endlegend<br>

|||
| :----: | :----: |
|Before| ![before](http://www.plantuml.com/plantuml/png/SoWkIImgIK_CAodXKYyeoimhAKvEp4bLoCtFAyd8gUGgAChFIaqkKG0hArOeoKXLC38mCjGt026kwBJCt5Ye75JSID_80YgUMQoGd9-JNvIQef2Pfr2UaLcIgWyceVAfUIaekXo00c2N0000) |
|After| ![after](http://www.plantuml.com/plantuml/png/LOwn3i8m34JtViNzGKecnlu38sAeMfCObGGvblXzZEMbfoZ9lPDFNeQkecLjgXDC1nLgEuHBDU2wrIxnZzYDlU4-qb-qARngG2iXp_cIvl-Pxaz-Fo8BdbE-1kU1hHzTQ0StV2ih9RyZj_xJr6B0j_q1) |

<div align="center">:star2:</div>

## Coloring columns date

- **colored**<br>
Useful to make in evidence some columns in the graph.
>*date* **is colored in** *[color](https://www.w3.org/TR/css-color-4/#named-colors)*<br>
>or<br>
>*date* **to** *date* **are colored in** *[color](https://www.w3.org/TR/css-color-4/#named-colors)*<br>
>- - -
>ex.:<br>
>    2021/01/01 is colored in lightblue<br>
>    2021/01/01 to 2021/01/10 are colored in lightblue<br>

|||
| :----: | :----: |
|Before| ![before](http://www.plantuml.com/plantuml/png/SoWkIImgIK_CAodXKYyeoimhAKvEp4bLoCtFAyd8gUGgAChFIaqkKG0hArOeoKXLC38mCjGt026kwBJCt5Ye75JSID_80YgUMQoGd9-JNvIQef2Pfr2UaLcIgWyceVAfUIaekXo00c2N0000) |
|After| ![after](http://www.plantuml.com/plantuml/png/LOv13i8W44NtdEBV0ChAPUzXN60xbZ481hxn-YgsqIQJIURzpCiV6qFb4Z9flFE3TPy12xPhS0XLC9LKgipGZAHBv3aznDnhkSf4T4a3e-0dCSUBtavRzkNU-iFAjVqxdr4fjkyrbpplliOtw3rV) |

<div align="center">:star2:</div>

## Sprites

- **user sprite**<br>
Useful to put some image in the graph.
>**sprite $**_name_ **[**_size_**]** _sprite-code_
>- - -
>ex.:<br>
>    sprite $printer [15x15/8z] NOtH3W0W208HxFz_kMAhj7lHWpa1XC716sz0Pq4MVPEWfBHIuxP3L6kbTcizR8tAhzaqFvXwvFfPEqm0<br>

|||
| :----: | :----: |
|Before| ![before](http://www.plantuml.com/plantuml/png/SoWkIImgIK_CAodXKYyeoimhAKvEp4bLoCtFAyd8gUGgAChFIaqkKG0hArOeoKXLC38mCjGt026kwBJCt5Ye75JSID_80YgUMQoGd9-JNvIQef2Pfr2UaLcIgWyceVAfUIaekXo00c2N0000) |
|After| ![after](http://www.plantuml.com/plantuml/png/LO_VIyCm4CVVyrVSW-zDChVrGMHJLYeuBI9sC8R4BbsoTMcRd5l9NsyiyK4uxhZFb_lnNJWK5W_281BNMOqIRa8nA2risNHWqoJrEtXvnNnIqfBJD1yo_tbQBzLntkHb9zZcSSvcpjEYlrr_5AkoViYVleTYyZmxVRrNsh-bk5HUzDbbSxraTR7gpvGqyY3Ddjpz7RideOL8EziUPOKm_kO0bGHEEKleRv1jhS-xg4NE4vv6hXrKRTDQkGTjuAg2esJCKG_x_qqj0XZj_m00) |

<div align="center">:star2:</div>

## Close days

- **closed**<br>
Defines the days which not be used on the graph.
><ins>(sunday|monday|tuesday|wednesday|thursday|friday|saturday)</ins> **are closed**<br>
>or<br>
>*date* **is closed**<br>
>or<br>
>*date* to *date* **are closed**<br>
>- - -
>ex.:<br>
>    saturday are closed<br>
>    sunday are closed<br>
>    2021/01/01 is closed<br>
>    2021/01/04 to 2021/01/08 are closed<br>

|||
| :----: | :----: |
|before| ![before](http://www.plantuml.com/plantuml/png/SoWkIImgIK_CAodXKYyeoimhAKvEp4bLoCtFAyd8gUGgAChFIaqkKG0hArOeoKXLC38mCjGt026kwBJCt5Ye75JSID_80YgUMQoGd9-JNvIQef2Pfr2UaLcIgWyceVAfUIaekXo00c2N0000) |
|after| ![after](http://www.plantuml.com/plantuml/png/ROzH2i8m38RVTuh_1fl5Xptk7k93MAEhp4QI3F7sQgiuOL0A-Jxo9ndCIVrCsRq102DVDD83f8nn5kDO-P8tQEZ2hktU3yasnHuklwfV1znKBZmwoWO6dtYLrnnEwNhykif36_hAopIPHJaYPTodvDoM_-Cvnx-kuGNAaKy0) |

<div align="center">:star2:</div>

## Separators

- **-- ... --**<br>
Defines separators in the graph, useful to segregade phases, sectors, groups or others.
>**--** *name* **--**
>- - -
>ex.:<br>
>    -- Phase One --<br>

|||
| :----: | :----: |
|before| ![before](http://www.plantuml.com/plantuml/png/SoWkIImgIK_CAodXKYyeoimhAKvEp4bLoCtFAyd8gUGgAChFIaqkKG0hArOeoKXLC38mCjGt026kwBJCt5Ye75JSID_80YgUMQoGd9-JNvIQef2Pfr2UaLcIgWyceVAfUIaekXo00c2N0000) |
|after| ![after](http://www.plantuml.com/plantuml/png/SoWkIImgIK_CAodXqjLL2CX8B4vLyCzBLT3LvIeeoizAJIvH02ifLYZ9I5KmCZ0or3S08QxejCpSMAWSLDn8tyW2AfvPh92SdvDVb9gYa9cdK9wHMPAg3oQXygbvAIYw7802O5S00000) |

<div align="center">:star2:</div>

## Tasks

- **task**<br>
Defines the graph tasks.
    - **dinamic**<br>
    These tasks will be sequenced autocmatly using the project starts and the task flow.
    >[*taskname*] **lasts** *day(s)* **days**
    >- - -
    >ex.:<br>
    >    [PlantUML1] lasts 13 days<br>
|||
| :----: | :----: |
|before| ![before](http://www.plantuml.com/plantuml/png/SoWkIImgIK_CAodXKYyeoimhAKvEp4bLoCtFAyd8gUGgAChFIaqkKG0hArOeoKXLC38mCjGt026kwBJCt5Ye75JSID_80YgUMQoGd9-JNvIQef2Pfr2UaLcIgWyceVAfUIaekXo00c2N0000) |
|after| ![after](http://www.plantuml.com/plantuml/png/LOwn3W8X343tVaL_W73WudWVeF4MfyiDvAY2GJ2qYV7lHS9YqdHupNlfpEAgt5qMWLSj3ze5EsAKG6WdQ_Jq6m2bS0cE2I-PK2bObzIqw_baDaoEcs4EwDs70TPRV6wZCnfMs-FWaN4lgLJo63E-GnJIVOyxPVzdpGtq3xy0) |
    - **fixed**<br>
    These tasks have a fixed beginning and end.
    >[*taskname*] **starts** *date*<br>
    >[*taskname*] **ends** *date*
    ```plantuml
    ex.:
        [PlantUML1] starts 2021/01/18
        [PlantUML1] ends 2021/02/12
    ```
- - -
- **colored**<br>
Defines the task line and it background colors.
>[*taskname*] **is colored in** *[color](https://www.w3.org/TR/css-color-4/#named-colors)* **/** *[color](https://www.w3.org/TR/ss-color-4#named-colors)*<br>
```plantuml
ex.:
    [PlantUML1] is colored in Red/Red
```
- - -
- **completed**<br>
Defines how much progress occur in the task, the percent will be showed in backgroud color.
>[*taskname*] **is** *%* **completed**
```plantuml
ex.:
    [PlanUML1] is 70% completed
```
- - -
- **links**<br>
Useful to redirect from the task to out of the graph.
>[*taskname*] **links to** [[*link*]]
```plantuml
ex.:
    [PlantUML1] links to [[http://plantuml.com]]
```
- - -
- **resource**<br>
Defines who will do the task and how much effort will be necessary. Under the graph wil be showed the resources and how nuch allocation used.
>[*taskname*] **on {** *user* **:** *%* **} lasts** *day(s)* **days**
```plantuml
ex.:
    [PlantUML1] on {User1:50}{User2:50} lasts 6 days
```
- - -
- **pause**<br>
Defines a pause in the task, there is a semantic difference between "pause" and "closed days". "Pause" denotes a task suspension, in the other way "closed days" inform the date is not available to work in the whole project.
>[*taskname*] **pause on** <ins>(sunday|monday|tuesday|wednesday|thursday|friday|saturday)</ins><br>
>or<br>
>[*taskname*] **pause on** *date*
```plantuml
ex.:
    [PlantUML1] pauses on monday
or
    [PlantUML1] pauses on 2021/01/12
```
- - -
- **note**<br>
Defines a note to be showed under the task, useful to bring more information.
>**note bottom**<br>
>*...*<br>
>**end note**
```plantuml
ex.:
    note bottom
      memo1 ...
      memo2 ...
      explanations1 ...
      explanations2 ...
    end note
```

<div align="center">:star2:</div>

## Flows

- **link**<br>
Defines which task will succeded after other.
>[*taskname*] **starts at** [*taskname*]**'s end**<br>
>or<br>
>[*taskname*] **starts at** [*taskname*]**'s end with** *[color](https://www.w3.org/TR/css-color-4/#named-colors)* <ins>(bold|dashed|dotted)</ins> **link**
```plantuml
ex.:
    [PlantUML2] starts at [PlantUML1]'s end
or
    [PlantUML2] starts at [PlantUML1]'s end with red bold link
```

<div align="center">:star2:</div>

## Milestones

- **milestone**<br>
Defines gant milestones.
>[*milestonename*] **happens at** [*taskname*]**'s end**
```plantuml
ex.:
    [Milestone1] happens at [PlantUML1]'s end
```

<div align="center">:star:</div>
<div align="center">:star::star:</div>

# Example

## Image

```plantuml
@startgantt
<style>

  ganttDiagram {

  	task {
  		FontName Courrier
  		FontColor black
  		FontSize 12
  		FontStyle bold
  		BackGroundColor Blue
  		LineColor blue
  	}

  	milestone {
  		FontColor blue
  		FontSize 12
  		FontStyle italic
  		BackGroundColor gold
  		LineColor red
  	}

  	note {
  		FontColor DarkGreen
  		FontSize 10
  		LineColor lightgreen
        BackGroundColor orange\yellow
  	}

  }

  footer {
    HorizontalAlignment right
  }

  title {
    FontColor black
    FontSize 40
    FontStyle italic
    HorizontalAlignment center
  }

</style>

skinparam footerFontColor blue
skinparam footerFontSize 10
skinparam footerFontStyle italic
'skinparam titleBackgroundColor Aqua-CadetBlue
'skinparam titleBorderColor blue
'skinparam titleBorderRoundCorner 15
'skinparam titleBorderThickness 2

' sprites
sprite $printer [15x15/8z] NOtH3W0W208HxFz_kMAhj7lHWpa1XC716sz0Pq4MVPEWfBHIuxP3L6kbTcizR8tAhzaqFvXwvFfPEqm0

' Initialization
caption figure 1
title Projeto<$printer>\nEntrega SDS 001 <&check>
footer Giovani Perotto Mesquita\n18/01/2011 - 13:01
scale 1.5
hide footbox
'printscale weekly
project starts the 2021/01/01

' Day watching
'today is 2021/01/20 and is colored in Yellow
today is 14 days after start and is colored in Yellow

' Close Days
saturday are closed
sunday are closed
2021/01/01 is closed
2021/01/01 is colored in lightblue
2021/01/04 to 2021/01/08 are colored in coral

' Tasks and separators
-- Phase One --
[Prototype design] on {Alice} lasts 13 days
  [Prototype design] links to [[http://plantuml.com]]
'note bottom
'  memo1 ...
'  memo2 ...
'  explanations1 ...
'  explanations2 ...
'  <img:http://plantuml.com/logo3.png>
'end note
[Config prototype] on {Giovani} lasts 7 days
'note bottom
'  WiFi <&wifi>
'  |= |= table |= header |
'  | a | table | row |
'  |<#FF8080> red |<#80FF80> green |<#8080FF> blue |
'  <#yellow>| b | table | row |
'end note
-- Phase Two --
[QA prototype] on {Davi} lasts 9 days
[Test prototype] on {Camila:50}{Giovani:50} lasts 6 days
-- Phase Three --
[Deploy] lasts 1 day
'note bottom
'  Example of Tree
'  |_ First line
'  |_ **Bom(Model)**
'    |_ prop1
'    |_ prop2
'    |_ prop3
'  |_ Last line
'end note
[PD audict] lasts 10 days
[Trainning] on {Camila:50}{Maria:50} starts 2021/01/18
  [Trainning] ends 2021/02/12
  legend right
    This is a legend
  endlegend
-- Milestones --

' Tasks flow
[Config prototype] starts at [Prototype design]'s end with red bold link
[QA prototype] starts at [Prototype design]'s end with red bold link
[Test prototype] starts at [Config prototype]'s end with red bold link
  [Test prototype] starts at [QA prototype]'s end with red bold link
  [Test prototype] pauses on monday
[Deploy] starts at [Test prototype]'s end with red bold link
[PD audict] starts at [Deploy]'s end with red bold link

' Tasks progress
[Prototype design] is 70% completed
[Config prototype] is 0% completed
[QA prototype] is 23% completed
[Test prototype] is 0% completed
[Deploy] is 0% completed
[PD audict] is 0% completed
[Trainning] is 20% completed

' Milestones
[DevEnd] happens at [Prototype design]'s end
  [DevEnd] happens at [QA prototype]'s end
[ReadyDeploy] happens at [Test prototype]'s end
  [ReadyDeploy] displays on same row as [DevEnd]
[PDEnd] happens at [PD audict]'s end
[PDEnd] displays on same row as [ReadyDeploy]

' Colors
[Prototype design] is colored in Red/Red
[Config prototype] is colored in Red/Red
[QA prototype] is colored in Red/Red
[Test prototype] is colored in Red/Red
[Deploy] is colored in Red/Red
[PD audict] is colored in Red/Red
[DevEnd] is colored in White/Black
[ReadyDeploy] is colored in Gray/Black
@endgantt
```

<div align="center">:star2:</div>

## Code

``` dos
| @startgantt
| <style>
| 
|   ganttDiagram {
| 
|   	task {
|   		FontName Courrier
|   		FontColor black
|   		FontSize 12
|   		FontStyle bold
|   		BackGroundColor Blue
|   		LineColor blue
|   	}
| 
|   	milestone {
|   		FontColor blue
|   		FontSize 12
|   		FontStyle italic
|   		BackGroundColor gold
|   		LineColor red
|   	}
| 
|   	note {
|   		FontColor DarkGreen
|   		FontSize 10
|   		LineColor lightgreen
|         BackGroundColor orange\yellow
|   	}
| 
|   }
| 
|   footer {
|     HorizontalAlignment right
|   }
| 
|   title {
|     FontColor black
|     FontSize 40
|     FontStyle italic
|     HorizontalAlignment center
|   }
| 
| </style>
| 
| skinparam footerFontColor blue
| skinparam footerFontSize 10
| skinparam footerFontStyle italic
| 'skinparam titleBackgroundColor Aqua-CadetBlue
| 'skinparam titleBorderColor blue
| 'skinparam titleBorderRoundCorner 15
| 'skinparam titleBorderThickness 2
| 
| ' sprites
| sprite $printer [15x15/8z] NOtH3W0W208HxFz_kMAhj7lHWpa1XC716sz0Pq4MVPEWfBHIuxP3L6kbTcizR8tAhzaqFvXwvFfPEqm0
| 
| ' Initialization
| caption figure 1
| title Projeto<$printer>\nEntrega SDS 001 <&check>
| footer Giovani Perotto Mesquita\n18/01/2011 - 13:01
| scale 1.5
| hide footbox
| 'printscale weekly
| project starts the 2021/01/01
| 
| ' Day watching
| 'today is 2021/01/20 and is colored in Yellow
| today is 14 days after start and is colored in Yellow
| 
| ' Close Days
| saturday are closed
| sunday are closed
| 2021/01/01 is closed
| 2021/01/01 is colored in lightblue
| 2021/01/04 to 2021/01/08 are colored in coral
| 
| ' Tasks and separators
| -- Phase One --
| [Prototype design] on {Alice} lasts 13 days
|   [Prototype design] links to [[http://plantuml.com]]
| 'note bottom
| '  memo1 ...
| '  memo2 ...
| '  explanations1 ...
| '  explanations2 ...
| '  <img:http://plantuml.com/logo3.png>
| 'end note
| [Config prototype] on {Giovani} lasts 7 days
| 'note bottom
| '  WiFi <&wifi>
| '  |= |= table |= header |
| '  | a | table | row |
| '  |<#FF8080> red |<#80FF80> green |<#8080FF> blue |
| '  <#yellow>| b | table | row |
| 'end note
| -- Phase Two --
| [QA prototype] on {Davi} lasts 9 days
| [Test prototype] on {Camila:50}{Giovani:50} lasts 6 days
| -- Phase Three --
| [Deploy] lasts 1 day
| 'note bottom
| '  Example of Tree
| '  |_ First line
| '  |_ **Bom(Model)**
| '    |_ prop1
| '    |_ prop2
| '    |_ prop3
| '  |_ Last line
| 'end note
| [PD audict] lasts 10 days
| [Trainning] on {Camila:50}{Maria:50} starts 2021/01/18
|   [Trainning] ends 2021/02/12
|   legend right
|     This is a legend
|   endlegend
| -- Milestones --
| 
| ' Tasks flow
| [Config prototype] starts at [Prototype design]'s end with red bold link
| [QA prototype] starts at [Prototype design]'s end with red bold link
| [Test prototype] starts at [Config prototype]'s end with red bold link
|   [Test prototype] starts at [QA prototype]'s end with red bold link
|   [Test prototype] pauses on monday
| [Deploy] starts at [Test prototype]'s end with red bold link
| [PD audict] starts at [Deploy]'s end with red bold link
| 
| ' Tasks progress
| [Prototype design] is 70% completed
| [Config prototype] is 0% completed
| [QA prototype] is 23% completed
| [Test prototype] is 0% completed
| [Deploy] is 0% completed
| [PD audict] is 0% completed
| [Trainning] is 20% completed
| 
| ' Milestones
| [DevEnd] happens at [Prototype design]'s end
|   [DevEnd] happens at [QA prototype]'s end
| [ReadyDeploy] happens at [Test prototype]'s end
|   [ReadyDeploy] displays on same row as [DevEnd]
| [PDEnd] happens at [PD audict]'s end
| [PDEnd] displays on same row as [ReadyDeploy]
| 
| ' Colors
| [Prototype design] is colored in Red/Red
| [Config prototype] is colored in Red/Red
| [QA prototype] is colored in Red/Red
| [Test prototype] is colored in Red/Red
| [Deploy] is colored in Red/Red
| [PD audict] is colored in Red/Red
| [DevEnd] is colored in White/Black
| [ReadyDeploy] is colored in Gray/Black
| @endgantt
```