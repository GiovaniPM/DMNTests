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

# Building Gant diagrams with PlantUML

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

</style>

skinparam ...
```
- **style** - Looks like CSS format
    - **task**
        - **FontName**
  		- **FontColor**
  		- **FontSize**
  		- **FontStyle**
  		- **BackGroundColor**
  		- **LineColor**
  	- **milestone**
  		- **FontColor**
  		- **FontSize**
  		- **FontStyle**
  		- **BackGroundColor**
  		- **LineColor**
  	- **note**
      	- **FontColor**
  		- **FontSize**
  		- **LineColor**
        - **BackGroundColor**
    - **footer**
        - **HorizontalAlignment**
    - **title**
        - **FontColor**
        - **FontSize**
        - **FontStyle**
        - **HorizontalAlignment**
- **skinparam** - Parameters
    - **footerFontColor**
    - **footerFontSize**
    - **footerFontStyle**
    - **titleBackgroundColor**
    - **titleBorderColor**
    - **titleBorderRoundCorner**
    - **titleBorderThickness**

## Project initialization

- **title**
```plantuml
ex.:
    title Project\nDelivery SDS 001
```
- **footer**
```plantuml
ex.:
    footer Giovani Perotto Mesquita\n18/01/2011 - 13:01
```
- **scale**
```plantuml
ex.:
    scale 1.5
```
- **hide**
```plantuml
ex.:
    hide footbox
```
- **printscale**
```plantuml
ex.:
    printscale weekly
```
- **project**
```plantuml
ex.:
    project starts the 2021/01/01
```

## Project day vision

- **today**
```plantuml
ex.:
    today is 2021/01/20 and is colored in Yellow
or
    today is 14 days after start and is colored in Yellow
```

## Close days

- **closed**
```plantuml
ex.:
    saturday are closed
    sunday are closed
    2021/01/01 is closed
    2021/01/01 is colored in lightblue
```

## Separators

- **-- ... --**
```plantuml
ex.:
    -- Phase One --
```

## Tasks

- **task**
    - **dinamic**
    ```plantuml
    ex.:
        [PlantUML1] lasts 13 days
    ```
    - **fixed**
    ```plantuml
    ex.:
        [PlantUML1] starts 2021/01/18
        [PlantUML1] ends 2021/02/12
    ```
- **link**
```plantuml
ex.:
    [PlantUML1] links to [[http://plantuml.com]]
```
- **resources**
```plantuml
ex.:
    [PlantUML1] on {User1:50}{User2:50} lasts 6 days
```
- **pauses**
```plantuml
ex.:
    [PlantUML1] pauses on monday
or
    [PlantUML1] pauses on 2021/01/12
```
- **colors**
```plantuml
ex.:
    [PlantUML1] is colored in Red/Red
```
- **note**
```plantuml
ex.:
    note bottom
      memo1 ...
      memo2 ...
      explanations1 ...
      explanations2 ...
    end note
```

## Flow

- **link**
```plantuml
ex.:
    [PlantUML2] starts at [PlantUML1]'s end with red bold link
```

## Progress

- **completed**
```plantuml
ex.:
    [PlanUML1] is 70% completed
```

## Milestone

- **milestone**
```plantuml
ex.:
    [Milestone1] happens at [PlantUML1]'s end
```